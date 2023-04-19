
# without using libraries
# import numpy as np

# def butter_bandpass(lowcut, highcut, fs, order=5):
#     """
#     Design a bandpass Butterworth filter.

#     Parameters
#     ----------
#     lowcut : float
#         Lower cut-off frequency of the filter.
#     highcut : float
#         Upper cut-off frequency of the filter.
#     fs : float
#         Sampling frequency of the signal.
#     order : int
#         Order of the Butterworth filter.

#     Returns
#     -------
#     b : array-like
#         Numerator coefficients of the filter.
#     a : array-like
#         Denominator coefficients of the filter.
#     """
#     nyq = 0.5 * fs
#     low = lowcut / nyq
#     high = highcut / nyq
#     b, a = butter_bandpass_coeffs(low, high, order)
#     return b, a

# def butter_bandpass_coeffs(low, high, order=5):
#     """
#     Compute the numerator (b) and denominator (a) coefficients of a
#     bandpass Butterworth filter.

#     Parameters
#     ----------
#     low : float
#         Lower cut-off frequency of the filter.
#     high : float
#         Upper cut-off frequency of the filter.
#     order : int
#         Order of the Butterworth filter.

#     Returns
#     -------
#     b : array-like
#         Numerator coefficients of the filter.
#     a : array-like
#         Denominator coefficients of the filter.
#     """
#     z = np.exp(1j * np.pi * (2 * np.arange(1, order+1) + order + 1) / (4 * order))
#     p = np.zeros_like(z)
#     p[:order:2] = np.cos(np.pi * (low + high))
#     p[1:order:2] = -np.sin(np.pi * (high - low))
#     return np.real(np.poly(np.concatenate([z, np.conj(z)]))), np.real(np.poly(np.concatenate([p, np.conj(p)])))

# def butter_notch(f0, Q, fs):
#     """
#     Design a notch Butterworth filter.

#     Parameters
#     ----------
#     f0 : float
#         Center frequency of the filter.
#     Q : float
#         Quality factor of the filter.
#     fs : float
#         Sampling frequency of the signal.

#     Returns
#     -------
#     b : array-like
#         Numerator coefficients of the filter.
#     a : array-like
#         Denominator coefficients of the filter.
#     """
#     w0 = 2 * np.pi * f0 / fs
#     alpha = np.sin(w0) / (2 * Q)
#     b, a = butter_notch_coeffs(w0, alpha)
#     return b, a

# def butter_notch_coeffs(w0, alpha):
#     """
#     Compute the numerator (b) and denominator (a) coefficients of a
#     notch Butterworth filter.

#     Parameters
#     ----------
#     w0 : float
#         Center frequency of the filter.
#     alpha : float
#         Bandwidth of the filter.

#     Returns
#     -------
#     b : array-like
#         Numerator coefficients of the filter.
#     a : array-like
#         Denominator coefficients of the filter.
#     """
#     b = np.array([1, -2 * np.cos(w0), 1])
#     a = np.array([1, -2 * np.cos(w0) * (1 - alpha), (1 - alpha)**2])
#     return b, a
