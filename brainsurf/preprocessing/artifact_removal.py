import numpy as np
from scipy import signal
from sklearn.decomposition import FastICA
from sklearn.preprocessing import StandardScaler

def signal_averaging(data):
    """
    Perform signal averaging to remove random noise or artifacts.
    """
    averaged_signal = np.mean(data, axis=0)
    return averaged_signal

def wavelet_denoising(data, wavelet='db4', level=1, threshold_type='soft'):
    """
    Apply wavelet denoising to remove noise and artifacts.
    """
    coefficients = pywt.wavedec(data, wavelet, level=level)
    threshold = np.sqrt(2 * np.log(len(data))) * np.median(np.abs(coefficients[-level]))
    denoised_coefficients = [pywt.threshold(c, value=threshold, mode=threshold_type) for c in coefficients]
    denoised_signal = pywt.waverec(denoised_coefficients, wavelet)
    return denoised_signal

def artifact_subspace_reconstruction(data, artifact_components):
    """
    Perform artifact subspace reconstruction to remove artifacts modeled as a subspace.
    """
    artifact_components = StandardScaler().fit_transform(artifact_components)
    data_projected = data - np.dot(np.dot(data, artifact_components.T), artifact_components)
    return data_projected

def pca_removal(data, n_components=1):
    """
    Perform PCA to remove artifacts by identifying and removing components capturing the most variance.
    """
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)
    pca = PCA(n_components=n_components)
    components = pca.fit_transform(scaled_data)
    reconstructed_data = scaler.inverse_transform(pca.inverse_transform(components))
    return reconstructed_data

def regression_based_removal(data, regressor, artifacts):
    """
    Apply regression-based artifact removal by modeling artifacts as a function of other variables.
    """
    predicted_artifacts = regressor.predict(data)
    cleaned_data = data - predicted_artifacts.reshape(-1, 1)
    return cleaned_data

def template_subtraction(data, template):
    """
    Perform template subtraction to remove artifacts with a consistent shape or waveform.
    """
    cleaned_data = data - template
    return cleaned_data

def ica_removal(data, n_components=None, random_state=None):
    """
    Apply Independent Component Analysis (ICA) to remove artifacts from the data.
    """
    ica = FastICA(n_components=n_components, random_state=random_state)
    cleaned_data = ica.fit_transform(data)
    return cleaned_data
