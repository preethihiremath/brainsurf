import numpy as np
from scipy.stats import ttest_ind, f_oneway
from statsmodels.stats import power

def calculate_t_test(data_pre, data_post):
    t_values = []
    p_values = []
    for feature_idx in range(data_pre.shape[1]):
        pre_vals = data_pre[:, feature_idx]
        post_vals = data_post[:, feature_idx]
        t, p = ttest_ind(pre_vals, post_vals)
        t_values.append(t)
        p_values.append(p)
    return t_values, p_values

def calculate_anova(data_pre, data_during, data_post):
    f_values = []
    p_values = []
    for feature_idx in range(data_pre.shape[1]):
        pre_vals = data_pre[:, feature_idx]
        during_vals = data_during[:, feature_idx]
        post_vals = data_post[:, feature_idx]
        f, p = f_oneway(pre_vals, during_vals, post_vals)
        f_values.append(f)
        p_values.append(p)
    return f_values, p_values

def calculate_cohens_d(data_pre, data_post):
    cohens_d = []
    for feature_idx in range(data_pre.shape[1]):
        pre_vals = data_pre[:, feature_idx]
        post_vals = data_post[:, feature_idx]
        pooled_std = np.sqrt(((len(pre_vals)-1) * np.var(pre_vals) + (len(post_vals)-1) * np.var(post_vals)) / (len(pre_vals) + len(post_vals) - 2))
        d = (np.mean(pre_vals) - np.mean(post_vals)) / pooled_std
        cohens_d.append(d)
    return cohens_d


