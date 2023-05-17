from mne.io import read_raw
from .eeg_data import EEGDataFactory

def convert_mff_to_eegdata(file_path):
    factory = EEGDataFactory()
    eeg_data = factory.create_eeg_data(file_path)
    return eeg_data

# import os

# folder_path = '/path/to/folder/P1.mff'  # Replace with the actual path to the folder containing the files

# # Initialize EEGDataFactory
# factory = EEGDataFactory()

# # Extract relevant file paths
# info_xml_path = os.path.join(folder_path, 'info.xml')
# signal_bin_path = os.path.join(folder_path, 'signal1.bin')
# channel_layout_xml_path = os.path.join(folder_path, 'sensorLayout.xml')

# # Create EEGData from the files
# eeg_data = factory.create_eeg_data(info_xml_path)
# eeg_data.set_data(raw_data=signal_bin_path)
# eeg_data.set_data(channel_layout=channel_layout_xml_path)

# # Access the extracted EEG data
# timestamps = eeg_data.get_data()['timestamps']
# eeg_signals = eeg_data.get_data()['raw_data']
# channel_names = eeg_data.get_data()['channel_layout']

# # Print EEG data summary
# eeg_data.summary(max_len=10)

# # Access individual data fields
# print("Timestamps:", timestamps)
# print("EEG Signals:", eeg_signals)
# print("Channel Names:", channel_names)
