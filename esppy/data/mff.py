from mne.io import read_raw

def read_mff(file_path):
    raw =  read_raw(file_path)
    return raw.get_data()
