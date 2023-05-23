import numpy as np
from scipy.stats import ttest_rel, wilcoxon
# from .cognitive_indexes import calculate_pe,calculate_band_power,calculate_arousal_index, calculate_neural_activity,calculate_engagement

def calculate_cognitive_indexes(data_before, data_after):
    """
    Calculate cognitive indexes from EEG data to assess attention, mental workload, or cognitive performance.
    Examples of cognitive indexes include response time, error rates, or other relevant measures.

    Args:
    - data_before (pandas.DataFrame): EEG data before meditation.
    - data_after (pandas.DataFrame): EEG data after meditation.

    Returns:
    - cognitive_indexes_before (numpy.ndarray): Cognitive indexes calculated from data_before.
    - cognitive_indexes_after (numpy.ndarray): Cognitive indexes calculated from data_after.
    """

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

    # Extract the necessary data columns from data_before
    freqs_before = data_before['sec']
    alpha_power_before = data_before['alpha']
    beta_power_before = data_before['beta']
    delta_power_before = data_before['delta']
    theta_power_before = data_before['theta']

    # Define the frequency bands for calculation
    bands = {
        'delta': (0.5, 4),
        'theta': (4, 8),
        'alpha': (8, 13),
        'beta': (13, 30)
    }

    # Calculate cognitive indexes before meditation
    pe_before = calculate_pe(alpha_power_before, beta_power_before)
    ai_before = calculate_arousal_index(alpha_power_before, theta_power_before)
    na_before = calculate_neural_activity(
        delta_power_before, theta_power_before, alpha_power_before, beta_power_before
    )
    eng_before = calculate_engagement(alpha_power_before, theta_power_before, delta_power_before)
    # Extract the necessary data columns from data_after
    freqs_after = data_after['sec']
    alpha_power_after = data_after['alpha']
    beta_power_after = data_after['beta']
    delta_power_after = data_after['delta']
    theta_power_after = data_after['theta']

    # Calculate band power for each frequency band after meditation
    band_power_after = calculate_band_power(freqs_after, alpha_power_after, bands)

    # Calculate cognitive indexes after meditation
    pe_after = calculate_pe(alpha_power_after,beta_power_after)
    ai_after = calculate_arousal_index(alpha_power_after,theta_power_after)
    na_after = calculate_neural_activity(
        delta_power_after, theta_power_after, alpha_power_after, beta_power_after
    )
    eng_after = calculate_engagement(alpha_power_after, theta_power_after, delta_power_after)

    # Compare the cognitive indexes before and after meditation using paired t-test
    cognitive_indexes_before = np.array([pe_before, ai_before, na_before, eng_before])
    cognitive_indexes_after = np.array([pe_after, ai_after, na_after, eng_after])
  
    # Perform the paired t-test
    return cognitive_indexes_before, cognitive_indexes_after



def compare_cognitive_indexes(cognitive_indexes_before, cognitive_indexes_after, test_type="paired_ttest"):
    """
    Compare cognitive indexes before and after meditation using appropriate statistical tests.

    Args:
    - cognitive_indexes_before (numpy.ndarray): Cognitive indexes before meditation.
    - cognitive_indexes_after (numpy.ndarray): Cognitive indexes after meditation.
    - test_type (str): Type of statistical test to perform. Options: "paired_ttest", "wilcoxon".

    Returns:
    - test_statistic (float): Test statistic value.
    - p_value (float): P-value indicating the statistical significance.
    """

    if test_type == "paired_ttest":
        # Perform paired t-test
        test_statistic, p_value = ttest_rel(cognitive_indexes_before, cognitive_indexes_after)
    elif test_type == "wilcoxon":
        # Perform Wilcoxon signed-rank test
        test_statistic, p_value = wilcoxon(cognitive_indexes_before, cognitive_indexes_after)
    else:
        raise ValueError("Invalid test_type. Options: 'paired_ttest', 'wilcoxon'")

    return test_statistic, p_value
