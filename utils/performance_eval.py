import pandas as pd
import os
import numpy as np


def calculate_mse(y_true, y_pred):
    """Calculates mean squared error between true and predicted values."""
    return np.mean((y_true - y_pred) ** 2)

def calculate_r_squared(y_true, y_pred):
    """Calculates R^2 coefficient of determination between true and predicted values."""
    ss_res = np.sum((y_true - y_pred) ** 2)
    ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
    return 1 - (ss_res / ss_tot)

def k_fold_cross_validation(X, y, model, k):
    """Performs k-fold cross validation and returns mean validation score."""
    scores = []
    n_samples = len(X)
    fold_size = n_samples // k
    for i in range(k):
        start = i * fold_size
        end = start + fold_size
        X_train = np.concatenate((X[:start], X[end:]))
        y_train = np.concatenate((y[:start], y[end:]))
        X_val = X[start:end]
        y_val = y[start:end]
        model.fit(X_train, y_train)
        y_pred = model.predict(X_val)
        score = calculate_r_squared(y_val, y_pred)
        scores.append(score)
    return np.mean(scores)