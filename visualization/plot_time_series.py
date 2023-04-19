import matplotlib.pyplot as plt

def plot_time_series(data, sfreq, tmin=0, tmax=None):
    """
    Plot the time series of EEG data.
    
    Parameters
    ----------
    data : array-like, shape (n_channels, n_samples)
        The EEG data.
    sfreq : float
        The sampling frequency of the data, in Hz.
    tmin : float
        The start time of the plot, in seconds (default=0).
    tmax : float or None
        The end time of the plot, in seconds (default=None, which plots to the end of the data).
    """
    n_channels, n_samples = data.shape
    times = np.arange(n_samples) / sfreq
    if tmax is None:
        tmax = times[-1]
    mask = (times >= tmin) & (times <= tmax)
    
    fig, ax = plt.subplots()
    for i in range(n_channels):
        ax.plot(times[mask], data[i, mask], label=f'Channel {i+1}')
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Amplitude ($\mu V$)')
    ax.legend()
    plt.show()
