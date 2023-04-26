import numpy as np
import mne

def apply_bandpass_filter(eeg_data, l_freq, h_freq, sfreq):
    """
    Apply a bandpass filter to EEG data using the MNE library.

    Parameters:
    ----------
    eeg_data : numpy.ndarray
        2D array containing EEG data.
    l_freq : float
        Lower frequency bound for the bandpass filter.
    h_freq : float
        Upper frequency bound for the bandpass filter.
    sfreq : float
        Sampling frequency of the EEG data.

    Returns:
    -------
    filtered_eeg_data : numpy.ndarray
        2D array containing the filtered EEG data.
    """
    # Create an MNE RawArray object from the EEG data
    info = mne.create_info(ch_names=['EEG'], sfreq=sfreq)
    raw = mne.io.RawArray(eeg_data, info)

    # Apply a bandpass filter to the EEG data using MNE
    raw.filter(l_freq=l_freq, h_freq=h_freq, fir_design='firwin')
    filtered_eeg_data = raw.get_data()

    return filtered_eeg_data

def apply_notch_filter(eeg_data, freq, sfreq):
    """
    Apply a notch filter to EEG data using the MNE library.

    Parameters:
    ----------
    eeg_data : numpy.ndarray
        2D array containing EEG data.
    freq : float
        Frequency to remove from the EEG data.
    sfreq : float
        Sampling frequency of the EEG data.

    Returns:
    -------
    filtered_eeg_data : numpy.ndarray
        2D array containing the filtered EEG data.
    """
    # Create an MNE RawArray object from the EEG data
    info = mne.create_info(ch_names=['EEG'], sfreq=sfreq)
    raw = mne.io.RawArray(eeg_data, info)

    # Apply a notch filter to the EEG data using MNE
    raw.notch_filter(freq, fir_design='firwin')
    filtered_eeg_data = raw.get_data()

    return filtered_eeg_data
