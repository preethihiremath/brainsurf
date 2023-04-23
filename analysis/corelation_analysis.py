import pandas as pd
from scipy.stats import pearsonr, spearmanr

def calculate_correlation(data, method='pearson'):
    """
    Calculate pairwise correlation between EEG signals using Pearson's correlation coefficient
    or Spearman's rank correlation coefficient.
    
    Args:
        data (str): Path to CSV file containing the EEG data.
        method (str): Correlation method to use. Can be 'pearson' (default) or 'spearman'.
    
    Returns:
        correlations (pd.DataFrame): A pandas dataframe containing the pairwise correlation coefficients between EEG signals.
    """
    # Load the data from CSV file into a pandas dataframe
    df = pd.read_csv(data)
    
    # Select the EEG signal columns
    eeg_signals = df.iloc[:, 1:].values
    
    # Calculate the correlation matrix using the specified method
    if method == 'pearson':
        corr_matrix = pearsonr(eeg_signals.T)
    elif method == 'spearman':
        corr_matrix = spearmanr(eeg_signals.T)
    else:
        raise ValueError("Invalid correlation method. Must be 'pearson' or 'spearman'.")
    
    # Convert the correlation matrix into a pandas dataframe
    correlations = pd.DataFrame(corr_matrix[0], columns=df.columns[1:], index=df.columns[1:])
    
    return correlations

# def pairwise_corr(data_file, method='pearson'):
#     """
#     Calculates pairwise correlation between the EEG signal using Pearson's correlation coefficient or Spearman's rank
#     correlation coefficient.

#     Args:
#         data_file (str): The path to the CSV file containing the EEG data.
#         method (str): The correlation coefficient to use. Default is 'pearson'. Other options are 'spearman'.

#     Returns:
#         corr_matrix (numpy.ndarray): The correlation matrix.
#     """
#     data = pd.read_csv(data_file)
#     eeg_data = data.loc[:, 'EEG':]

#     if method == 'pearson':
#         corr_matrix = np.corrcoef(eeg_data, rowvar=False)
#     elif method == 'spearman':
#         corr_matrix = np.corrcoef(eeg_data, rowvar=False, ddof=1)
#     else:
#         raise ValueError("Invalid correlation method. Choose 'pearson' or 'spearman'.")

#     return corr_matrix

# # corr_matrix = pairwise_corr('eeg_data.csv', method='pearson')
# # print(corr_matrix)