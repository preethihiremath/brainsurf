import pandas as pd

def read_xlsx_eeg(file_path):
    """
    Read EEG data from an XLSX file using Pandas.

    Parameters:
    ----------
    file_path : str
        Path to the XLSX file containing EEG data.

    Returns:
    -------
    eeg_data : pandas.DataFrame
        DataFrame containing the EEG data.
    """
    eeg_data = pd.read_excel(file_path)
    return eeg_data
