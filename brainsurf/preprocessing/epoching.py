import numpy as np
from typing import List, Tuple

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


def create_epochs(signal: List[float], events: List[Tuple[int, int]]) -> List[List[float]]:
    """Create epochs from a raw EEG signal.

    Args:
        signal (List[float]): The raw EEG signal.
        events (List[Tuple[int, int]]): The events indicating the start and end of each epoch.

    Returns:
        List[List[float]]: The list of epochs.
    """
    epochs = []
    for event in events:
        start_idx, end_idx = event
        epoch = signal[start_idx:end_idx]
        epochs.append(epoch)
    return epochs
