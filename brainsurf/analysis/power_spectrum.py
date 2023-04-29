import numpy as np
from scipy.signal import welch, coherence, correlate
import astropy as ast 
from scipy.signal import periodogram , multitaper

def psd_fft(data, sfreq, freq_range=(0, 100)):
    n_freqs = int(sfreq/2) + 1
    fft_data = np.fft.rfft(data)
    power_spectrum = np.abs(fft_data)**2 / len(data)
    freqs = np.fft.rfftfreq(len(data), 1.0/sfreq)
    mask = (freqs >= freq_range[0]) & (freqs <= freq_range[1])
    freqs = freqs[mask]
    power_spectrum = power_spectrum[mask]
    return freqs, power_spectrum

def psd_welch(data, fs):
    nperseg= calculate_nperseg(data)
    freqs, psd = welch(data, fs=fs, nperseg=10)
    print(freqs)
    return freqs, psd

def psd_lombscargle(signal, fs):
    time = np.arange(len(signal))/fs
    frequency, power = ast.timeseries.LombScargle(time, signal).autopower(normalization='psd')
    return frequency, power

def psd_multitaper(signal, fs, nperseg=256, NW=3):
    f, Pxx = multitaper(signal, fs, nperseg=nperseg, NW=NW, adaptive=True)
    return f, Pxx.mean(axis=1)

def psd_periodogram(signal, fs, nfft=None):
    f, Pxx = periodogram(signal, fs, nfft=nfft)
    return f, Pxx

def calculate_nperseg(data):
    n = len(data)
    if n < 256:
        nperseg = n
    elif n < 2048:
        nperseg = 256
    else:
        nperseg = 1024
    return nperseg