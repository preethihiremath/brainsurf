import pandas as pd
import numpy as np
from scipy.stats import pearsonr, spearmanr
from scipy.signal import correlate
import numpy as np
from sklearn.metrics import mutual_info_score

def calculate_correlation(data, method='pearson'):
    if method == 'pearson':
        corr_matrix = pearsonr(data)
    elif method == 'spearman':
        corr_matrix = spearmanr(data)
    else:
        raise ValueError("Invalid correlation method. Must be 'pearson' or 'spearman'.")
    correlations = pd.DataFrame(corr_matrix[0], columns=data.columns[1:], index=data.columns[1:]) 
    return correlations


def calculate_cross_correlation(data1, data2):
    xcorr = correlate(data1, data2)
    lags = np.arange(-len(data1) + 1, len(data1))
    return xcorr, lags

def calculate_phase_sync(data1, data2):
    phase_diff = np.angle(np.exp(1j * (np.angle(np.fft.fft(data1)) - np.angle(np.fft.fft(data2)))))
    return np.abs(np.mean(np.exp(1j * phase_diff)))


def calculate_mutual_information(x, y):
    mi = mutual_info_score(x, y)
    return mi
