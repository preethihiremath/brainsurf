import pandas as pd
import os
import numpy as np



# Define paths to input and output directories
data_dir = 'data'
results_dir = 'results'


# Data handling and file I/O functions

def read_csv_file(filename):
    """Reads a CSV file and returns a pandas DataFrame."""
    filepath = os.path.join(data_dir, filename)
    return pd.read_csv(filepath)

def save_csv_file(df, filename):
    """Saves a pandas DataFrame to a CSV file."""
    filepath = os.path.join(results_dir, filename)
    df.to_csv(filepath, index=False)


# Data manipulation functions

def resample_data(data, orig_fs, new_fs):
    """Resamples data from original sampling rate to new sampling rate."""
    orig_dt = 1 / orig_fs
    new_dt = 1 / new_fs
    orig_time = np.arange(0, len(data)) * orig_dt
    new_time = np.arange(0, orig_time[-1], new_dt)
    return np.interp(new_time, orig_time, data)

def segment_data(data, seg_len, overlap):
    """Segments data into segments of length seg_len with specified overlap."""
    step = seg_len - overlap
    n_segs = int(np.ceil((len(data) - seg_len) / step) + 1)
    segments = np.zeros((n_segs, seg_len))
    for i in range(n_segs):
        start = i * step
        end = start + seg_len
        if end > len(data):
            segment = np.zeros((seg_len,))
            segment[:len(data)-start] = data[start:]
        else:
            segment = data[start:end]
        segments[i,:] = segment
    return segments

    
def get_columns(dataset, columns):
    """
    Get specific columns from the dataset.
    
    Parameters:
    -----------
    dataset : str or pandas.DataFrame
        The dataset to extract columns from. It can be either a path to a CSV file or a pandas DataFrame.
    columns : list
        A list of column names to extract from the dataset.
        
    Returns:
    --------
    pandas.DataFrame
        A DataFrame with the selected columns.
    """
    if isinstance(dataset, str):
        # If dataset is a string, assume it's a path to a CSV file
        df = pd.read_csv(dataset)
    elif isinstance(dataset, pd.DataFrame):
        # If dataset is a DataFrame, use it directly
        df = dataset
    else:
        #Update to handle more types directly
        raise TypeError("dataset must be either a path to a CSV file or a pandas DataFrame.")
    
    # Check if all columns are in the dataset
    for col in columns:
        if col not in df.columns:
            raise ValueError(f"Column '{col}' not found in the dataset.")
    return df[columns]
    
def estimate_sampling_frequency(timestamps):
    """
    Estimates the sampling frequency of an EEG signal dataset based on the time stamps of the data points.

    Parameters:
    ----------
    timestamps : array-like
        Array of time stamps (in seconds) for each data point in the EEG signal dataset.

    Returns:
    -------
    sampling_frequency : float
        Estimated sampling frequency of the EEG signal dataset.
    """
    time_diff = np.diff(timestamps)
    median_time_diff = np.median(time_diff)
    sampling_frequency = 1 / median_time_diff
    return sampling_frequency