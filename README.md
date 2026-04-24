# Advanced Time Series Modeling in Financial Econometrics

## Overview
This project presents applied solutions to three major challenges in financial time series modeling:

- Modeling Non-Stationarity and Equilibrium
- Handling Multicollinearity
- Feature Extraction

Using real-world macroeconomic and financial datasets, this project demonstrates econometric theory, model implementation, calibration, diagnostics, and deployment.

---
## Project Objectives

- Detect and model non-stationarity using cointegration and ECM
- Resolve multicollinearity through PCA
- Apply feature extraction for dimensionality reduction
- Build robust forecasting and decision-support models

---
## Methods Used

### Econometric Models
- Augmented Dickey-Fuller Test
- Johansen Cointegration Test
- Vector Error Correction Model (VECM)
- Principal Component Analysis (PCA)
- Factor Analysis

### Tools
- Python
- R
- SQL
- Jupyter Notebook

Libraries:
```python
pandas
numpy
statsmodels
scikit-learn
matplotlib
plotly
```

---
## Repository Structure

```bash
financial-time-series-modeling/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_nonstationarity.ipynb
│   ├── 02_multicollinearity.ipynb
│   └── 03_feature_extraction.ipynb
│
├── models/
│   ├── vecm_model.py
│   ├── pca_model.py
│   └── diagnostics.py
│
├── visuals/
├── report/
│   └── Final_Report.pdf
│
├── requirements.txt
└── README.md
```

---

## Key Results

| Challenge | Outcome |
|---------|---------|
| Non-stationarity | Equilibrium relationships identified |
| Multicollinearity | Stable predictors recovered |
| Feature Extraction | Reduced dimensionality with signal retained |

---

## Sample Equations

Error Correction Model:

```math
Δy_t = α + βΔx_t + γ(y_{t−1}−θx_{t−1}) + ε_t
```

Variance Inflation Factor:

```math
VIF_j = 1/(1-R_j^2)
```

PCA Transformation:

```math
Z = XW
```

---

## Applications
- Risk Management
- Portfolio Analytics
- Forecasting
- Financial Econometrics

---

## Author
Solomon Dejenie 
Quantitative Finance | Econometrics | Machine Learning
