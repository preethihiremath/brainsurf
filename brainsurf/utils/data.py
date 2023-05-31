import numpy as np
def estimate_sampling_frequency(timestamps):
    time_diff = np.diff(timestamps)  # Calculate the time difference between consecutive samples
    sampling_freq = 1 / np.nanmean(time_diff) 
    return sampling_freq