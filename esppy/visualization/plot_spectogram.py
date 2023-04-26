import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import spectrogram


def plot_spectrogram(data, fs, window='hann',nperseg=256, noverlap=None, cmap='RdBu_r', show=True,scaling='density',):
    """
    Plot a spectrogram of EEG/MEG data.

    Parameters
    ----------
    data : array, shape (n_channels, n_samples)
        The data values to be plotted.
    sfreq : float
        The sampling frequency of the data.
    nperseg : int
        The number of samples per segment.
    noverlap : int | None
        The number of samples to overlap between segments. If None,
        noverlap=nperseg//2 is used.
    cmap : str
        The name of the colormap to use.
    show : bool
        Whether to show the plot.

    Returns
    -------
    fig : matplotlib.figure.Figure
        The figure object.
    ax : matplotlib.axes.Axes
        The axis object.
    """
    # compute spectrogram
    f, t, Sxx = spectrogram(data, fs=fs, window=window, nperseg=nperseg, noverlap=noverlap, scaling=scaling)

    # Plot the spectrogram
    plt.pcolormesh(t, f, Sxx, cmap=cmap)
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [sec]')
    plt.colorbar()
    plt.show()