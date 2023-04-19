import pandas as pd

def read_csv_eeg(file_path):
    """
    Read EEG data from a CSV file using Pandas.

    Parameters:
    ----------
    file_path : str
        Path to the CSV file containing EEG data.

    Returns:
    -------
    eeg_data : pandas.DataFrame
        DataFrame containing the EEG data.
    """
    eeg_data = pd.read_csv(file_path)
    return eeg_data
