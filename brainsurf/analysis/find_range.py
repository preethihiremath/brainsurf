import numpy as np

def find_frequency_bands(data, sampling_rate):
    fft_values = np.fft.fft(data)
    fft_freq = np.fft.fftfreq(len(data), 1 / sampling_rate)
    
    # Define frequency ranges for each band
    alpha_range = (8, 12)
    beta_range = (12, 30)
    theta_range = (4, 8)
    delta_range = (0.5, 4)
    gamma_range = (30, 50)
    
    # Find indices within each frequency range
    alpha_indices = np.where((fft_freq >= alpha_range[0]) & (fft_freq <= alpha_range[1]))[0]
    beta_indices = np.where((fft_freq >= beta_range[0]) & (fft_freq <= beta_range[1]))[0]
    theta_indices = np.where((fft_freq >= theta_range[0]) & (fft_freq <= theta_range[1]))[0]
    delta_indices = np.where((fft_freq >= delta_range[0]) & (fft_freq <= delta_range[1]))[0]
    gamma_indices = np.where((fft_freq >= gamma_range[0]) & (fft_freq <= gamma_range[1]))[0]
    
    # Calculate the average power within each frequency range
    alpha_power = np.mean(np.abs(fft_values[alpha_indices]) ** 2)
    beta_power = np.mean(np.abs(fft_values[beta_indices]) ** 2)
    theta_power = np.mean(np.abs(fft_values[theta_indices]) ** 2)
    delta_power = np.mean(np.abs(fft_values[delta_indices]) ** 2)
    gamma_power = np.mean(np.abs(fft_values[gamma_indices]) ** 2)
    
    return {
        'alpha': alpha_power,
        'beta': beta_power,
        'theta': theta_power,
        'delta': delta_power,
        'gamma': gamma_power
    }
