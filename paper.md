---
title: 'BrainSurf: An Open-Source Python Library for EEG Signal Analysis in Meditation Research'
tags:
  - Python
  - EEG
  - electroencephalography
  - meditation
  - neuroscience
  - signal processing
authors:
  - name: Preethi V. Hiremath
    affiliation: 1
    orcid: 0009-0002-8984-3049
    email: preethivhiremath.vh@gmail.com
  - name: Rakshitha B. R.
    affiliation: 1
    email: rakshitharavishankar2000@gmail.com
  - name: Rashi Prasad
    affiliation: 1
    email: rashiprasad1@gmail.com
affiliations:
  - name: Department of Information Science and Engineering, BMS College of Engineering, Bengaluru, India
    index: 1
date: 2025-10-28
bibliography: paper.bib
---

# Summary

**BrainSurf** is an open-source Python library developed for preprocessing, feature extraction, and statistical analysis of EEG (Electroencephalography) signals, with a focus on meditation-based cognitive neuroscience research. It provides predefined functions for high-pass and low-pass filtering, Common Average Referencing (CAR), artifact removal using ICA (via MNE), epoching, power spectral density (PSD) computation, nonlinear complexity analysis, and inter-channel connectivity estimation.

The library was developed to support EEG-based meditation research, where neural patterns before and after meditative states are studied for their cognitive implications. BrainSurf enables reproducible EEG analysis through an intuitive API and modular design, empowering researchers to efficiently process large EEG datasets and extract meaningful cognitive features. It is available on PyPI (`pip install brainsurf`) and is built on NumPy, SciPy, Matplotlib, MNE, pyabf, and nolds.

# Statement of Need

EEG analysis is critical in understanding how meditation alters cognitive states such as attention, relaxation, and emotional balance. However, existing EEG software—such as MNE-Python [@gramfort2013] and EEGLAB [@delorme2004]—are architected around clinical and experimental paradigms (e.g., event-related potentials, source localisation) that do not map naturally onto the continuous, steady-state nature of meditation recordings. These tools require researchers to write substantial custom scripts to compute domain-specific cognitive indices such as frontal alpha asymmetry, theta/alpha engagement ratios, and multifractal complexity measures.

BrainSurf addresses this gap by offering a Python-based, extensible, and open-source library focused on meditation and cognitive EEG research. The package is suitable for:

- Neuroscientists investigating EEG correlates of meditation,
- Psychologists studying mindfulness and cognition,
- Machine learning practitioners building EEG-based classification models,
- Undergraduate and postgraduate students learning EEG signal processing.

# State of the Field

Meditation EEG studies typically rely on a mix of general-purpose preprocessing tools and researcher-written analysis code. Packages such as MNE-Python [@gramfort2013] and EEGLAB [@delorme2004] provide strong foundations for filtering, ICA-based artifact removal, and common EEG representations, but they do not bundle meditation-specific, cognition-oriented feature sets in a way that can be reused consistently across projects. In practice, researchers still need to implement custom workflows to compute cognitive indices (e.g., alpha asymmetry, engagement or relaxation ratios, and nonlinear complexity measures) and to adapt these computations to the particular structure of meditation recordings (pre/post comparisons and continuous resting-state segments).

This gap matters because small differences in preprocessing parameters, epoching choices, and feature definitions can materially affect reported effects. BrainSurf’s contribution is to package this domain-specific analysis logic into a focused Python library with a modular, reproducible API—so that labs can run comparable pipelines, more easily interpret outputs, and share code patterns rather than duplicating ad-hoc scripts.

# Software Design

## Build vs. Contribute Justification

MNE-Python [@gramfort2013] and EEGLAB [@delorme2004] are powerful and well-maintained, but contributing meditation-specific cognitive indices to these projects would have required substantial refactoring of their core data models, which are optimised for event-driven paradigms. BrainSurf was therefore created as a focused, standalone library rather than a downstream extension, allowing a simpler API tailored specifically to continuous resting-state and meditation recordings.

## Architecture and Design Trade-offs

BrainSurf is organised as a collection of loosely coupled modules—`preprocessing`, `analysis`, `visualization`, and `cognitive`—each importable independently:

```python
import brainsurf.data as data
import brainsurf.preprocessing as pre
import brainsurf.analysis as analysis
import brainsurf.visualization as vis
```

This flat, modular structure was preferred over a monolithic pipeline object to lower the barrier for beginners who need only a subset of functionality. The trade-off is that inter-module state (e.g., sampling frequency) must be passed explicitly, which adds verbosity but avoids hidden side effects.

