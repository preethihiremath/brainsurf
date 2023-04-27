# import numpy as np
# import pywt
# from scipy.signal import butter, filtfilt
# from scipy.signal import hilbert, hilbert2
# from pyhht.visualization import plot_imfs

# def get_frequency_bands_fourier(eeg_data, fs):
#     # Calculate Fourier transform
#     freqs = np.fft.fftfreq(len(eeg_data), 1/fs)
#     fft = np.fft.fft(eeg_data)
#     power = np.abs(fft)**2
    
#     # Define frequency bands
#     bands = {'delta': (0.5, 4),
#              'theta': (4, 8),
#              'alpha': (8, 13),
#              'beta': (13, 30),
#              'gamma': (30, 100)}
    
#     # Calculate band powers
#     band_powers = {}
#     for band in bands:
#         freq_range = np.logical_and(freqs >= bands[band][0], freqs <= bands[band][1])
#         band_powers[band] = np.sum(power[freq_range])
    
#     return band_powers

# def get_frequency_bands_wavelet(eeg_data, fs):
#     # Define wavelet family and parameters
#     wavelet = 'morl'
#     scales = np.arange(1, 201)
    
#     # Calculate wavelet transform
#     [coefficients, frequencies] = pywt.cwt(eeg_data, scales, wavelet, 1/fs)
#     power = (np.abs(coefficients))**2
    
#     # Define frequency bands
#     bands = {'delta': (0.5, 4),
#              'theta': (4, 8),
#              'alpha': (8, 13),
#              'beta': (13, 30),
#              'gamma': (30, 100)}
    
#     # Calculate band powers
#     band_powers = {}
#     for band in bands:
#         freq_range = np.logical_and(frequencies >= bands[band][0], frequencies <= bands[band][1])
#         band_powers[band] = np.sum(power[:,freq_range], axis=1)
    
#     return band_powers

# def get_frequency_bands_hilbert(eeg_data, fs):
#     # Apply Hilbert transform
#     analytic_signal = hilbert(eeg_data)
    
#     # Define frequency bands
#     bands = {'delta': (0.5, 4),
#              'theta': (4, 8),
#              'alpha': (8, 13),
#              'beta': (13, 30),
#              'gamma': (30, 100)}
    
#     # Calculate band powers
#     band_powers = {}
#     for band in bands:
#         freq_range = np.logical_and(frequencies >= bands[band][0], frequencies <= bands[band][1])
#         band_powers[band] = np.sum(np.abs(analytic_signal[freq_range])**2)
    
#     return band_powers

# def get_frequency_bands_adaptive(eeg_data, fs):
#     # Define filter parameters
#     f_cutoff = [1, 40]
#     n_order = 4
    
#     # Apply adaptive filter
#     b, a = butter(n_order, f_cutoff, btype='bandpass', fs=fs)
#     filtered_data = filtfilt(b, a, eeg_data)
    
#     # Define frequency bands
#     bands = {'delta': (0.5, 4),
#              'theta': (4, 8),
#              'alpha': (8, 13),
#              'beta': (13, 30),
#              'gamma': (30, 100)}
    
#     #


# import numpy as np

# def fourier_transform(data, sampling_rate):
#     fft_vals = np.fft.fft(data)
#     freqs = np.fft.fftfreq(len(data)) * sampling_rate
#     return fft_vals, freqs

# import pywt

# def wavelet_transform(data, wavelet='db4', level=6):
#     coeffs = pywt.wavedec(data, wavelet, level=level)
#     return coeffs

# from PyEMD import EMD, EEMD

# def hilbert_huang_transform(data):
#     # Decompose signal into intrinsic mode functions (IMFs)
#     emd = EMD()
#     imfs = emd(data)
#     # Calculate Hilbert transform of each IMF
#     hilbert_imfs = [np.abs(hilbert(imf)) for imf in imfs]
#     return hilbert_imfs

# from scipy.signal import savgol_filter

# def adaptive_filter(data, window_length=51, polyorder=3):
#     filtered_data = savgol_filter(data, window_length, polyorder)
#     return filtered_data

