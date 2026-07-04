from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

from brainsurf.analysis.power_spectrum import psd_welch
from brainsurf.analysis.stats_analysis import (
    calc_ap_entropy,
    calc_fractal_dimension,
    calculate_kurtosis,
    calculate_skewness,
)
from brainsurf.cognitive_analysis_module.cognitive_indexes import (
    calculate_alertness,
    calculate_arousal_index,
    calculate_band_power,
    calculate_engagement,
    calculate_load_index,
    calculate_neural_activity,
    calculate_pe,
)
from brainsurf.data.eeg_data import EEGDataFactory
from brainsurf.machine_learning import EEGClassifier
from brainsurf.preprocessing.baseline import apply_baseline
from brainsurf.preprocessing.filtering import (
    butter_bandpass_filter,
    common_average_reference,
    highpass_filter,
    lowpass_filter,
    notch_filter,
)

try:
    from brainsurf.preprocessing.artifact_removal import wavelet_denoising

    WAVELET_AVAILABLE = True
except ModuleNotFoundError:
    WAVELET_AVAILABLE = False


ROOT = Path(__file__).parent
SAMPLE_MANIFEST = ROOT / "brainsurf/data/samples/sample_manifest.csv"
DEFAULT_SAMPLE = ROOT / "brainsurf/data/samples/reference/sample_data.csv"
SUPPORTED_UPLOADS = ["csv", "xlsx", "xls"]
COMPARISON_PRESETS = {
    "Adarsh meditation: pre vs post": (
        "brainsurf/data/samples/cohort/adarsh/eeg/pre_meditation.csv",
        "brainsurf/data/samples/cohort/adarsh/eeg/post_meditation.csv",
    ),
    "Anirudh meditation: pre vs post": (
        "brainsurf/data/samples/cohort/anirudh/eeg/pre_meditation.csv",
        "brainsurf/data/samples/cohort/anirudh/eeg/post_meditation.csv",
    ),
    "Yogesh meditation: pre vs post": (
        "brainsurf/data/samples/cohort/yogesh/eeg/pre_meditation.csv",
        "brainsurf/data/samples/cohort/yogesh/eeg/post_meditation.csv",
    ),
    "Adarsh cognitive: pre vs post": (
        "brainsurf/data/samples/cohort/adarsh/cognitive/pre_cognitive_eeg.csv",
        "brainsurf/data/samples/cohort/adarsh/cognitive/post_cognitive_eeg.csv",
    ),
    "Single built-in sample": None,
}
BANDS = {
    "delta": (0.5, 4),
    "theta": (4, 8),
    "alpha": (8, 13),
    "beta": (13, 30),
    "gamma": (30, 50),
}
COGNITIVE_FORMULAS = {
    "Performance": "beta / alpha",
    "Arousal": "alpha / theta",
    "Engagement": "(alpha + theta) / delta",
    "Load": "alpha / beta",
    "Alertness": "alpha / (alpha + theta)",
    "Neural activity": "(delta + theta) / (alpha + beta)",
}


