import matplotlib.pyplot as plt

def plot_eeg_signal(time, eeg, title='EEG Signal', xlabel='Time (sec)', ylabel='Amplitude (uV)'):
    plt.plot(time, eeg)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()