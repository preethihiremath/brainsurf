import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_cross_corr(data, channel_1, channel_2):
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.lineplot(x='time', y='cross_corr', data=data, ax=ax)
    ax.set_title(f'Cross-correlation between {channel_1} and {channel_2}')
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Cross-correlation')
    plt.show()

