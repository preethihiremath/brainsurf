import numpy as np
import pandas as pd
from scipy import signal
from scipy.signal import welch, coherence, correlate
import nolds


def calculate_mean(data):
    """
    Calculates the mean of the input data.

    Parameters
    ----------
    data : numpy.ndarray
        The input data.

    Returns
    -------
    float
        The mean of the input data.
    """
    return np.mean(data)

def calculate_variance(data):
    """
    Calculates the variance of the input data.

    Parameters
    ----------
    data : numpy.ndarray
        The input data.

    Returns
    -------
    float
        The variance of the input data.
    """
    return np.var(data)

def calculate_spectral_power(data, fs):
    """
    Calculates the power spectral density of the input data.

    Parameters
    ----------
    data : numpy.ndarray
        The input data.
    fs : float
        The sampling frequency of the data.

    Returns
    -------
    freqs : numpy.ndarray
        The frequencies.
    psd : numpy.ndarray
        The power spectral density.
    """
    freqs, psd = welch(data, fs=fs, nperseg=1024)
    return freqs, psd


def calculate_coherence(data1, data2, fs):
    """
    Calculates the coherence between two sets of data.

    Coherence is a measure of the linear dependence between two signals as a function of frequency. It is a value between 0 and 1, 
    where 1 represents perfect coherence (i.e., the two signals are perfectly synchronized) and 0 represents no coherence (i.e., the two signals are completely unrelated).
    Parameters:
        data1 (array): The first set of data.
        data2 (array): The second set of data.
        fs (int): The sampling rate of the data.

    Returns:
        freqs (array): The frequencies at which the coherence was calculated.
        coh (array): The coherence between the two sets of data.
    """
    # Calculate the power spectral density of the two data sets
    freqs, psd_data1 = signal.welch(data1, fs=fs, nperseg=1024)
    freqs, psd_data2 = signal.welch(data2, fs=fs, nperseg=1024)

    # Calculate the cross-spectral density of the two data sets
    freqs, csd = signal.csd(data1, data2, fs=fs, nperseg=1024)

    # Calculate the coherence between the two data sets
    coh = np.abs(csd)**2 / (psd_data1 * psd_data2)

    return freqs, coh


def calculate_cross_correlation(data1, data2):
    """
    Calculates the cross-correlation between two sets of data.

    Parameters
    ----------
    data1 : numpy.ndarray
        The first set of data.
    data2 : numpy.ndarray
        The second set of data.

    Returns
    -------
    xcorr : numpy.ndarray
        The cross-correlation between the two sets of data.
    lags : numpy.ndarray
        The lag values.
    """

    xcorr = correlate(data1, data2)
    lags = np.arange(-len(data1) + 1, len(data1))
    return xcorr, lags


def calculate_max(data):
    """
    Compute the maximum value of the EEG data

    Parameters
    ----------
    data : array-like, shape (n_channels, n_samples)
        The EEG data.

    Returns
    -------
    max : array-like, shape (n_channels,)
        The maximum value of the EEG data for each channel.
    """
    return np.max(data, axis=1)

def calculate_min(data):
    """
    Compute the minimum value of the EEG data

    Parameters
    ----------
    data : array-like, shape (n_channels, n_samples)
        The EEG data.

    Returns
    -------
    min : array-like, shape (n_channels,)
        The minimum value of the EEG data for each channel.
    """
    return np.min(data, axis=1)

def calculate_phase_sync(data1, data2):
    """Calculate the phase synchronization between two EEG datasets."""
    phase_diff = np.angle(np.exp(1j * (np.angle(np.fft.fft(data1)) - np.angle(np.fft.fft(data2)))))
    return np.abs(np.mean(np.exp(1j * phase_diff)))


def calculate_relative_power(freqs, psd):
    """Calculate the relative power of the alpha, beta, delta, and theta frequency bands."""
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

    # return delta_power,theta_power,alpha_power,beta_power;
    return {
        "delta": delta_power / total_power,
        "theta": theta_power / total_power,
        "alpha": alpha_power / total_power,
        "beta": beta_power / total_power
    }



def calc_ap_entropy(data, m=2, r=0.2):
    """
    Calculates the approximate entropy of a given dataset.

    Parameters
    ----------
    data : numpy.ndarray
        The input data.
    m : int, optional
        The embedding dimension (default is 2).
    r : float, optional
        The tolerance value (default is 0.2).

    Returns
    -------
    ae : float
        The approximate entropy of the input data.
    """
    ae = nolds.sampen(data, emb_dim=m, tolerance=r)
    return ae

def calc_fractal_dimension(data):
    """
    Calculates the fractal dimension of a given dataset.

    Parameters
    ----------
    data : numpy.ndarray
        The input data.

    Returns
    -------
    fd : float
        The fractal dimension of the input data.
    """
    fd = nolds.dfa(data)
    return fd