Data are represented as NumPy arrays throughout, so BrainSurf outputs are immediately compatible with SciPy, Pandas, and MNE. ICA-based artifact removal delegates to MNE's built-in ICA implementation rather than a bespoke solver, keeping the core codebase lean. Nonlinear complexity analysis (e.g., Hurst exponent, DFA, multifractal measures) is provided via the `nolds` library, a deliberate choice to leverage a maintained specialist dependency rather than re-implementing these algorithms. File-format support (EDF, CSV, MFF, XLSX) was prioritised to accommodate the heterogeneous recording equipment common in university meditation laboratories—the MFF format in particular is the native format of EGI/Philips high-density EEG systems widely used in cognitive neuroscience.

# Functionality and Features

BrainSurf provides a complete EEG analysis workflow:

**Preprocessing**
- Common Average Referencing (CAR)
- High-pass and low-pass filtering
- Independent Component Analysis (ICA)-based artifact removal (via MNE)
- Epoch segmentation

**Analysis**
- Power Spectral Density (PSD) computation (Welch method)
- Band power estimation (alpha, beta, theta, gamma)
- Wavelet transforms
- Multifractal and nonlinear complexity analysis (via nolds)
- Coherence-based functional connectivity and inter-channel correlation

**Cognitive Indices**
- Indices for arousal, engagement, and relaxation states
- Pre- vs. post-meditation statistical comparison

**Visualization**
- Topographic mapping
- Power spectrum plots
- Heatmaps and correlation matrices

**Machine Learning**
- EEG classification using RNNs, LDA, or SVMs

# Example Usage

```python
import brainsurf.data as data
import brainsurf.preprocessing as pre
import brainsurf.analysis as analysis
import brainsurf.visualization as vis

# Load EEG data from file
eeg_data = data.read_edf_file('eeg_data.edf')

# Preprocess the data
preprocessed_data = pre.bandpass_filter(eeg_data, low_cutoff=1, high_cutoff=40)

# Compute power spectral density
freqs, psd = analysis.psd_welch(preprocessed_data, sampling_freq=256)

# Visualize results
vis.plot_power_spectrum(freqs, psd)
```

# Validation and Application

BrainSurf was validated using EEG datasets collected from guided meditation sessions involving 20 meditators and 11 non-meditators. Analysis using BrainSurf's preprocessing and spectral analysis pipeline showed a statistically significant increase in alpha and theta band power after meditation, consistent with enhanced relaxation and focus reported in the literature [@wahbeh2018; @hadli2020].

The Jupyter notebooks included in the repository (`demo.ipynb`, `brainSurf_Cognitive.ipynb`, `prePost.ipynb`, `med_nonmed.ipynb`) document this analysis end-to-end, from raw EEG loading through preprocessing and cognitive index extraction to visualisation, providing fully reproducible reference analyses.

# Research Impact Statement

BrainSurf addresses a practical gap in the meditation-neuroscience toolchain: the absence of a Python-native library that bundles domain-specific cognitive indices (frontal alpha asymmetry, engagement ratio, multifractal complexity) with standard EEG preprocessing in a single, pip-installable package. Existing general-purpose tools require researchers to assemble these indices from disparate custom scripts, increasing the risk of implementation inconsistency across studies.

The library has been validated on a real dataset of 31 participants (20 meditators, 11 non-meditators), with results consistent with established EEG literature on meditation. Community-readiness signals are in place: the software is publicly available on PyPI, distributed under the MIT License, and its source is openly hosted on GitHub. Multiple Jupyter notebooks serve as reproducible reference analyses, and contributions are accepted via GitHub issues and pull requests.

Near-term impact is anticipated in three areas. First, undergraduate and postgraduate laboratories studying contemplative neuroscience can adopt BrainSurf as a teaching tool, replacing ad-hoc scripts with a documented, version-controlled pipeline. Second, the machine learning module (supporting RNN, LDA, and SVM classifiers) provides a baseline classification workflow that future studies can benchmark against. Third, the multi-format file reader (EDF, CSV, MFF, XLSX) reduces the friction of pooling data across recording devices, a known bottleneck in multi-site meditation studies.

# AI Usage Disclosure

The authors did not use generative AI tools in the development of the BrainSurf software, the preparation of this manuscript, or the generation of documentation included in the repository.

# Acknowledgements

We thank **Prof. Rajeshwari K**, Department of Information Science and Engineering, BMS College of Engineering, for supervision and guidance during development. We also acknowledge contributors to the open-source EEG analysis community whose prior work inspired this project.

# References