import numpy as np
from scipy.signal import welch, coherence, correlate
import astropy as ast 


def extract_frequency_bands(raw_data, fs=128, epoch_size=1000):
    raw_data = np.asarray(raw_data, dtype=float)
    raw_data = raw_data[~np.isnan(raw_data)]
    if len(raw_data) == 0:
        raise ValueError("raw_data must contain numeric values.")

    epoch_samples = max(2, int(round(epoch_size)))
    data = {}
    bands = {
        'delta': (1, 4),
        'theta': (4, 8),
        'alpha': (8, 13),
        'beta': (13, 30),
        'gamma': (30, 50),
    }

    for band, (low, high) in bands.items():
        features = np.full(len(raw_data), np.nan)
        for start in range(0, len(raw_data), epoch_samples):
            stop = min(start + epoch_samples, len(raw_data))
            epoch = raw_data[start:stop]
            if len(epoch) < 2:
                continue

            f, psd = welch(epoch, fs=fs, nperseg=min(256, len(epoch)))
            band_psd = psd[(f >= low) & (f <= high)]
            features[start:stop] = np.mean(band_psd) if band_psd.size else np.nan

        data[band] = features
            
    return data

def psd_fft(data, sfreq, freq_range=(0, 100)):
    data = np.asarray(data, dtype=float)
    data = data[~np.isnan(data)]
    if len(data) == 0:
        raise ValueError("data must contain numeric values.")

    fft_data = np.fft.rfft(data)
    power_spectrum = np.abs(fft_data)**2 / len(data)
    freqs = np.fft.rfftfreq(len(data), 1.0/sfreq)
    mask = (freqs >= freq_range[0]) & (freqs <= freq_range[1])
    freqs = freqs[mask]
    power_spectrum = power_spectrum[mask]
    return freqs, power_spectrum

def psd_welch(data, fs=None, sampling_freq=None):
    if fs is None:
        fs = sampling_freq
    if fs is None:
        raise ValueError("Sampling frequency must be provided using fs or sampling_freq.")

    data = np.asarray(data, dtype=float)
    data = data[~np.isnan(data)]
    if len(data) == 0:
        raise ValueError("data must contain numeric values.")

    nperseg = calculate_nperseg(data)
    freqs, psd = welch(data, fs=fs, nperseg=nperseg)
    return freqs, psd

def psd_lombscargle(signal, fs):
    time = np.arange(len(signal))/fs
    frequency, power = ast.timeseries.LombScargle(time, signal).autopower(normalization='psd')
    return frequency, power

# def psd_multitaper(signal, fs, nperseg=256, NW=3):
#     f, Pxx = multitaper(signal, fs, nperseg=nperseg, NW=NW, adaptive=True)
#     return f, Pxx.mean(axis=1)

# def psd_periodogram(signal, fs, nfft=None):
#     f, Pxx = periodogram(signal, fs, nfft=nfft)
#     return f, Pxx

def calculate_nperseg(data):
    n = len(data)
    if n < 256:
        nperseg = n
    elif n < 2048:
        nperseg = 256
    else:
        nperseg = 1024
    return nperseg
