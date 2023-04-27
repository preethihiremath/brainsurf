import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def plot_power_spectrum_fft(data, sfreq):
    """
    Compute and plot the power spectrum of EEG data.
    
    Parameters
    ----------
    data : array-like, shape (n_channels, n_samples)
        The EEG data.
    sfreq : float
        The sampling frequency of the data, in Hz.
    """
    n_channels, n_samples = data.shape
  
    freqs = np.fft.rfftfreq(n_samples, 1/sfreq)

    psd = np.abs(np.fft.rfft(data, axis=1))**2 / (n_samples * sfreq)
    
    fig, ax = plt.subplots()
    for i in range(n_channels):
        ax.plot(freqs, psd[i], label=f'Channel {i+1}')
    ax.set_xlabel('Frequency (Hz)')
    ax.set_ylabel('Power ($\mu V^2$/Hz)')
    ax.legend()
    plt.show()


def welch_power_spectrum(freqs, psd, nperseg=1024):
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
    # eeg=data.iloc[:, 1]
    # freqs, psd = signal.welch(eeg, sfreq, nperseg=nperseg)
    plt.figure()
    plt.plot(freqs, psd)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('PSD')
    plt.title('Frequency-Domain EEG Signal')
    plt.show()
    

