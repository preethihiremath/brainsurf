import os
import pandas as pd
import mne

def read_csv_file(filename):
    """Read a CSV file and return an MNE Raw object."""
    data = pd.read_csv(filename)
    ch_names = data.columns[1:]
    ch_types = ['eeg'] * len(ch_names)
    info = mne.create_info(ch_names=ch_names, sfreq=1000, ch_types=ch_types)
    raw = mne.io.RawArray(data[ch_names].T, info)
    return raw

def read_xlsx_file(filename):
    """Read an XLSX file and return an MNE Raw object."""
    data = pd.read_excel(filename)
    ch_names = data.columns[1:]
    ch_types = ['eeg'] * len(ch_names)
    info = mne.create_info(ch_names=ch_names, sfreq=1000, ch_types=ch_types)
    raw = mne.io.RawArray(data[ch_names].T, info)
    return raw

def read_eeg_data():
    """Read all EEG data files in the EEGDATA directory and return a list of MNE Raw objects."""
    eeg_dir = "EEGDATA"
    raw_objects = []
    for filename in os.listdir(eeg_dir):
        if filename.endswith(".csv"):
            raw_objects.append(read_csv_file(os.path.join(eeg_dir, filename)))
        elif filename.endswith(".xlsx"):
            raw_objects.append(read_xlsx_file(os.path.join(eeg_dir, filename)))
    return raw_objects
