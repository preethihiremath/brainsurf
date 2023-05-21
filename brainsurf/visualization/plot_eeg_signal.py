import matplotlib.pyplot as plt

def plot_eeg_signal(sec, EEG, title='EEG Signal', xlabel='Time (sec)', ylabel='Amplitude (uV)'):
    plt.plot(sec, EEG)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
