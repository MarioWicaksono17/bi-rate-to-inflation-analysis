# Impact of BI Rate Changes on Inflation (2016–2025)

## 📌 Project Overview

This project analyzes the relationship between Indonesia’s policy interest rate (BI 7-Day Reverse Repo Rate) and inflation over the period 2016–2025.

The objective is to examine whether changes in the BI Rate influence inflation dynamics, particularly considering potential time-lag effects in monetary policy transmission.

The analysis combines time-series visualization, lagged correlation analysis, regression modeling, and Vector Autoregression (VAR).

---

## 🎯 Research Question

How do changes in the BI Rate affect inflation in Indonesia in the short to medium term?

---

## 🧠 Key Findings

- No strong contemporaneous correlation is observed between BI Rate and inflation.
- A stronger negative correlation emerges at a 3–4 month lag.
- The findings suggest a gradual transmission of monetary policy to inflation.

---

## 🛠 Tools & Technologies

- Python (Pandas, Statsmodels, Matplotlib)
- Power BI
- Jupyter Notebook
- Time-Series Analysis (Lag Regression, VAR, IRF)

---

## 📂 Project Structure

```
impact-bi-rate-inflation/
├── data/
│   ├── raw/
│   │   ├── BI-7Day-RR.xlsx
│   │   └── Data Inflasi.xlsx
│   └── processed/
│       ├── macro_monthly_clean.csv
│       ├── correlation_lag_table.csv
│       ├── regression_lag_coefficients.csv
│       ├── irf_values.csv
│       ├── var_forecast.csv
│       └── regression_model_summaries.txt
├── notebooks/
│   ├── 01_data_collection.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_exploratory_analysis.ipynb
│   ├── 04_correlation_lag_analysis.ipynb
│   ├── 05_regression_with_lag.ipynb
│   └── 06_var_model.ipynb
├── src/
│   ├── preprocessing.py
│   ├── eda.py
│   ├── stats_analysis.py
│   └── var_model.py
├── dashboard/
│   ├── power_bi/
│   │   └── dashboard.pbix
│   └── screenshots
│       └── dashboard_screenshots.png
├── reports/
│   ├── executive_summary.md
│   └── methodology.md
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run the Project

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
2. Run notebooks in order:
- 01_data_collection.ipynb
- 02_data_cleaning.ipynb
- 03_exploratory_analysis.ipynb
- 04_correlation_lag_analysis.ipynb
- 05_regression_with_lag.ipynb
- 06_var_model.ipynb
3. Open Power BI dashboard:
   ```bash
   dashboard/power_bi/test.pbix

---

## 📊 Dashboard Preview
![Dashboard Preview](dashboard/dashboard_screenshot.png)

---

## 📌 Notes

This project does not claim strict causality.  
Results are interpreted within the scope of correlation and time-series modeling.

## 👤 Author
Mario Suryowisnu Wicaksono | Jason Evan Hendarko

**LinkedIn:** 
*www.linkedin.com/in/marioswicaksono* | *www.linkedin.com/in/jason-evan-hendarko*
