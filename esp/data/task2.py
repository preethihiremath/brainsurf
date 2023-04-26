import numpy as np
from scipy import signal

class EEGObject:
    def __init__(self, data, sample_rate, channels):
        self.data = data
        self.sample_rate = sample_rate
        self.channels = channels
        self.filter_type = None
        self.filter_params = None

    def apply_filter(self, filter_type, **kwargs):
        if filter_type == 'butterworth':
            self.filter_type = filter_type
            self.filter_params = kwargs
            order = kwargs.get('order', 5)
            cutoff = kwargs.get('cutoff', [0.5, 40])
            b, a = signal.butter(order, np.array(cutoff)/(self.sample_rate/2), btype='bandpass')
            self.data = signal.filtfilt(b, a, self.data, axis=0)
        elif filter_type == 'notch':
            self.filter_type = filter_type
            self.filter_params = kwargs
            freq = kwargs.get('freq', 60)
            Q = kwargs.get('Q', 30)
            b, a = signal.iirnotch(freq/(self.sample_rate/2), Q)
            self.data = signal.filtfilt(b, a, self.data, axis=0)
        else:
            print('Invalid filter type.')

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_sample_rate(self):
        return self.sample_rate

    def set_sample_rate(self, sample_rate):
        self.sample_rate = sample_rate

    def get_channels(self):
        return self.channels

    def set_channels(self, channels):
        self.channels = channels

    def get_filter_type(self):
        return self.filter_type

    def set_filter_type(self, filter_type):
        self.filter_type = filter_type

    def get_filter_params(self):
        return self.filter_params

    def set_filter_params(self, filter_params):
        self.filter_params = filter_params


# import mne

# class EEGObject:
#     def __init__(self, data, ch_names, ch_types, sfreq, info=None):
#         self.data = data
#         self.ch_names = ch_names
#         self.ch_types = ch_types
#         self.sfreq = sfreq
#         self.info = info
#         self.filter_type = None
#         self.filter_params = None
#         self.preprocessed_data = None
#         self.epochs = None

#     def apply_filter(self, filter_type, filter_params):
#         # Apply filter to the data and store the preprocessed data
#         # Update filter_type and filter_params variables

#     def apply_epochs(self, events, event_id, tmin, tmax, baseline=None):
#         # Segment the preprocessed data into epochs
#         # Create an MNE Epochs object and store it in the epochs variable

#     def plot_psd(self):
#         # Plot the power spectral density of the preprocessed data

#     def plot_epochs(self):
#         # Plot the epochs of the preprocessed data

#     # Other methods for artifact removal, feature extraction, etc.
