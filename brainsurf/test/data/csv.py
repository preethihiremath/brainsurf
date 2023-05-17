import pandas as pd
from ...csv import read_csv_eeg




eeg_data= read_csv_eeg('./data/samples/anirudh/ani_med.csv')
print(eeg_data.head())  
print(eeg_data['EEG'])