import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plot_coherence(data, freq_range=None):
    """Visualize coherence plot for the given EEG data."""
    if freq_range is not None:
        data = data[(data['frequency'] >= freq_range[0]) & (data['frequency'] <= freq_range[1])]
    
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.lineplot(x='frequency', y='coherence', data=data, ax=ax)
    ax.set_title('Coherence Plot')
    ax.set_xlabel('Frequency (Hz)')
    ax.set_ylabel('Coherence')
    plt.show()