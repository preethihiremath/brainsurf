import pandas as pd

def read_csv_eeg(file_path):
    eeg_data = pd.read_csv(file_path)
    return eeg_data
