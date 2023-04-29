import pandas as pd

def read_csv_eeg(file_path):
    print("the file path is")
    print(file_path)
    eeg_data = pd.read_csv(file_path)
    return eeg_data
