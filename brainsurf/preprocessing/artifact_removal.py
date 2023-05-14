# import numpy as np
# import mne

# # load the EEG data
# raw = mne.io.read_raw_eeglab('eeg_data.set')

# # set up ICA parameters
# ica = mne.preprocessing.ICA(n_components=20, random_state=42, method='fastica')

# # fit ICA to the raw data
# ica.fit(raw)

# # plot the sources
# ica.plot_sources(raw)

# # pick the components to remove based on visual inspection
# ica.exclude = [0, 2, 4, 5, 7, 11, 15]

# # apply ICA to remove the selected components
# ica.apply(raw)
