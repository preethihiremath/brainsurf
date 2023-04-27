import numpy as np
from scipy.signal import butter, lfilter, iirnotch

def butter_bandpass_filter(data, lowcut, highcut, fs, order):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    y = lfilter(b, a, data)
    return y

def notch_filter(data, fs, freqs, q):
    # to remove a narrow band of frequencies from a signal.
    # The higher the q, the narrower the band of frequencies that will be filtered.
    b, a = iirnotch(freqs, q, fs)
    y = lfilter(b, a, data)
    return y

