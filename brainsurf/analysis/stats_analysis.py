import numpy as np
import pandas as pd
from scipy import signal

import nolds

def calculate_mean(data):
    return np.mean(data)

def calculate_variance(data):
    return np.var(data)

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
