import numpy as np
from scipy.signal import morlet2

def compute_time_frequency(data, sfreq, freqs, method='morlet', n_cycles=7):
    """On the other hand, time-frequency analysis aims to analyze how the power
      of a signal changes over time and across different frequency components. 
      It provides a more detailed representation of the signal by capturing both temporal and spectral information. 
      Time-frequency analysis is commonly performed using methods like the Continuous Wavelet Transform (CWT), 
    Short-Time Fourier Transform (STFT), or the Stockwell Transform."""
    n_samples = len(data)
    time_bandwidth = 2 * n_cycles
    power = np.zeros((len(freqs), n_samples))
    for i, freq in enumerate(freqs):
        w = 2 * np.pi * freq
        wavelet = morlet2(n_samples, w, time_bandwidth)
        convolved = np.convolve(data, wavelet, mode='same')
        power[i, :] = np.abs(convolved)**2

    return power
