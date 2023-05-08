import numpy as np

def epoching(eeg_data, sfreq, event_times, tmin=-0.5, tmax=0.5):
    n_channels, n_samples = eeg_data.shape
    n_samples_per_epoch = int((tmax - tmin) * sfreq)
    n_events = len(event_times)
    epochs = np.zeros((n_events, n_channels, n_samples_per_epoch))
    for i, event_time in enumerate(event_times):
        start_time = int((event_time + tmin) * sfreq)
        end_time = start_time + n_samples_per_epoch
        if end_time <= n_samples:
            epochs[i] = eeg_data[:, start_time:end_time]

    return epochs
