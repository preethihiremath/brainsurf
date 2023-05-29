# import matplotlib.pyplot as plt

# class ComparativeVisualizationFactory:
    # @staticmethod
    # def visualize_mean(pre_mean, during_mean, post_mean):
    #     # Set up the figure and axes
    #     fig, ax = plt.subplots(figsize=(10, 6))

    #     # Create the line plots
    #     x_labels = ['Pre', 'During', 'Post']
    #     line_x = range(3)
    #     line_y1 = [pre_mean, during_mean, post_mean]
    #     ax.plot(line_x, line_y1, color='blue', linewidth=2, linestyle='--', marker='o', label='Mean')

    #     # Set the labels and titlez
    #     ax.set_xticks(line_x)
    #     ax.set_xticklabels(x_labels)
    #     ax.set_xlabel('Meditation State')
    #     ax.set_ylabel('Mean')
    #     ax.set_title('Comparison of Mean Values')
    #     ax.legend()

    #     # Show the plot
    #     plt.show()

    # @staticmethod
    # def visualize_standard_deviation(pre_std, during_std, post_std):
    #     # Set up the figure and axes
    #     fig, ax = plt.subplots(figsize=(10, 6))

    #     # Create the line plots
    #     x_labels = ['Pre', 'During', 'Post']
    #     line_x = range(3)
    #     line_y1 = [pre_std, during_std, post_std]
    #     ax.plot(line_x, line_y1, color='red', linewidth=2, linestyle='--', marker='o', label='Standard Deviation')

    #     # Set the labels and title
    #     ax.set_xticks(line_x)
    #     ax.set_xticklabels(x_labels)
    #     ax.set_xlabel('Meditation State')
    #     ax.set_ylabel('Standard Deviation')
    #     ax.set_title('Comparison of Standard Deviation Values')
    #     ax.legend()

    #     # Show the plot
    #     plt.show()

    # # Implement the remaining visualization functions for median, interquartile range, skewness, kurtosis, range, variance, RMS, spectral power, coherence, and fractal dimension.

    # @staticmethod
    # def visualize_median(pre_median, during_median, post_median):
    #     # Set up the figure and axes
    #     fig, ax = plt.subplots(figsize=(10, 6))

    #     # Create the line plots
    #     x_labels = ['Pre', 'During', 'Post']
    #     line_x = range(3)
    #     line_y1 = [pre_median, during_median, post_median]
    #     ax.plot(line_x, line_y1, color='green', linewidth=2, linestyle='--', marker='o', label='Median')

    #     # Set the labels and title
    #     ax.set_xticks(line_x)
    #     ax.set_xticklabels(x_labels)
    #     ax.set_xlabel('Meditation State')
    #     ax.set_ylabel('Median')
    #     ax.set_title('Comparison of Median Values')
    #     ax.legend()

    #     # Show the plot
    #     plt.show()

    # @staticmethod
    # def visualize_interquartile_range(pre_iqr, during_iqr, post_iqr):
    #     # Set up the figure and axes
    #     fig, ax = plt.subplots(figsize=(10, 6))

    #     # Create the line plots
    #     x_labels = ['Pre', 'During', 'Post']
    #     line_x = range(3)
    #     line_y1 = [pre_iqr, during_iqr, post_iqr]
    #     ax.plot(line_x, line_y1, color='purple', linewidth=2, linestyle='--', marker='o', label='Interquartile Range')

    #     # Set the labels and title
    #     ax.set_xticks(line_x)
    #     ax.set_xticklabels(x_labels)
    #     ax.set_xlabel('Meditation State')
    #     ax.set_ylabel('Interquartile Range')
    #     ax.set_title('Comparison of Interquartile Range Values')
    #     ax.legend()

    #     # Show the plot
    #     plt.show()

    # @staticmethod
    # def visualize_skewness(pre_skewness, during_skewness, post_skewness):
    #     # Set up the figure and axes
    #     fig, ax = plt.subplots(figsize=(10, 6))

    #     # Create the line plots
    #     x_labels = ['Pre', 'During', 'Post']
    #     line_x = range(3)
    #     line_y1 = [pre_skewness, during_skewness, post_skewness]
    #     ax.plot(line_x, line_y1, color='orange', linewidth=2, linestyle='--', marker='o', label='Skewness')

    #     # Set the labels and title
    #     ax.set_xticks(line_x)
    #     ax.set_xticklabels(x_labels)
    #     ax.set_xlabel('Meditation State')
    #     ax.set_ylabel('Skewness')
    #     ax.set_title('Comparison of Skewness Values')
    #     ax.legend()

    #     # Show the plot
    #     plt.show()

    # @staticmethod
    # def visualize_kurtosis(pre_kurtosis, during_kurtosis, post_kurtosis):
    #     # Set up the figure and axes
    #     fig, ax = plt.subplots(figsize=(10, 6))

    #     # Create the line plots
    #     x_labels = ['Pre', 'During', 'Post']
    #     line_x = range(3)
    #     line_y1 = [pre_kurtosis, during_kurtosis, post_kurtosis]
    #     ax.plot(line_x, line_y1, color='magenta', linewidth=2, linestyle='--', marker='o', label='Kurtosis')

    #     # Set the labels and title
    #     ax.set_xticks(line_x)
    #     ax.set_xticklabels(x_labels)
    #     ax.set_xlabel('Meditation State')
    #     ax.set_ylabel('Kurtosis')
    #     ax.set_title('Comparison of Kurtosis Values')
    #     ax.legend()

    #     # Show the plot
    #     plt.show()

    # @staticmethod
    # def visualize_range(pre_range, during_range, post_range):
    #     # Set up the figure and axes
    #     fig, ax = plt.subplots(figsize=(10, 6))

    #     # Create the line plots
    #     x_labels = ['Pre', 'During', 'Post']
    #     line_x = range(3)
    #     line_y1 = [pre_range, during_range, post_range]
    #     ax.plot(line_x, line_y1, color='cyan', linewidth=2, linestyle='--', marker='o', label='Range')

    #     # Set the labels and title
    #     ax.set_xticks(line_x)
    #     ax.set_xticklabels(x_labels)
    #     ax.set_xlabel('Meditation State')
    #     ax.set_ylabel('Range')
    #     ax.set_title('Comparison of Range Values')
    #     ax.legend()

    #     # Show the plot
    #     plt.show()

    # @staticmethod
    # def visualize_variance(pre_variance, during_variance, post_variance):
    #     # Set up the figure and axes
    #     fig, ax = plt.subplots(figsize=(10, 6))

    #     # Create the line plots
    #     x_labels = ['Pre', 'During', 'Post']
    #     line_x = range(3)
    #     line_y1 = [pre_variance, during_variance, post_variance]
    #     ax.plot(line_x, line_y1, color='brown', linewidth=2, linestyle='--', marker='o', label='Variance')

    #     # Set the labels and title
    #     ax.set_xticks(line_x)
    #     ax.set_xticklabels(x_labels)
    #     ax.set_xlabel('Meditation State')
    #     ax.set_ylabel('Variance')
    #     ax.set_title('Comparison of Variance Values')
    #     ax.legend()

    #     # Show the plot
    #     plt.show()

    # @staticmethod
    # def visualize_rms(pre_rms, during_rms, post_rms):
    #     # Set up the figure and axes
    #     fig, ax = plt.subplots(figsize=(10, 6))

    #     # Create the line plots
    #     x_labels = ['Pre', 'During', 'Post']
    #     line_x = range(3)
    #     line_y1 = [pre_rms, during_rms, post_rms]
    #     ax.plot(line_x, line_y1, color='gray', linewidth=2, linestyle='--', marker='o', label='Root Mean Square (RMS)')

    #     # Set the labels and title
    #     ax.set_xticks(line_x)
    #     ax.set_xticklabels(x_labels)
    #     ax.set_xlabel('Meditation State')
    #     ax.set_ylabel('Root Mean Square (RMS)')
    #     ax.set_title('Comparison of Root Mean Square (RMS) Values')
    #     ax.legend()

    #     # Show the plot
    #     plt.show()

    # # Implement the remaining visualization functions for spectral power, coherence, and fractal dimension.
    
    # @staticmethod
    # def visualize_spectral_power(pre_alpha_power, during_alpha_power, post_alpha_power,
    #                              pre_beta_power, during_beta_power, post_beta_power):
    #     # Set up the figure and axes
    #     fig, ax = plt.subplots(figsize=(10, 6))

    #     # Create the line plots
    #     x_labels = ['Pre', 'During', 'Post']
    #     line_x = range(3)
        
    #     # Alpha power
    #     line_y1 = [pre_alpha_power, during_alpha_power, post_alpha_power]
    #     ax.plot(line_x, line_y1, color='blue', linewidth=2, linestyle='--', marker='o', label='Alpha Power')
        
    #     # Beta power
    #     line_y2 = [pre_beta_power, during_beta_power, post_beta_power]
    #     ax.plot(line_x, line_y2, color='red', linewidth=2, linestyle='--', marker='o', label='Beta Power')

    #     # Set the labels and title
    #     ax.set_xticks(line_x)
    #     ax.set_xticklabels(x_labels)
    #     ax.set_xlabel('Meditation State')
    #     ax.set_ylabel('Power')
    #     ax.set_title('Comparison of Spectral Power (Alpha and Beta) Values')
    #     ax.legend()

    #     # Show the plot
    #     plt.show()

    # @staticmethod
    # def visualize_coherence(pre_coherence, during_coherence, post_coherence):
    #     # Set up the figure and axes
    #     fig, ax = plt.subplots(figsize=(10, 6))

    #     # Create the line plots
    #     x_labels = ['Pre', 'During', 'Post']
    #     line_x = range(3)
    #     line_y1 = [pre_coherence, during_coherence, post_coherence]
    #     ax.plot(line_x, line_y1, color='green', linewidth=2, linestyle='--', marker='o', label='Coherence')

    #     # Set the labels and title
    #     ax.set_xticks(line_x)
    #     ax.set_xticklabels(x_labels)
    #     ax.set_xlabel('Meditation State')
    #     ax.set_ylabel('Coherence')
    #     ax.set_title('Comparison of Coherence Values')
    #     ax.legend()

    #     # Show the plot
    #     plt.show()

    # @staticmethod
    # def visualize_fractal_dimension(pre_fractal_dimension, during_fractal_dimension, post_fractal_dimension):
    #     # Set up the figure and axes
    #     fig, ax = plt.subplots(figsize=(10, 6))

    #     # Create the line plots
    #     x_labels = ['Pre', 'During', 'Post']
    #     line_x = range(3)
    #     line_y1 = [pre_fractal_dimension, during_fractal_dimension, post_fractal_dimension]
    #     ax.plot(line_x, line_y1, color='purple', linewidth=2, linestyle='--', marker='o', label='Fractal Dimension')

    #     # Set the labels and title
    #     ax.set_xticks(line_x)
    #     ax.set_xticklabels(x_labels)
    #     ax.set_xlabel('Meditation State')
    #     ax.set_ylabel('Fractal Dimension')
    #     ax.set_title('Comparison of Fractal Dimension Values')
    #     ax.legend()

    #     # Show the plot
    #     plt.show()
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats, signal

