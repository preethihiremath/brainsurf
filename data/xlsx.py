import pandas as pd

def read_xlsx_eeg(file_path):
    eeg_data = pd.read_excel(file_path)
    return eeg_data
