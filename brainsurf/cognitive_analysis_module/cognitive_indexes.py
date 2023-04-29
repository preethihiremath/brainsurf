import numpy as np

def calculate_power(data, fs):
    """
    Calculates the power spectrum of a set of data using Welch's method.

    Parameters
    ----------
    data : numpy.ndarray
        The data to be analyzed.
    fs : float
        The sampling rate of the data.

    Returns
    -------
    freqs : numpy.ndarray
        The frequencies of the power spectrum.
    power : numpy.ndarray
        The power spectrum of the data.
    """

    from scipy.signal import welch

    f, Pxx = welch(data, fs=fs, nperseg=fs*2, noverlap=fs, scaling='density')
    return f, Pxx


def calculate_band_power(freqs, power, bands):
    """
    Calculates the power in specific frequency bands.

    Parameters
    ----------
    freqs : numpy.ndarray
        The frequencies of the power spectrum.
    power : numpy.ndarray
        The power spectrum of the data.
    bands : dict
        A dictionary of frequency band definitions, with keys 'alpha', 'beta', etc.

    Returns
    -------
    band_power : dict
        A dictionary of power values, with keys 'alpha', 'beta', etc.
    """

    band_power = {}
    for band, f_range in bands.items():
        idx = np.logical_and(freqs >= f_range[0], freqs <= f_range[1])
        band_power[band] = np.trapz(power[idx], freqs[idx])

    return band_power


def calculate_pe(band_power):
    """
    Calculates the Performance Enhancement index from the given band power values.

    Parameters
    ----------
    band_power : dict
        A dictionary of power values, with keys 'alpha', 'beta', etc.

    Returns
    -------
    pe : float
        The Performance Enhancement index.
    """

    pe = band_power['beta'] / band_power['alpha']
    return pe


def calculate_arousal_index(band_power):
    """
    Calculates the Arousal Index from the given band power values.

    Parameters
    ----------
    band_power : dict
        A dictionary of power values, with keys 'alpha', 'beta', etc.

    Returns
    -------
    ai : float
        The Arousal Index.
    """

    ai = (band_power['beta'] + band_power['gamma']) / band_power['alpha']
    return ai


def calculate_neural_activity(band_power):
    """
    Calculates the Neural Activity index from the given band power values.

    Parameters
    ----------
    band_power : dict
        A dictionary of power values, with keys 'alpha', 'beta', etc.

    Returns
    -------
    na : float
        The Neural Activity index.
    """

    na = (band_power['beta'] + band_power['gamma']) / (band_power['theta'] + band_power['alpha'])
    return na


def calculate_engagement(band_power):
    """
    Calculates the Engagement index from the given band power values.

    Parameters
    ----------
    band_power : dict
        A dictionary of power values, with keys 'alpha', 'beta', etc.

    Returns
    -------
    eng : float
        The Engagement index.
    """

    eng = (band_power['theta'] + band_power['alpha']) / (band_power['beta'] + band_power['gamma'])
    return eng



def calculate_performance_enhancement(alpha_power, beta_power):
    """Calculate the Performance Enhancement index using alpha and beta power.

    Parameters
    ----------
    alpha_power : float
        The relative power in the alpha band.
    beta_power : float
        The relative power in the beta band.

    Returns
    -------
    pe : float
        The Performance Enhancement index.
    """

    pe = beta_power / alpha_power
    return pe

def calculate_arousal_index(alpha_power, theta_power):
    """Calculate the Arousal Index using alpha and theta power.

    Parameters
    ----------
    alpha_power : float
        The relative power in the alpha band.
    theta_power : float
        The relative power in the theta band.

    Returns
    -------
    ai : float
        The Arousal Index.
    """

    ai = alpha_power / theta_power
    return ai

def calculate_neural_activity(delta_power, theta_power, alpha_power, beta_power):
    """Calculate the Neural Activity index using delta, theta, alpha and beta power.

    Parameters
    ----------
    delta_power : float
        The relative power in the delta band.
    theta_power : float
        The relative power in the theta band.
    alpha_power : float
        The relative power in the alpha band.
    beta_power : float
        The relative power in the beta band.

    Returns
    -------
    na : float
        The Neural Activity index.
    """

    na = (delta_power + theta_power) / (alpha_power + beta_power)
    return na

def calculate_engagement(alpha_power, theta_power, delta_power):
    """Calculate the Engagement index using alpha, theta and delta power.

    Parameters
    ----------
    alpha_power : float
        The relative power in the alpha band.
    theta_power : float
        The relative power in the theta band.
    delta_power : float
        The relative power in the delta band.

    Returns
    -------
    eng : float
        The Engagement index.
    """

    eng = (alpha_power + theta_power) / delta_power
    return eng

def calculate_load_index(alpha_power, beta_power):
    """Calculate the Load Index using alpha and beta power.

    Parameters
    ----------
    alpha_power : float
        The relative power in the alpha band.
    beta_power : float
        The relative power in the beta band.

    Returns
    -------
    li : float
        The Load Index.
    """

    li = alpha_power / beta_power
    return li

def calculate_alertness(alpha_power, theta_power):
    """Calculate the Alertness index using alpha and theta power.

    Parameters
    ----------
    alpha_power : float
        The relative power in the alpha band.
    theta_power : float
        The relative power in the theta band.

    Returns
    -------
    al : float
        The Alertness index.
    """

    al = alpha_power / (alpha_power + theta_power)
    return al
