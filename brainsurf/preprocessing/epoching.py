import numpy as np

def epoching(eeg_data, sfreq, event_times, tmin=-0.5, tmax=0.5):
    """
    Epochs the EEG data around the given event times, with a specified time window.

    Parameters
    ----------
    eeg_data : numpy array, shape (n_channels, n_samples)
        The EEG data to be epoched.
    sfreq : float
        The sampling frequency of the EEG data, in Hz.
    event_times : numpy array, shape (n_events,)
        The times (in seconds) of the events to epoch around.
    tmin : float
        The start time (in seconds) of the epoch relative to the event time.
        Default is -0.5 seconds.
    tmax : float
        The end time (in seconds) of the epoch relative to the event time.
        Default is 0.5 seconds.

    Returns
    -------
    epochs : numpy array, shape (n_events, n_channels, n_samples_per_epoch)
        The epoched EEG data.
    """
    n_channels, n_samples = eeg_data.shape
    n_samples_per_epoch = int((tmax - tmin) * sfreq)
    n_events = len(event_times)

    # Initialize the array to store the epochs
    epochs = np.zeros((n_events, n_channels, n_samples_per_epoch))

    # Loop through each event time and extract the corresponding epoch
    for i, event_time in enumerate(event_times):
        start_time = int((event_time + tmin) * sfreq)
        end_time = start_time + n_samples_per_epoch
        if end_time <= n_samples:
            epochs[i] = eeg_data[:, start_time:end_time]

    return epochs
