import numpy as np


def compute_mean_baseline(data, sfreq, baseline=(None, 0)):
    """Compute the mean baseline of data.

    Parameters
    ----------
    data : array, shape (n_channels, n_samples)
        The data to compute the mean baseline of.
    sfreq : float
        The sampling frequency of the data.
    baseline : tuple of length 2 (default: (None, 0))
        The time interval to use as the baseline. If None, the entire data is used
        as the baseline. If the first element is None, the beginning of the data is
        used as the start of the baseline. If the second element is None, the end
        of the data is used as the end of the baseline.

    Returns
    -------
    baseline_mean : array, shape (n_channels,)
        The mean baseline of each channel.
    """
    if baseline[0] is None:
        start = 0
    else:
        start = int(round(baseline[0] * sfreq))
    if baseline[1] is None:
        end = data.shape[1]
    else:
        end = int(round(baseline[1] * sfreq))

    baseline_data = data[:, start:end]
    baseline_mean = np.mean(baseline_data, axis=1)

    return baseline_mean


def apply_baseline(data, sfreq, baseline=(None, 0)):
    """Apply baseline correction to data.

    Parameters
    ----------
    data : array, shape (n_channels, n_samples)
        The data to apply baseline correction to.
    sfreq : float
        The sampling frequency of the data.
    baseline : tuple of length 2 (default: (None, 0))
        The time interval to use as the baseline. If None, the entire data is used
        as the baseline. If the first element is None, the beginning of the data is
        used as the start of the baseline. If the second element is None, the end
        of the data is used as the end of the baseline.

    Returns
    -------
    data_bc : array, shape (n_channels, n_samples)
        The data with baseline correction applied.
    """
    baseline_mean = compute_mean_baseline(data, sfreq, baseline)
    data_bc = data - baseline_mean[:, np.newaxis]

    return data_bc
