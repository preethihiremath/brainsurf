import numpy as np
from scipy.signal import butter, lfilter, iirnotch

def butter_bandpass_filter(data, lowcut, highcut, fs, order):
    """
    Apply a Butterworth band-pass filter to the input data.

    Parameters:
        data (array-like): Input data to be filtered.
        lowcut (float): Lower cut-off frequency of the filter.
        highcut (float): Upper cut-off frequency of the filter.
        fs (float): Sampling frequency of the data.
        order (int): Order of the Butterworth filter.

    Returns:
        array-like: Filtered data.

    """
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    y = lfilter(b, a, data)
    return y

def notch_filter(data, fs, freqs, q):
    """
    Apply an IIR notch filter to remove specific frequencies from the input data.

    Parameters:
        data (array-like): Input data to be filtered.
        fs (float): Sampling frequency of the data.
        freqs (float or array-like): Frequency or frequencies to be removed.
        q (float): Quality factor of the notch filter.

    Returns:
        array-like: Filtered data.

    """
    b, a = iirnotch(freqs, q, fs)
    y = lfilter(b, a, data)
    return y

def lowpass_filter(data, cutoff_freq, fs, order):
    """
    Apply a low-pass filter to the input data.

    Parameters:
        data (array-like): Input data to be filtered.
        cutoff_freq (float): Cut-off frequency of the filter.
        fs (float): Sampling frequency of the data.
        order (int): Order of the Butterworth filter.

    Returns:
        array-like: Filtered data.

    """
    nyq = 0.5 * fs
    cutoff = cutoff_freq / nyq
    b, a = butter(order, cutoff, btype='low')
    y = lfilter(b, a, data)
    return y

def highpass_filter(data, cutoff_freq, fs, order):
    """
    Apply a high-pass filter to the input data.

    Parameters:
        data (array-like): Input data to be filtered.
        cutoff_freq (float): Cut-off frequency of the filter.
        fs (float): Sampling frequency of the data.
        order (int): Order of the Butterworth filter.

    Returns:
        array-like: Filtered data.

    """
    nyq = 0.5 * fs
    cutoff = cutoff_freq / nyq
    b, a = butter(order, cutoff, btype='high')
    y = lfilter(b, a, data)
    return y

def comb_filter(data, delay, gain):
    """
    Apply a comb filter to the input data.

    Parameters:
        data (array-like): Input data to be filtered.
        delay (int): Delay value for the comb filter.
        gain (float): Gain value for the comb filter.

    Returns:
        array-like: Filtered data.

    """
    y = np.zeros_like(data)
    for i in range(delay, len(data)):
        y[i] = data[i] + gain * data[i - delay]
    return y

def adaptive_filter(data, reference, order):
    """
    Apply an adaptive filter to the input data.

    Parameters:
        data (array-like): Input data to be filtered.
        reference (array-like): Reference data for the adaptive filter.
        order (int): Order of the adaptive filter.

    Returns:
        array-like: Filtered data.

    """
    y = np.zeros_like(data)
    w = np.zeros(order)
    for i in range(order, len(data)):
        x = data[i-order:i][::-1]
        y[i] = np.dot(w, x)
        e = reference[i] - y[i]
        w += 0.01 * e * x
    return y

def kalman_filter(data, measurement_noise, process_noise):
    """
    Apply a Kalman filter to the input data.

    Parameters:
        data (array-like): Input data to be filtered.
        measurement_noise (float): Measurement noise covariance.
        process_noise (float): Process noise covariance.

    Returns:
        array-like: Filtered data.

    """
    n = len(data)
    x = np.zeros(n)
    P = np.zeros(n)
    x[0] = data[0]
    P[0] = measurement_noise
    for i in range(1, n):
        x_priori = x[i-1]
        P_priori = P[i-1] + process_noise
        K = P_priori / (P_priori + measurement_noise)
        x[i] = x_priori + K * (data[i] - x_priori)
        P[i] = (1 - K) * P_priori
    return x
