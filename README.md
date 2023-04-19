# Description
ESP is a Python library for processing and analyzing EEG (electroencephalography) signals. It provides a collection of tools and methods for reading, preprocessing, analyzing, and visualizing EEG data. The library is built using the NumPy, SciPy, and Matplotlib packages and is designed to be easily extensible for custom analysis and visualization needs

# Installation
ESP can be installed using pip, a Python package manager. To install the latest stable version of the library, run the following command:
pip install esp

# Github
Alternatively, you can clone the repository from GitHub and install it from source:
git clone https://github.com/preethihiremath/esp
cd esp
pip install -r requirements.txt
python setup.py install


import esp.data as data
import esp.preprocessing as pre
import esp.analysis as analysis
import esp.visualization as vis

#load EEG data from file
eeg_data = data.read_edf_file('eeg_data.edf')

#preprocess the data
preprocessed_data = pre.bandpass_filter(eeg_data, low_cutoff=1, high_cutoff=40)

#analyze the data
erp_data = analysis.compute_erp(preprocessed_data, event_markers=[1, 2, 3], epoch_duration=2)

#visualize the results
vis.plot_erp(erp_data)