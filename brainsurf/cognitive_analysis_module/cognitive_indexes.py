import numpy as np

def calculate_band_power(freqs, power, bands):
    band_power = {}
    for band, f_range in bands.items():
        idx = np.logical_and(freqs >= f_range[0], freqs <= f_range[1])
        band_power[band] = np.trapz(power[idx], freqs[idx])

    return band_power

def calculate_pe(alpha_power, beta_power):
    pe = beta_power / alpha_power
    return pe


def calculate_arousal_index(alpha_power, theta_power):
    ai = alpha_power / theta_power
    return ai


def calculate_neural_activity(delta_power, theta_power, alpha_power, beta_power):
    na = (delta_power + theta_power) / (alpha_power + beta_power)
    return na

def calculate_engagement(alpha_power, theta_power, delta_power):
    eng = (alpha_power + theta_power) / delta_power
    return eng

def calculate_load_index(alpha_power, beta_power):
    li = alpha_power / beta_power
    return li

def calculate_alertness(alpha_power, theta_power):
    al = alpha_power / (alpha_power + theta_power)
    return al
