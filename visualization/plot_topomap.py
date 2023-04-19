import numpy as np
import matplotlib.pyplot as plt

def plot_topomap(data, pos, vmin=None, vmax=None, cmap='viridis', show=True):
    """Plot a topographic map of EEG data.
    
    Args:
        data (array-like): 1D array of EEG data values.
        pos (array-like): 2D array of electrode positions (x, y coordinates).
        vmin (float): Minimum value for the color scale (optional).
        vmax (float): Maximum value for the color scale (optional).
        cmap (str): Name of the color map to use (optional).
        show (bool): Whether to display the plot (optional).
        
    Returns:
        fig (matplotlib Figure): The figure object for the plot.
        ax (matplotlib Axes): The axes object for the plot.
    """
    fig, ax = plt.subplots()
    
    # Plot the topographic map using a scatter plot
    sc = ax.scatter(pos[:, 0], pos[:, 1], c=data, cmap=cmap, vmin=vmin, vmax=vmax)
    
    # Add a colorbar
    plt.colorbar(sc, ax=ax)
    
    # Set the axis limits to fit the electrode positions
    ax.set_xlim([np.min(pos[:, 0]) - 0.1, np.max(pos[:, 0]) + 0.1])
    ax.set_ylim([np.min(pos[:, 1]) - 0.1, np.max(pos[:, 1]) + 0.1])
    
    # Add labels
    ax.set_title('Topographic Map')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    
    if show:
        plt.show()
    
    return fig, ax
