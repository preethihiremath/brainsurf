import numpy as np

def compute_power_spectrum(data, sfreq, freq_range=(0, 100)):
    """
    Compute the power spectrum of a given data sequence.

    Parameters
    ----------
    data : ndarray, shape (n_samples,)
        The data to be analyzed.
    sfreq : float
        The sampling frequency of the data.
    freq_range : tuple of float, optional
        The frequency range to compute the power spectrum over. Default is (0, 100).

    Returns
    -------
    freqs : ndarray, shape (n_freqs,)
        The frequency values.
    power_spectrum : ndarray, shape (n_freqs,)
        The power spectrum.
    """
    # compute the number of frequency bins
    n_freqs = int(sfreq/2) + 1

    # compute the power spectrum using FFT
    fft_data = np.fft.rfft(data)
    power_spectrum = np.abs(fft_data)**2 / len(data)

    # extract the frequency range of interest
    freqs = np.fft.rfftfreq(len(data), 1.0/sfreq)
    mask = (freqs >= freq_range[0]) & (freqs <= freq_range[1])
    freqs = freqs[mask]
    power_spectrum = power_spectrum[mask]

    return freqs, power_spectrum