class ComparativeVisualizationFactory:
    @staticmethod
    def visualize_mean(pre_data, during_data, post_data):
        # Calculate the mean values
        pre_mean = np.mean(pre_data)
        during_mean = np.mean(during_data)
        post_mean = np.mean(post_data)

        # Set up the figure and axes
        fig, ax = plt.subplots(figsize=(10, 6))

        # Create the line plots
        x_labels = ['Pre', 'During', 'Post']
        line_x = range(3)
        line_y = [pre_mean, during_mean, post_mean]
        ax.plot(line_x, line_y, color='blue', linewidth=2, linestyle='--', marker='o', label='Mean')

        # Set the labels and title
        ax.set_xticks(line_x)
        ax.set_xticklabels(x_labels)
        ax.set_xlabel('Meditation State')
        ax.set_ylabel('Mean')
        ax.set_title('Comparison of Mean Values')
        ax.legend()

        # Show the plot
        plt.show()

    @staticmethod
    def visualize_standard_deviation(pre_data, during_data, post_data):
        # Calculate the standard deviation values
        pre_std = np.std(pre_data)
        during_std = np.std(during_data)
        post_std = np.std(post_data)

        # Set up the figure and axes
        fig, ax = plt.subplots(figsize=(10, 6))

        # Create the line plots
        x_labels = ['Pre', 'During', 'Post']
        line_x = range(3)
        line_y = [pre_std, during_std, post_std]
        ax.plot(line_x, line_y, color='red', linewidth=2, linestyle='--', marker='o', label='Standard Deviation')

        # Set the labels and title
        ax.set_xticks(line_x)
        ax.set_xticklabels(x_labels)
        ax.set_xlabel('Meditation State')
        ax.set_ylabel('Standard Deviation')
        ax.set_title('Comparison of Standard Deviation Values')
        ax.legend()

        # Show the plot
        plt.show()

    @staticmethod
    def visualize_median(pre_data, during_data, post_data):
        # Calculate the median values
        pre_median = np.median(pre_data)
        during_median = np.median(during_data)
        post_median = np.median(post_data)

        # Set up the figure and axes
        fig, ax = plt.subplots(figsize=(10, 6))

        # Create the line plots
        x_labels = ['Pre', 'During', 'Post']
        line_x = range(3)
        line_y = [pre_median, during_median, post_median]
        ax.plot(line_x, line_y, color='green', linewidth=2, linestyle='--', marker='o', label='Median')

        # Set the labels and title
        ax.set_xticks(line_x)
        ax.set_xticklabels(x_labels)
        ax.set_xlabel('Meditation State')
        ax.set_ylabel('Median')
        ax.set_title('Comparison of Median Values')
        ax.legend()

        # Show the plot
        plt.show()

    @staticmethod
    def visualize_interquartile_range(pre_data, during_data, post_data):
        # Calculate the interquartile range values
        pre_iqr = np.percentile(pre_data, 75) - np.percentile(pre_data, 25)
        during_iqr = np.percentile(during_data, 75) - np.percentile(during_data, 25)
        post_iqr = np.percentile(post_data, 75) - np.percentile(post_data, 25)

        # Set up the figure and axes
        fig, ax = plt.subplots(figsize=(10, 6))

        # Create the line plots
        x_labels = ['Pre', 'During', 'Post']
        line_x = range(3)
        line_y = [pre_iqr, during_iqr, post_iqr]
        ax.plot(line_x, line_y, color='orange', linewidth=2, linestyle='--', marker='o', label='Interquartile Range')

        # Set the labels and title
        ax.set_xticks(line_x)
        ax.set_xticklabels(x_labels)
        ax.set_xlabel('Meditation State')
        ax.set_ylabel('Interquartile Range')
        ax.set_title('Comparison of Interquartile Range Values')
        ax.legend()

        # Show the plot
        plt.show()

    @staticmethod
    def visualize_skewness(pre_data, during_data, post_data):
        # Calculate the skewness values
        pre_skewness = stats.skew(pre_data)
        during_skewness = stats.skew(during_data)
        post_skewness = stats.skew(post_data)

        # Set up the figure and axes
        fig, ax = plt.subplots(figsize=(10, 6))

        # Create the line plots
        x_labels = ['Pre', 'During', 'Post']
        line_x = range(3)
        line_y = [pre_skewness, during_skewness, post_skewness]
        ax.plot(line_x, line_y, color='purple', linewidth=2, linestyle='--', marker='o', label='Skewness')

        # Set the labels and title
        ax.set_xticks(line_x)
        ax.set_xticklabels(x_labels)
        ax.set_xlabel('Meditation State')
        ax.set_ylabel('Skewness')
        ax.set_title('Comparison of Skewness Values')
        ax.legend()

        # Show the plot
        plt.show()

    @staticmethod
    def visualize_kurtosis(pre_data, during_data, post_data):
        # Calculate the kurtosis values
        pre_kurtosis = stats.kurtosis(pre_data)
        during_kurtosis = stats.kurtosis(during_data)
        post_kurtosis = stats.kurtosis(post_data)

        # Set up the figure and axes
        fig, ax = plt.subplots(figsize=(10, 6))

        # Create the line plots
        x_labels = ['Pre', 'During', 'Post']
        line_x = range(3)
        line_y = [pre_kurtosis, during_kurtosis, post_kurtosis]
        ax.plot(line_x, line_y, color='magenta', linewidth=2, linestyle='--', marker='o', label='Kurtosis')

        # Set the labels and title
        ax.set_xticks(line_x)
        ax.set_xticklabels(x_labels)
        ax.set_xlabel('Meditation State')
        ax.set_ylabel('Kurtosis')
        ax.set_title('Comparison of Kurtosis Values')
        ax.legend()

        # Show the plot
        plt.show()

    @staticmethod
    def visualize_range(pre_data, during_data, post_data):
        # Calculate the range values
        pre_range = np.max(pre_data) - np.min(pre_data)
        during_range = np.max(during_data) - np.min(during_data)
        post_range = np.max(post_data) - np.min(post_data)

        # Set up the figure and axes
        fig, ax = plt.subplots(figsize=(10, 6))

        # Create the line plots
        x_labels = ['Pre', 'During', 'Post']
        line_x = range(3)
        line_y = [pre_range, during_range, post_range]
        ax.plot(line_x, line_y, color='brown', linewidth=2, linestyle='--', marker='o', label='Range')

        # Set the labels and title
        ax.set_xticks(line_x)
        ax.set_xticklabels(x_labels)
        ax.set_xlabel('Meditation State')
        ax.set_ylabel('Range')
        ax.set_title('Comparison of Range Values')
        ax.legend()

        # Show the plot
        plt.show()

    @staticmethod
    def visualize_variance(pre_data, during_data, post_data):
        # Calculate the variance values
        pre_variance = np.var(pre_data)
        during_variance = np.var(during_data)
        post_variance = np.var(post_data)

        # Set up the figure and axes
        fig, ax = plt.subplots(figsize=(10, 6))

        # Create the line plots
        x_labels = ['Pre', 'During', 'Post']
        line_x = range(3)
        line_y = [pre_variance, during_variance, post_variance]
        ax.plot(line_x, line_y, color='gray', linewidth=2, linestyle='--', marker='o', label='Variance')

        # Set the labels and title
        ax.set_xticks(line_x)
        ax.set_xticklabels(x_labels)
        ax.set_xlabel('Meditation State')
        ax.set_ylabel('Variance')
        ax.set_title('Comparison of Variance Values')
        ax.legend()

        # Show the plot
        plt.show()

    @staticmethod
    def visualize_rms(pre_data, during_data, post_data):
        # Calculate the root mean square (RMS) values
        pre_rms = np.sqrt(np.mean(np.square(pre_data)))
        during_rms = np.sqrt(np.mean(np.square(during_data)))
        post_rms = np.sqrt(np.mean(np.square(post_data)))

        # Set up the figure and axes
        fig, ax = plt.subplots(figsize=(10, 6))

        # Create the line plots
        x_labels = ['Pre', 'During', 'Post']
        line_x = range(3)
        line_y = [pre_rms, during_rms, post_rms]
        ax.plot(line_x, line_y, color='cyan', linewidth=2, linestyle='--', marker='o', label='RMS')

        # Set the labels and title
        ax.set_xticks(line_x)
        ax.set_xticklabels(x_labels)
        ax.set_xlabel('Meditation State')
        ax.set_ylabel('RMS')
        ax.set_title('Comparison of RMS Values')
        ax.legend()

        # Show the plot
        plt.show()

    @staticmethod
    def visualize_spectral_power(pre_data, during_data, post_data, fs):
        # Calculate the spectral power values using the periodogram method
        pre_freq, pre_power = signal.periodogram(pre_data, fs)
        during_freq, during_power = signal.periodogram(during_data, fs)
        post_freq, post_power = signal.periodogram(post_data, fs)

        # Set up the figure and axes
        fig, ax = plt.subplots(figsize=(10, 6))

        # Create the line plots
        ax.plot(pre_freq, pre_power, color='blue', linewidth=2, linestyle='--', label='Pre')
        ax.plot(during_freq, during_power, color='red', linewidth=2, linestyle='--', label='During')
        ax.plot(post_freq, post_power, color='green', linewidth=2, linestyle='--', label='Post')

        # Set the labels and title
        ax.set_xlabel('Frequency (Hz)')
        ax.set_ylabel('Power Spectral Density')
        ax.set_title('Comparison of Power Spectral Density')
        ax.legend()

        # Show the plot
        plt.show()

    @staticmethod
    def visualize_coherence(data1, data2, fs):
        # Calculate the coherence values using Welch's method
        freq, coherence = signal.coherence(data1, data2, fs)

        # Set up the figure and axes
        fig, ax = plt.subplots(figsize=(10, 6))

        # Create the line plot
        ax.plot(freq, coherence, color='blue', linewidth=2, linestyle='--', label='Coherence')

        # Set the labels and title
        ax.set_xlabel('Frequency (Hz)')
        ax.set_ylabel('Coherence')
        ax.set_title('Coherence between Signals')
        ax.legend()

        # Show the plot
        plt.show()

    @staticmethod
    def calculate_boxcount(data, scales):
        distance_matrix = pairwise_distances(data)
        mean_distances = np.mean(distance_matrix, axis=1)

        counts = []
        for scale in scales:
            count = np.sum(mean_distances <= scale)
            counts.append(count)

        return counts

    @staticmethod
    def visualize_fractal_dimension(data, scales):
        counts = calculate_boxcount(data, scales)
        dimensions = np.log(counts) / np.log(scales)

        # Set up the figure and axes
        fig, ax = plt.subplots(figsize=(10, 6))

        # Create the line plot
        ax.plot(scales, dimensions, color='blue', linewidth=2, marker='o', label='Fractal Dimension')

        # Set the labels and title
        ax.set_xscale('log')
        ax.set_yscale('log')
        ax.set_xlabel('Scale')
        ax.set_ylabel('Fractal Dimension')
        ax.set_title('Fractal Dimension Analysis')
        ax.legend()

        # Show the plot
        plt.show()

