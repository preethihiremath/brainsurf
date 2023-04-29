import numpy as np
from scipy.signal import morlet2

def compute_time_frequency(data, sfreq, freqs, method='morlet', n_cycles=7):
    n_samples = len(data)
    time_bandwidth = 2 * n_cycles
    power = np.zeros((len(freqs), n_samples))
    for i, freq in enumerate(freqs):
        w = 2 * np.pi * freq
        wavelet = morlet2(n_samples, w, time_bandwidth)
        convolved = np.convolve(data, wavelet, mode='same')
        power[i, :] = np.abs(convolved)**2

    return power
