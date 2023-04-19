import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def welch_power_spectrum(data, sfreq, nperseg=1024):
    """
    Calculate the power spectrum of EEG data using the Welch method.
    
    Parameters
    ----------
    data : array-like, shape (n_channels, n_samples)
        The EEG data.
    sfreq : float
        The sampling frequency of the data, in Hz.
    nperseg : int
        The length of each segment for the Welch method (default=256).
    noverlap : int or None
        The number of samples to overlap between segments for the Welch method (default=None, which sets noverlap to nperseg // 2).
    
    Returns
    -------
    freqs : array-like, shape (n_freqs,)
        The frequency values for the power spectrum.
    power_spectrum : array-like, shape (n_channels, n_freqs)
        The power spectrum of the EEG data.
    """
    # n_channels, n_samples = data.shape
    eeg=data.iloc[:, 1]
    freqs, psd = signal.welch(eeg, sfreq, nperseg=nperseg)
    plt.figure()
    plt.semilogx(freqs, psd)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('PSD')
    plt.title('Frequency-Domain EEG Signal')
    plt.show()
    
