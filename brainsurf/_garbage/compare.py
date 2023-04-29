import numpy as np
import pandas as pd

def compare_eeg(csv_files):
    """
    Compares EEG signals between CSV files containing EEG signals of 5 people during mantra meditation
    
    Parameters:
    csv_files (list): A list of CSV file names
    
    Returns:
    eeg_comparison (DataFrame): A DataFrame containing EEG signal comparisons between each pair of people
    """
    
    # Load data from CSV files
    data = []
    for file in csv_files:
        df = pd.read_csv(file)
        data.append(df.values)
    
    # Create empty DataFrame to store comparisons
    eeg_comparison = pd.DataFrame(index=["Person {}".format(i+1) for i in range(len(data))], 
                                  columns=["Person {}".format(i+1) for i in range(len(data))])
    
    # Compare each pair of people
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            person_i = data[i]
            person_j = data[j]
            
            # Calculate correlation between the two people's EEG signals
            correlation = np.corrcoef(person_i, person_j)[0][1]
            
            # Store result in DataFrame
            eeg_comparison.iloc[i, j] = correlation
            eeg_comparison.iloc[j, i] = correlation
    
    return eeg_comparison


# This function takes a list of CSV files containing EEG signals of 5 people during mantra meditation, loads the data from each file into a list, and then compares each pair of people by calculating the correlation between their EEG signals. The results are stored in a DataFrame and returned. Note that this function assumes that the CSV files have the same format, with the same number of channels and the same sampling rate. If this is not the case, additional data preprocessing may be necessary.