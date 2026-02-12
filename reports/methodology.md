# Methodology

## 1. Data Source

- BI 7-Day Reverse Repo Rate (Bank Indonesia)
- Monthly Inflation Data (Bank Indonesia)

Period: April 2016 – December 2025  
Frequency: Monthly

---

## 2. Data Cleaning

- Standardized date formats
- Converted percentage strings to numeric values
- Aligned data by month and year
- Merged BI Rate and inflation datasets
- Removed missing observations

---

## 3. Exploratory Analysis

- Time-series visualization
- Moving average smoothing (6-month window)
- Visual inspection of trend dynamics

---

## 4. Lagged Correlation Analysis

Correlation was computed between:

Inflationₜ and BI Rateₜ₋ₖ

Where lag (k) ranges from 0 to 4 months.

This step identifies potential delayed relationships.

---

## 5. Regression with Lag

For each lag (k), the following model was estimated:

Inflationₜ = α + β × BI Rateₜ₋ₖ + εₜ

Ordinary Least Squares (OLS) regression was applied.

Model diagnostics were evaluated using:
- R-squared
- t-statistics
- p-values
- Durbin-Watson statistic

---

## 6. Vector Autoregression (VAR)

A VAR model was implemented to capture dynamic interactions between BI Rate and inflation.

Steps:
- Stationarity check
- First differencing
- Optimal lag selection
- Impulse Response Function (IRF) analysis

The IRF analysis examined how inflation responds over time to shocks in the BI Rate.

---

## Assumptions

- Linearity
- Stationarity (after differencing for VAR)
- No omitted structural breaks

---

## Limitations

- The model does not include additional macroeconomic controls.
- Structural causal inference is not performed.
- Results are interpreted as dynamic association, not definitive causality.