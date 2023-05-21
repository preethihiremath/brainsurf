import numpy as np
import pandas as pd
from scipy import signal

import nolds

def calculate_mean(data):
    return np.nanmean(data)

def calculate_variance(data):
    return np.nanvar(data)

import numpy as np

def calculate_skewness(data):
    """
    Calculates skewness of given data.

    Parameters:
    data (ndarray): 1-D or 2-D array of data.

    Returns:
    float: Skewness value of the data.
    """
    if data.ndim == 1:
        mean = np.nanmean(data)
        std = np.nanstd(data)
        skewness = np.nanmean((data - mean) ** 3) / std ** 3
    elif data.ndim == 2:
        mean = np.nanmean(data, axis=1)
        std = np.nanstd(data, axis=1)
        skewness = np.nanmean(((data - mean[:, np.newaxis]) ** 3), axis=1) / (std ** 3)
    else:
        raise ValueError('Data must be 1-D or 2-D array.')
    return skewness


def calculate_kurtosis(data):
    """
    Calculates kurtosis of given data.

    Parameters:
    data (ndarray): 1-D or 2-D array of data.

    Returns:
    float: Kurtosis value of the data.
    """
    if data.ndim == 1:
        mean = np.nanmean(data)
        std = np.nanstd(data)
        kurtosis = np.nanmean((data - mean) ** 4) / std ** 4
    elif data.ndim == 2:
        mean = np.nanmean(data, axis=1)
        std = np.nanstd(data, axis=1)
        kurtosis = np.nanmean(((data - mean[:, np.newaxis]) ** 4), axis=1) / (std ** 4)
    else:
        raise ValueError('Data must be 1-D or 2-D array.')
    return kurtosis


def calculate_coherence(data1, data2, fs):
    freqs, psd_data1 = signal.welch(data1, fs=fs, nperseg=1024)
    freqs, psd_data2 = signal.welch(data2, fs=fs, nperseg=1024)
    freqs, csd = signal.csd(data1, data2, fs=fs, nperseg=1024)
    coh = np.abs(csd)**2 / (psd_data1 * psd_data2)
    return freqs, coh


def calculate_max(data):
    return np.max(data, axis=1)

def calculate_min(data):
    return np.min(data, axis=1)

def calculate_relative_power(freqs, psd):
    delta_mask = (freqs >= 0.5) & (freqs <= 4)
    theta_mask = (freqs >= 4) & (freqs <= 8)
    alpha_mask = (freqs >= 8) & (freqs <= 13)
    beta_mask = (freqs >= 13) & (freqs <= 30)

    delta_power = np.trapz(psd[delta_mask], freqs[delta_mask])
    theta_power = np.trapz(psd[theta_mask], freqs[theta_mask])
    alpha_power = np.trapz(psd[alpha_mask], freqs[alpha_mask])
    beta_power = np.trapz(psd[beta_mask], freqs[beta_mask])

    total_power = delta_power + theta_power + alpha_power + beta_power

    delta_power=delta_power / total_power
    theta_power=theta_power / total_power
    alpha_power=alpha_power / total_power
    beta_power=beta_power / total_power
    return {
        "delta": delta_power / total_power,
        "theta": theta_power / total_power,
        "alpha": alpha_power / total_power,
        "beta": beta_power / total_power
    }

def calc_ap_entropy(data, m=2, r=0.2):
    ae = nolds.sampen(data, emb_dim=m, tolerance=r)
    return ae

def calc_fractal_dimension(data):
    fd = nolds.dfa(data)
    return fd
