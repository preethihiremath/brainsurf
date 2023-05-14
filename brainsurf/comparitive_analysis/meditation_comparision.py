import numpy as np
from scipy import signal

class EEGComparison:
    def __init__(self, pre_meditation_data, post_meditation_data):
        self.pre_data = pre_meditation_data
        self.post_data = post_meditation_data

    def calculate_power_spectrum(self, data):
        # Calculate power spectrum using Welch's method
        f, Pxx = signal.welch(data, fs=256, nperseg=256*4)
        return f, Pxx

    def extract_features(self):
        # Calculate power spectra for pre and post-meditation data
        pre_f, pre_power_spectrum = self.calculate_power_spectrum(self.pre_data)
        post_f, post_power_spectrum = self.calculate_power_spectrum(self.post_data)
        
        # Calculate mean and standard deviation of power spectrum for pre and post-meditation data
        pre_mean = np.mean(pre_power_spectrum, axis=1)
        pre_std = np.std(pre_power_spectrum, axis=1)

        post_mean = np.mean(post_power_spectrum, axis=1)
        post_std = np.std(post_power_spectrum, axis=1)
  
        # Calculate the difference between pre and post-meditation mean and standard deviation
        mean_diff = post_mean - pre_mean
        std_diff = post_std - pre_std

        # Return the feature vector
        return np.concatenate([mean_diff, std_diff])
    

