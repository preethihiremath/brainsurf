---
title: "BrainSurf: An Open-Source Python Library for EEG Signal Analysis in Meditation Research"
tags:
  - Python
  - EEG
  - Meditation
  - Neuroscience
  - Signal Processing
authors:
  - name: Preethi V Hiremath
    affiliation: 1
    orcid: 0009-0002-8984-3049
  - name: Rakshitha B R
    affiliation: 1
  - name: Rashi Prasad
    affiliation: 1
affiliations:
  - name: Department of Information Science and Engineering, BMS College of Engineering, Bengaluru, India
    index: 1
date: 2025-10-26
bibliography: paper.bib
---

# Summary

**BrainSurf** is an open-source Python library developed for preprocessing, feature extraction, and statistical analysis of EEG (Electroencephalography) signals. It simplifies EEG workflows for meditation-based cognitive neuroscience studies, offering accessible tools for cleaning, analyzing, and visualizing EEG data. BrainSurf provides predefined functions for high-pass and low-pass filtering, artifact removal using ICA, epoching, power spectral analysis, and inter-channel connectivity computation. 

The library was developed to support EEG-based meditation research, where neural patterns before and after meditative states are studied for their cognitive implications. BrainSurf enables reproducible EEG analysis through an intuitive API and modular design, empowering researchers to efficiently process large EEG datasets and extract meaningful cognitive features.

# Statement of Need

EEG analysis is critical in understanding how meditation alters cognitive states such as attention, relaxation, and emotional balance. However, existing EEG software often requires steep learning curves, lacks transparency, or is closed-source. BrainSurf addresses this gap by offering a Python-based, extensible, and open-source alternative focused on meditation and cognitive EEG research. 

The package is suitable for:
- Neuroscientists investigating EEG correlates of meditation,
- Psychologists studying mindfulness and cognition,
- Machine learning practitioners building EEG-based classification models.

# Functionality and Features

BrainSurf provides a complete EEG analysis workflow:

- **Preprocessing**  
  - Common Average Referencing (CAR)  
  - High-pass and low-pass filtering  
  - Independent Component Analysis (ICA)-based artifact removal  

- **Feature Extraction**  
  - Power Spectral Density (PSD) computation  
  - Band power estimation (alpha, beta, theta, gamma)  
  - Functional connectivity and inter-channel correlation analysis  

- **Utilities**  
  - Epoching and reshaping of EEG data  
  - Statistical analysis of pre- vs. post-meditation signals  
  - Visualization of spectral and correlation matrices  

# Example Usage

```python
from brainsurf import preprocess, extract_features

# Preprocess EEG data
data = preprocess("subject01.edf", highpass=1, lowpass=40)

# Extract frequency features
features = extract_features(data, bands=['alpha', 'theta', 'beta'])
print(features.summary())
```

# Validation and Application
BrainSurf was validated using EEG datasets collected from guided meditation sessions involving 20 meditators and 11 non-meditators. Analysis showed an increase in alpha and theta power after meditation, consistent with enhanced relaxation and focus reported in the literature.  

By integrating preprocessing, analysis, and visualization in one framework, BrainSurf simplifies complex EEG workflows and enables reproducible cognitive neuroscience research.

# Installation
BrainSurf is available on **PyPI** and can be installed via: pip install brainsurf

Source code and documentation are hosted on GitHub: [https://github.com/preethihiremath/brainsurf](https://github.com/preethihiremath/brainsurf)

# Availability and Reuse Potential
BrainSurf is distributed under the **MIT License**. Contributions are welcome through issues and pull requests. The modular design allows researchers to extend it with new algorithms, preprocessing techniques, or visualization methods.

# Acknowledgements
We thank **Prof. Rajeshwari K**, Department of Information Science and Engineering, BMS College of Engineering, for supervision and guidance during development.  
We also acknowledge contributors to the open-source EEG analysis community whose prior work inspired this project.

# References
- Swati Singh, Vinay Gupta, Laxmidhar Behera. *"Meditation and Cognitive Enhancement: A Machine Learning-Based Classification Using EEG."* Cognitive Neurodynamics, 2022.  
- Mallikarjun A. Hadli, Nikith K. Kottary, Shwetha Baliga. *"Detection and Analysis of EEG Signals Before and After Meditation."* International Journal of Engineering Research, 2020.  
- Helané Wahbeh, Amira Sagher, Frederick Travis. *"A Systematic Review of Transcendent States Across Meditation and Contemplative Traditions."* Frontiers in Human Neuroscience, 2018.