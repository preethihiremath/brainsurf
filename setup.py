import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Read the Excel file into a pandas DataFrame
df = pd.read_excel('eeg_data.xlsx')

# Convert the DataFrame to a numpy array
data = df.to_numpy()

# Extract the time and EEG signals from the array
time = data[:, 0]
eeg = data[:, 1]

# Extract the frequency-domain signals from the array
alpha = data[:, 2]
beta = data[:, 3]
delta = data[:, 4]
theta = data[:, 5]

# Plot the time-domain signal
plt.figure()
plt.plot(time, eeg)
plt.xlabel('Time (sec)')
plt.ylabel('EEG')
plt.title('Time-Domain EEG Signal')

# Compute the power spectral density (PSD) using Welch's method
f, psd = signal.welch(eeg, fs=1/(time[1]-time[0]), nperseg=1024)

# Plot the frequency-domain signals
plt.figure()
plt.semilogx(f, psd)
plt.xlabel('Frequency (Hz)')
plt.ylabel('PSD')
plt.title('Frequency-Domain EEG Signal')
plt.show()