def page_style():
    st.markdown(
        """
        <style>
        .stApp {
            background: #f6f8f5;
            color: #18221f;
        }
        .block-container {
            padding-top: 1.4rem;
            padding-bottom: 3rem;
            max-width: 1380px;
        }
        [data-testid="stSidebar"] {
            background: #13201d;
        }
        [data-testid="stSidebar"] * {
            color: #f7fbf8;
        }
        .hero {
            padding: 1.1rem 0 1.35rem;
            border-bottom: 1px solid rgba(34, 55, 48, 0.16);
            margin-bottom: 1rem;
        }
        .hero h1 {
            margin: 0;
            color: #13201d;
            font-size: 2.35rem;
            line-height: 1.05;
            font-weight: 760;
        }
        .hero p {
            margin: 0.45rem 0 0;
            color: #54645f;
            font-size: 1rem;
        }
        .section-label {
            color: #24745c;
            font-weight: 760;
            text-transform: uppercase;
            font-size: 0.76rem;
            letter-spacing: 0.06rem;
            margin: 0.2rem 0 0.45rem;
        }
        div[data-testid="stMetric"] {
            background: #ffffff;
            border: 1px solid rgba(34, 55, 48, 0.14);
            border-radius: 8px;
            padding: 0.85rem 0.95rem;
            box-shadow: 0 10px 28px rgba(19, 32, 29, 0.055);
        }
        div[data-testid="stMetric"] label {
            color: #53645f;
        }
        .stTabs [data-baseweb="tab-list"] {
            gap: 0.25rem;
            border-bottom: 1px solid rgba(34, 55, 48, 0.14);
        }
        .stTabs [data-baseweb="tab"] {
            background: transparent;
            border-radius: 6px 6px 0 0;
            padding: 0.6rem 0.9rem;
        }
        .stTabs [aria-selected="true"] {
            background: #ffffff;
            border: 1px solid rgba(34, 55, 48, 0.14);
            border-bottom: 1px solid #ffffff;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


@st.cache_data
def load_manifest():
    if not SAMPLE_MANIFEST.exists():
        return pd.DataFrame()
    manifest = pd.read_csv(SAMPLE_MANIFEST)
    return manifest[manifest["modality"].str.contains("EEG CSV", na=False)].copy()


@st.cache_data
def read_local_table(path_text):
    path = Path(path_text)
    if not path.is_absolute():
        path = ROOT / path
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    return read_table(path), str(path.relative_to(ROOT) if path.is_relative_to(ROOT) else path)


def read_table(source):
    name = str(getattr(source, "name", source)).lower()
    if name.endswith(".csv"):
        return pd.read_csv(source)
    if name.endswith(".xlsx") or name.endswith(".xls"):
        return pd.read_excel(source)
    raise ValueError("Use a CSV or Excel file for the workbench.")


def load_builtin_sample(selected_sample):
    manifest = load_manifest()
    if manifest.empty:
        return read_table(DEFAULT_SAMPLE), str(DEFAULT_SAMPLE.relative_to(ROOT))

    row = manifest.loc[manifest["session_state"].eq(selected_sample)].head(1)
    path = ROOT / row.iloc[0]["path"] if not row.empty else DEFAULT_SAMPLE
    return read_table(path), str(path.relative_to(ROOT))


def load_preset_side(preset_name, side):
    preset = COMPARISON_PRESETS.get(preset_name)
    if preset is None:
        return None

    path = ROOT / preset[0 if side == "primary" else 1]
    return read_table(path), str(path.relative_to(ROOT))


def load_input(uploaded_file, selected_sample, manual_path, comparison_preset):
    if uploaded_file is not None:
        return read_table(uploaded_file), uploaded_file.name
    if manual_path:
        return read_local_table(manual_path)
    preset_primary = load_preset_side(comparison_preset, "primary")
    if preset_primary is not None:
        return preset_primary
    return load_builtin_sample(selected_sample)


def to_eeg_frame(df):
    eeg_data = EEGDataFactory().create_eeg_data(df)
    eeg_frame = eeg_data.get_data().copy()
    signal_columns = [column for column in eeg_data.signal_columns if column in eeg_frame.columns]
    if not signal_columns and "raw" in eeg_frame.columns:
        signal_columns = ["raw"]
    return eeg_data, eeg_frame, signal_columns


def numeric_array(series):
    return pd.to_numeric(series, errors="coerce").to_numpy(dtype=float)


def clean_signal(series):
    values = numeric_array(series)
    values = values[~np.isnan(values)]
    if len(values) == 0:
        raise ValueError("Selected signal does not contain numeric EEG values.")
    return values


def validate_config(config):
    nyquist = config["sampling_freq"] / 2
    if config["filter_mode"] in {"Bandpass", "Low-pass"} and config["high_freq"] >= nyquist:
        return f"High cutoff must be below Nyquist frequency ({nyquist:.1f} Hz)."
    if config["filter_mode"] in {"Bandpass", "High-pass"} and config["low_freq"] <= 0:
        return "Low cutoff must be greater than 0 Hz."
    if config["filter_mode"] == "Bandpass" and config["low_freq"] >= config["high_freq"]:
        return "Low cutoff must be lower than high cutoff."
    if config["apply_notch"] and config["notch_freq"] >= nyquist:
        return f"Notch frequency must be below Nyquist frequency ({nyquist:.1f} Hz)."
    return None


def process_signal(signal, eeg_frame, signal_columns, signal_col, config):
    processed = np.asarray(signal, dtype=float)

    if config["apply_car"] and len(signal_columns) > 1 and signal_col in signal_columns:
        channels = eeg_frame[signal_columns].apply(pd.to_numeric, errors="coerce").dropna()
        referenced = common_average_reference(channels.to_numpy(dtype=float).T, axis=0).T
        processed = referenced[:, signal_columns.index(signal_col)]

    if config["apply_baseline"]:
        processed = apply_baseline(
            processed.reshape(1, -1),
            config["sampling_freq"],
            baseline=(None, None),
        )[0]

    if config["filter_mode"] == "Bandpass":
        processed = butter_bandpass_filter(
            processed,
            lowcut=config["low_freq"],
            highcut=config["high_freq"],
            fs=config["sampling_freq"],
            order=config["filter_order"],
        )
    elif config["filter_mode"] == "Low-pass":
        processed = lowpass_filter(
            processed,
            cutoff_freq=config["high_freq"],
            fs=config["sampling_freq"],
            order=config["filter_order"],
        )
    elif config["filter_mode"] == "High-pass":
        processed = highpass_filter(
            processed,
            cutoff_freq=config["low_freq"],
            fs=config["sampling_freq"],
            order=config["filter_order"],
        )

    if config["apply_notch"]:
        processed = notch_filter(
            processed,
            fs=config["sampling_freq"],
            freqs=config["notch_freq"],
            q=30,
        )

    if config["apply_wavelet"]:
        processed = wavelet_denoising(processed)
        processed = processed[: len(signal)]

    return np.asarray(processed, dtype=float)


def safe_metric(value):
    if value is None or not np.isfinite(value):
        return "n/a"
    return f"{value:.4f}"


def signal_stats(signal):
    preview = signal[: min(len(signal), 3000)]
    values = {
        "Mean": np.nanmean(signal),
        "Std Dev": np.nanstd(signal),
        "Skewness": calculate_skewness(preview),
        "Kurtosis": calculate_kurtosis(preview),
    }
    if len(preview) > 20:
        try:
            values["Sample Entropy"] = calc_ap_entropy(preview)
        except Exception:
            values["Sample Entropy"] = np.nan
        try:
            values["DFA"] = calc_fractal_dimension(preview)
        except Exception:
            values["DFA"] = np.nan
    return values


def spectral_features(signal, sampling_freq):
    freqs, psd = psd_welch(signal, fs=sampling_freq)
    band_power = calculate_band_power(freqs, psd, BANDS)
    eps = np.finfo(float).eps
    alpha = band_power["alpha"] + eps
    beta = band_power["beta"] + eps
    theta = band_power["theta"] + eps
    delta = band_power["delta"] + eps
    cognitive = {
        "Performance": calculate_pe(alpha, beta),
        "Arousal": calculate_arousal_index(alpha, theta),
        "Engagement": calculate_engagement(alpha, theta, delta),
        "Load": calculate_load_index(alpha, beta),
        "Alertness": calculate_alertness(alpha, theta),
        "Neural activity": calculate_neural_activity(delta, theta, alpha, beta),
    }
    return freqs, psd, band_power, cognitive


def plot_signal(raw, processed, column_name, max_points):
    raw = raw[:max_points]
    processed = processed[:max_points]
    fig, ax = plt.subplots(figsize=(12.5, 4.8))
    fig.patch.set_facecolor("#ffffff")
    ax.set_facecolor("#fbfcfb")
    ax.plot(raw, color="#697a75", linewidth=1, alpha=0.42, label="Raw")
    ax.plot(processed, color="#24745c", linewidth=1.35, label="Processed")
    ax.set_title(f"{column_name} signal")
    ax.set_xlabel("Sample")
    ax.set_ylabel("Amplitude")
    ax.grid(alpha=0.18)
    ax.legend(frameon=False)
    return fig


def plot_psd(freqs, psd):
    fig, ax = plt.subplots(figsize=(12.5, 4.8))
    fig.patch.set_facecolor("#ffffff")
    ax.set_facecolor("#fbfcfb")
    ax.plot(freqs, psd, color="#245d74", linewidth=1.5)
    for name, (start, end) in BANDS.items():
        ax.axvspan(start, end, alpha=0.08, label=name)
    ax.set_xlim(0, min(60, max(freqs) if len(freqs) else 60))
    ax.set_title("Welch power spectral density")
    ax.set_xlabel("Frequency (Hz)")
    ax.set_ylabel("Power")
    ax.grid(alpha=0.18)
    ax.legend(frameon=False, ncol=5)
    return fig


def plot_band_power(band_power, title="Band power"):
    labels = list(band_power.keys())
    values = [band_power[label] for label in labels]
    colors = ["#6b8f71", "#24745c", "#245d74", "#b57f3b", "#7a5c95"]
    fig, ax = plt.subplots(figsize=(8.5, 4.6))
    fig.patch.set_facecolor("#ffffff")
    ax.set_facecolor("#fbfcfb")
    ax.bar(labels, values, color=colors)
    ax.set_title(title)
    ax.set_ylabel("Integrated power")
    ax.grid(axis="y", alpha=0.18)
    return fig


def plot_comparison(primary, secondary, primary_name, secondary_name, max_points):
    limit = min(max_points, len(primary), len(secondary))
    fig, ax = plt.subplots(figsize=(12.5, 4.8))
    fig.patch.set_facecolor("#ffffff")
    ax.set_facecolor("#fbfcfb")
    ax.plot(primary[:limit], color="#24745c", linewidth=1.25, label=primary_name)
    ax.plot(secondary[:limit], color="#b57f3b", linewidth=1.05, alpha=0.85, label=secondary_name)
    ax.set_title("Processed signal comparison")
    ax.set_xlabel("Sample")
    ax.set_ylabel("Amplitude")
    ax.grid(alpha=0.18)
    ax.legend(frameon=False)
    return fig


def plot_band_comparison(primary_band, secondary_band):
    labels = list(BANDS.keys())
    x = np.arange(len(labels))
    width = 0.36
    fig, ax = plt.subplots(figsize=(10, 4.8))
    fig.patch.set_facecolor("#ffffff")
    ax.set_facecolor("#fbfcfb")
    ax.bar(x - width / 2, [primary_band[label] for label in labels], width, label="Primary", color="#24745c")
    ax.bar(x + width / 2, [secondary_band[label] for label in labels], width, label="Comparison", color="#b57f3b")
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylabel("Integrated power")
    ax.set_title("Band power comparison")
    ax.grid(axis="y", alpha=0.18)
    ax.legend(frameon=False)
    return fig


def comparison_table(primary_band, secondary_band):
    rows = []
    for band in BANDS:
        primary_value = primary_band[band]
        comparison_value = secondary_band[band]
        delta = comparison_value - primary_value
        pct_delta = np.nan
        if np.isfinite(primary_value) and abs(primary_value) > np.finfo(float).eps:
            pct_delta = (delta / abs(primary_value)) * 100
        rows.append(
            {
                "Band": band,
                "Primary": primary_value,
                "Comparison": comparison_value,
                "Delta": delta,
                "Delta %": pct_delta,
            }
        )
    return pd.DataFrame(rows)


def cognitive_comparison_table(primary_cognitive, secondary_cognitive):
    rows = []
    for name in primary_cognitive:
        primary_value = primary_cognitive[name]
        comparison_value = secondary_cognitive[name]
        rows.append(
            {
                "Index": name,
                "Primary": primary_value,
                "Comparison": comparison_value,
                "Delta": comparison_value - primary_value,
                "Formula": COGNITIVE_FORMULAS[name],
            }
        )
    return pd.DataFrame(rows)


def infer_comparison(primary_band, secondary_band, primary_cognitive, secondary_cognitive):
    band_df = comparison_table(primary_band, secondary_band)
    valid = band_df.replace([np.inf, -np.inf], np.nan).dropna(subset=["Delta %"])
    if valid.empty:
        return "The comparison loaded, but the band-power values are too small or incomplete for a stable summary."

    strongest = valid.iloc[valid["Delta %"].abs().argmax()]
    direction = "increased" if strongest["Delta"] > 0 else "decreased"
    cognitive_df = cognitive_comparison_table(primary_cognitive, secondary_cognitive)
    cognitive_delta = cognitive_df.iloc[cognitive_df["Delta"].abs().argmax()]
    cognitive_direction = "increased" if cognitive_delta["Delta"] > 0 else "decreased"

    return (
        f"The largest spectral shift is in {strongest['Band']} power, which {direction} "
        f"by {abs(strongest['Delta %']):.1f}% in the comparison file. "
        f"The largest derived cognitive-index shift is {cognitive_delta['Index']}, "
        f"which {cognitive_direction}. Treat this as an exploratory BrainSurf feature summary, "
        "not a clinical conclusion."
    )


def plot_channel_correlation(eeg_frame, signal_columns):
    channel_frame = eeg_frame[signal_columns].apply(pd.to_numeric, errors="coerce").dropna()
    if len(signal_columns) < 2 or channel_frame.empty:
        return None
    corr = channel_frame.corr()
    fig, ax = plt.subplots(figsize=(8, 6))
    fig.patch.set_facecolor("#ffffff")
    im = ax.imshow(corr, cmap="viridis", vmin=-1, vmax=1)
    ax.set_xticks(range(len(corr.columns)))
    ax.set_yticks(range(len(corr.index)))
    ax.set_xticklabels(corr.columns, rotation=45, ha="right")
    ax.set_yticklabels(corr.index)
    ax.set_title("Channel correlation")
    fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    return fig


def build_ml_features(signal, sampling_freq, window_size):
    rows = []
    labels = []
    median_value = np.nanmedian(signal)
    for start in range(0, len(signal) - window_size + 1, window_size):
        window = signal[start : start + window_size]
        if len(window) < 4:
            continue
        freqs, psd = psd_welch(window, fs=sampling_freq)
        powers = calculate_band_power(freqs, psd, BANDS)
        rows.append(
            [
                np.nanmean(window),
                np.nanstd(window),
                np.nanmin(window),
                np.nanmax(window),
                np.nanpercentile(window, 25),
                np.nanpercentile(window, 75),
                powers["delta"],
                powers["theta"],
                powers["alpha"],
                powers["beta"],
                powers["gamma"],
            ]
        )
        labels.append(int(np.nanmean(window) > median_value))
    return np.asarray(rows, dtype=float), np.asarray(labels, dtype=int)


def run_ml(signal, sampling_freq, model_type, window_size):
    features, labels = build_ml_features(signal, sampling_freq, window_size)
    if len(features) < 8 or len(np.unique(labels)) < 2:
        raise ValueError("Not enough varied windows for ML. Try a smaller window or a longer signal.")
    split = max(2, int(len(features) * 0.75))
    if split >= len(features):
        split = len(features) - 1
    classifier = EEGClassifier(model_type=model_type.lower())
    classifier.train(features[:split], labels[:split])
    predictions = classifier.predict(features[split:])
    accuracy = classifier.evaluate(features[split:], labels[split:])
    return {
        "accuracy": accuracy,
        "windows": len(features),
        "train_windows": split,
        "test_windows": len(features) - split,
        "predictions": predictions,
        "labels": labels[split:],
    }


def render_metric_row(values):
    cols = st.columns(len(values))
    for col, (label, value) in zip(cols, values.items()):
        col.metric(label, safe_metric(value) if isinstance(value, float) else value)


def main():
    st.set_page_config(page_title="BrainSurf EEG Workbench", layout="wide")
    page_style()

    st.markdown(
        """
        <div class="hero">
            <h1>BrainSurf EEG Workbench</h1>
            <p>Load common EEG tables, preprocess signals, compare sessions, extract spectral/cognitive features, and run BrainSurf classification.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    manifest = load_manifest()
    sample_options = list(dict.fromkeys(manifest["session_state"].tolist())) if not manifest.empty else ["demo_csv"]
    default_sample = "demo_csv" if "demo_csv" in sample_options else sample_options[0]

    with st.sidebar:
        st.header("Dataset")
        comparison_preset = st.selectbox(
            "Built-in workflow",
            list(COMPARISON_PRESETS.keys()),
            index=0,
        )
        uploaded_file = st.file_uploader("Primary CSV/Excel", type=SUPPORTED_UPLOADS)
        selected_sample = st.selectbox(
            "Built-in sample",
            sample_options,
            index=sample_options.index(default_sample),
            disabled=uploaded_file is not None or COMPARISON_PRESETS[comparison_preset] is not None,
        )
        manual_path = st.text_input("Manual CSV/Excel path", value="")
        comparison_file = st.file_uploader("Comparison CSV/Excel", type=SUPPORTED_UPLOADS)

        st.header("Preprocessing")
        sampling_freq = st.number_input("Sampling rate (Hz)", 1.0, 5000.0, 200.0, 1.0)
        filter_mode = st.selectbox("Filter", ["Bandpass", "Low-pass", "High-pass", "None"])
        low_freq = st.slider("Low cutoff (Hz)", 0.1, 100.0, 1.0, 0.1)
        high_freq = st.slider("High cutoff (Hz)", 1.0, 120.0, 40.0, 0.5)
        filter_order = st.slider("Filter order", 1, 10, 4)
        apply_notch = st.checkbox("Notch line noise", value=False)
        notch_freq = st.selectbox("Notch frequency", [50.0, 60.0], index=1)
        apply_car = st.checkbox("Common average reference", value=False)
        apply_baseline_option = st.checkbox("Baseline correction", value=False)
        apply_wavelet = st.checkbox("Wavelet denoise", value=False, disabled=not WAVELET_AVAILABLE)
        if not WAVELET_AVAILABLE:
            st.caption("Wavelet denoise is unavailable because PyWavelets is not installed.")
        max_points = st.slider("Plot samples", 500, 20000, 3000, 500)

    try:
        source_df, source_name = load_input(uploaded_file, selected_sample, manual_path, comparison_preset)
        eeg_data, eeg_frame, signal_columns = to_eeg_frame(source_df)
    except Exception as exc:
        st.error(f"Could not load primary EEG data: {exc}")
        return

    inferred_fs = eeg_data.sampling_frequency
    if inferred_fs and not uploaded_file and not manual_path:
        sampling_freq = float(inferred_fs)

    selectable_signals = ["raw"] + [column for column in signal_columns if column != "raw"]
    selectable_signals = [column for column in dict.fromkeys(selectable_signals) if column in eeg_frame.columns]
    if not selectable_signals:
        st.error("No usable EEG signal columns were found.")
        return

    top_cols = st.columns([2, 1, 1, 1])
    with top_cols[0]:
        signal_col = st.selectbox("Signal", selectable_signals)
    with top_cols[1]:
        st.metric("Rows", f"{len(eeg_frame):,}")
    with top_cols[2]:
        st.metric("Signals", len(signal_columns))
    with top_cols[3]:
        st.metric("Rate", f"{sampling_freq:.1f} Hz")

    config = {
        "sampling_freq": sampling_freq,
        "filter_mode": filter_mode,
        "low_freq": low_freq,
        "high_freq": high_freq,
        "filter_order": filter_order,
        "apply_notch": apply_notch,
        "notch_freq": notch_freq,
        "apply_car": apply_car,
        "apply_baseline": apply_baseline_option,
        "apply_wavelet": apply_wavelet,
    }

    error = validate_config(config)
    if error:
        st.error(error)
        return

    try:
        raw_signal = clean_signal(eeg_frame[signal_col])
        processed_signal = process_signal(raw_signal, eeg_frame, signal_columns, signal_col, config)
        freqs, psd, band_power, cognitive = spectral_features(processed_signal, sampling_freq)
        stats = signal_stats(processed_signal)
    except Exception as exc:
        st.error(f"Analysis failed: {exc}")
        return

    st.caption(f"Primary source: {source_name}")

    comparison = None
    preset_comparison = None
    if comparison_file is None and not uploaded_file and not manual_path:
        preset_comparison = load_preset_side(comparison_preset, "comparison")

    if comparison_file is not None or preset_comparison is not None:
        try:
            if comparison_file is not None:
                comparison_df = read_table(comparison_file)
                comparison_name = comparison_file.name
            else:
                comparison_df, comparison_name = preset_comparison

            comparison_data, comparison_frame, comparison_signals = to_eeg_frame(comparison_df)
            comparison_col = signal_col if signal_col in comparison_frame.columns else "raw"
            comparison_raw = clean_signal(comparison_frame[comparison_col])
            comparison_processed = process_signal(
                comparison_raw,
                comparison_frame,
                comparison_signals,
                comparison_col,
                config,
            )
            comparison_freqs, comparison_psd, comparison_band, comparison_cognitive = spectral_features(
                comparison_processed,
                sampling_freq,
            )
            comparison = {
                "name": comparison_name,
                "frame": comparison_frame,
                "signal": comparison_processed,
                "freqs": comparison_freqs,
                "psd": comparison_psd,
                "band": comparison_band,
                "cognitive": comparison_cognitive,
            }
        except Exception as exc:
            st.warning(f"Comparison input skipped: {exc}")

    overview_tab, spectrum_tab, cognitive_tab, compare_tab, ml_tab, data_tab = st.tabs(
        ["Overview", "Spectrum", "Cognitive", "Compare", "ML", "Data"]
    )

    with overview_tab:
        st.markdown('<div class="section-label">Processed Signal</div>', unsafe_allow_html=True)
        render_metric_row(stats)
        st.pyplot(plot_signal(raw_signal, processed_signal, signal_col, max_points), use_container_width=True)

        corr_fig = plot_channel_correlation(eeg_frame, signal_columns)
        if corr_fig is not None:
            st.pyplot(corr_fig, use_container_width=True)

    with spectrum_tab:
        left, right = st.columns([1.45, 1])
        with left:
            st.pyplot(plot_psd(freqs, psd), use_container_width=True)
        with right:
            st.pyplot(plot_band_power(band_power), use_container_width=True)
            st.dataframe(
                pd.DataFrame({"Band": list(band_power.keys()), "Power": list(band_power.values())}),
                use_container_width=True,
            )

    with cognitive_tab:
        st.markdown('<div class="section-label">Band-Derived Cognitive Metrics</div>', unsafe_allow_html=True)
        cognitive_cols = st.columns(3)
        for index, (label, value) in enumerate(cognitive.items()):
            cognitive_cols[index % 3].metric(label, safe_metric(value))
        st.dataframe(
            pd.DataFrame(
                {
                    "Index": list(cognitive.keys()),
                    "Value": list(cognitive.values()),
                    "Based on": [COGNITIVE_FORMULAS[label] for label in cognitive],
                }
            ),
            use_container_width=True,
        )

    with compare_tab:
        if comparison is None:
            st.info("Choose a built-in pre/post workflow or upload a comparison CSV/Excel file to compare sessions or groups.")
        else:
            st.caption(f"Comparison source: {comparison['name']}")
            st.markdown('<div class="section-label">Feature Inference</div>', unsafe_allow_html=True)
            st.info(infer_comparison(band_power, comparison["band"], cognitive, comparison["cognitive"]))
            st.pyplot(
                plot_comparison(
                    processed_signal,
                    comparison["signal"],
                    "Primary",
                    "Comparison",
                    max_points,
                ),
                use_container_width=True,
            )
            st.pyplot(plot_band_comparison(band_power, comparison["band"]), use_container_width=True)
            st.dataframe(comparison_table(band_power, comparison["band"]), use_container_width=True)
            st.dataframe(
                cognitive_comparison_table(cognitive, comparison["cognitive"]),
                use_container_width=True,
            )

    with ml_tab:
        st.markdown('<div class="section-label">BrainSurf Classification</div>', unsafe_allow_html=True)
        ml_cols = st.columns([1, 1, 2])
        with ml_cols[0]:
            model_type = st.radio("Model", ["SVM", "LDA"], horizontal=True)
        with ml_cols[1]:
            window_size = st.number_input("Window size", 32, 4096, 256, 32)
        with ml_cols[2]:
            st.caption("Windows are represented with summary and band-power features, then classified with BrainSurf EEGClassifier.")

        if st.button("Run ML analysis", type="primary"):
            try:
                result = run_ml(processed_signal, sampling_freq, model_type, int(window_size))
                ml_metrics = {
                    "Accuracy": result["accuracy"],
                    "Windows": f"{result['windows']:,}",
                    "Train": f"{result['train_windows']:,}",
                    "Test": f"{result['test_windows']:,}",
                }
                render_metric_row(ml_metrics)
                st.dataframe(
                    pd.DataFrame(
                        {
                            "Actual": result["labels"],
                            "Predicted": result["predictions"],
                        }
                    ),
                    use_container_width=True,
                )
            except Exception as exc:
                st.error(f"ML analysis failed: {exc}")

    with data_tab:
        st.markdown('<div class="section-label">Normalized BrainSurf Frame</div>', unsafe_allow_html=True)
        st.dataframe(eeg_frame.head(1000), use_container_width=True)
        export = eeg_frame.copy()
        export["processed_signal"] = np.nan
        export.loc[: len(processed_signal) - 1, "processed_signal"] = processed_signal
        st.download_button(
            "Download processed CSV",
            export.to_csv(index=False),
            file_name="brainsurf_processed.csv",
            mime="text/csv",
        )


if __name__ == "__main__":
    main()
