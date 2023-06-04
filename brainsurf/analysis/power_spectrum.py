import numpy as np
from scipy.signal import welch, coherence, correlate
import astropy as ast 


def extract_frequency_bands(raw_data, fs=128):
    epoch_length = 1000  # Length of each epoch in milliseconds
    num_epochs = len(raw_data) // epoch_length
    pre_epochs = np.split(raw_data[:num_epochs * epoch_length], num_epochs)
    
    # Initialize the dictionary to store the frequency bands
    data = {}
    
    for band in ['alpha', 'beta', 'delta', 'theta', 'gamma']:
        if band not in data:
            pre_features = []
            
            for epoch in pre_epochs:
                f, psd = welch(epoch, fs=fs)
                
                # Adjust the frequency range based on the band
                if band == 'alpha':
                    band_psd = psd[(f >= 8) & (f <= 13)]
                elif band == 'beta':
                    band_psd = psd[(f >= 13) & (f <= 30)]
                elif band == 'delta':
                    band_psd = psd[(f >= 1) & (f <= 4)]
                elif band == 'theta':
                    band_psd = psd[(f >= 4) & (f <= 8)]
                elif band == 'gamma':
                    band_psd = psd[(f >= 30) & (f <= 50)]
                else:
                    raise ValueError("Invalid frequency band.")
                band_power = np.mean(band_psd) if band_psd.any() else np.nan
                pre_features.append(band_power)
            
            # Make sure the extracted features have the same length as the original data
            pre_features += [np.nan] * (len(raw_data) - len(pre_features))
            
            data[band] = pre_features
            
    return data

def psd_fft(data, sfreq, freq_range=(0, 100)):
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

# def psd_multitaper(signal, fs, nperseg=256, NW=3):
#     f, Pxx = multitaper(signal, fs, nperseg=nperseg, NW=NW, adaptive=True)
#     return f, Pxx.mean(axis=1)

# def psd_periodogram(signal, fs, nfft=None):
#     f, Pxx = periodogram(signal, fs, nfft=nfft)
#     return f, Pxx

def calculate_nperseg(data):
    n = len(data)
    if n < 256:
        nperseg = n
    elif n < 2048:
        nperseg = 256
    else:
        nperseg = 1024
    return nperseg