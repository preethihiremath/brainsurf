import pandas as pd
from .eeg_data import EEGDataFactory

def convert_csv_to_eeg_data(file_path):
    factory = EEGDataFactory()
    eeg_data = factory.create_eeg_data(file_path)
    return eeg_data
