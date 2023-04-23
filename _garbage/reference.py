import pandas as pd
from stats_analysis import calculate_coherence, calculate_cross_corr
from visualization import coherence_plot, cross_corr_plot, heatmap, cluster_plot

# Load data
data = pd.read_csv('data.csv')

# Calculate coherence and cross-correlation
coherence_data = calculate_coherence(data)
cross_corr_data = calculate_cross_corr(data)

# Visualize coherence plot
coherence_plot(coherence_data)

# Visualize cross-correlation plot
cross_corr_plot(cross_corr_data, 'EEG', 'alpha')

# Visualize heatmap of EEG power in different frequency bands
heatmap(data[['alpha', 'beta', 'delta', 'theta']].corr())

# Visualize cluster plot of EEG power in different frequency bands
cluster_plot(data[['alpha', 'beta', 'delta', 'theta']].corr())