import numpy as np

def compute_time_frequency(data, sfreq, freqs, method='morlet', n_cycles=7):
    """
    Compute the time-frequency representation of a given data sequence.

    Parameters
    ----------
    data : ndarray, shape (n_samples,)
        The data to be analyzed.
    sfreq : float
        The sampling frequency of the data.
    freqs : ndarray, shape (n_freqs,)
        The frequency values to compute the time-frequency representation over.
    method : str, optional
        The method to use for the time-frequency decomposition. Default is 'morlet'.
    n_cycles : float, optional
        The number of cycles to use for the Morlet wavelet. Default is 7.

    Returns
    -------
    power : ndarray, shape (n_freqs, n_samples)
        The power spectral density for each frequency band and time point.
    """
    from scipy.signal import morlet2

    # compute the time-frequency representation using Morlet wavelets
    n_samples = len(data)
    time_bandwidth = 2 * n_cycles
    power = np.zeros((len(freqs), n_samples))
    for i, freq in enumerate(freqs):
        w = 2 * np.pi * freq
        wavelet = morlet2(n_samples, w, time_bandwidth)
        convolved = np.convolve(data, wavelet, mode='same')
        power[i, :] = np.abs(convolved)**2

    return power
