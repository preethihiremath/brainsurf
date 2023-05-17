import pandas as pd
import os
import numpy as np

    
def get_columns(dataset, columns):
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

    time_diff = np.diff(timestamps)  # Calculate the time difference between consecutive samples
    sampling_freq = 1 / np.nanmean(time_diff) 
    return sampling_freq