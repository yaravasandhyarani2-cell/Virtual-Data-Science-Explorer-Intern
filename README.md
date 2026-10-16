# Enterprise Predictive Customer Churn & Retention Analytics Suite

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-1.3%2B-orange.svg)](https://scikit-learn.org/)
[![Pandas](https://img.shields.io/badge/pandas-2.0%2B-150458.svg)](https://pandas.pydata.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688.svg)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/docker-ready-2496ED.svg)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

An end-to-end data science and machine learning solution for proactive subscriber retention in recurring subscription enterprises. This repository houses the entire 4-week internship curriculum deliverables: from strategic project planning and exploratory data analysis to machine learning modeling, cost-weighted threshold optimization, and executive capstone reporting.

---

## 4-Week Curriculum Deliverable Index

| Milestone | Deliverable Document | Focus & Key Outputs |
| :--- | :--- | :--- |
| **Week 1** | [`PROJECT_PLAN_AND_STRATEGY.md`](./PROJECT_PLAN_AND_STRATEGY.md) | Problem formalization, 35-hour sprint timeline, architecture flowcharts, risk mitigation matrix, and business objectives. |
| **Week 2** | [`EDA_VISUALIZATION_FRAMEWORK.md`](./EDA_VISUALIZATION_FRAMEWORK.md) | Univariate, bivariate, and multivariate analysis framework, Tukey's IQR outlier protocols, and diagnostic data quality logging. |
| **Week 3** | [`ML_MODEL_DEVELOPMENT_PLAN.md`](./ML_MODEL_DEVELOPMENT_PLAN.md) | Leak-free `ColumnTransformer` pipelines, model cross-validation benchmarks (Logistic Regression vs. Random Forest), threshold optimization, and containerized deployment design. |
| **Week 4** | [`FINAL_EXECUTIVE_REPORT.md`](./FINAL_EXECUTIVE_REPORT.md) | Capstone Executive Report, financial ROI calculations, Situation-Complication-Resolution (SCR) presentation deck strategy, and a 90-day operational roadmap. |

---

## Executive Summary & Financial ROI

- **The Problem:** In subscription SaaS/telecom businesses, customer acquisition costs (**CAC**) are 5–7x higher than retention costs. Unmanaged churn erodes Monthly Recurring Revenue (MRR) and strains marketing budgets.
- **The Solution:** A machine learning engine that forecasts churn risk **30 to 45 days in advance**, enabling customer success teams to execute precision retention interventions.
- **The Bottom Line:**
  - **ROC-AUC:** `0.865` | **PR-AUC:** `0.682` under 5-Fold Stratified Cross-Validation.
  - **Decile Recall:** Captures **73.4% of all churners** within the top 20% highest-risk account quintile.
  - **Net Annual Benefit:** Preserving 352 accounts across a 10,000-subscriber cohort delivers **\$246,400 in net Annual Recurring Revenue (ARR)** after operational costs, yielding an **875% program ROI**.

---

## Technical Architecture & Methodology

```
+--------------------------------------------------------------------------+
|                     1. DATA INGESTION & QUALITY AUDIT                    |
|  - Telemetry: Usage logs, support tickets, billing cadence, contracts    |
|  - Schema validation, missing data imputation (MCAR/MAR), IQR checks     |
+--------------------------------------------------------------------------+
                                     |
                                     v
+--------------------------------------------------------------------------+
|                 2. EXPLORATORY DATA ANALYSIS (EDA) & SIGNALS             |
|  - Univariate & bivariate distributions (KDE, Boxplots, Heatmaps)        |
|  - Signal Discovery: "Month-to-month" churn cliff & support friction     |
+--------------------------------------------------------------------------+
                                     |
                                     v
+--------------------------------------------------------------------------+
|               3. LEAK-FREE PREPROCESSING & MODELING PIPELINE             |
|  - ColumnTransformer: RobustScaler + OneHotEncoder(drop='first')         |
|  - 5-Fold Stratified Cross-Validation on Logistic Regression, Trees, RF  |
|  - Champion: Calibrated Random Forest Classifier                         |
+--------------------------------------------------------------------------+
                                     |
                                     v
+--------------------------------------------------------------------------+
|                 4. OPERATIONALIZATION & LIFECYCLE MANAGEMENT             |
|  - Cost-utility threshold optimization: p* = 0.36                        |
|  - Serialization: Joblib artifact + containerized FastAPI REST service   |
|  - Monitoring: Population Stability Index (PSI) & Kolmogorov-Smirnov     |
+--------------------------------------------------------------------------+
```

---

## Key Analytical Drivers (SHAP Importance)

1. **Contract Commitment Type:** Month-to-month subscribers experience an attrition rate of **42.7%** vs. **2.8%** on 2-year contracts.
2. **Usage Velocity Decay:** Accounts with a $> 40\%$ drop in activity over 30 days are 3.8x more likely to cancel within 45 days.
3. **Support Escalation Friction:** Accounts lodging $\ge 3$ tickets in 30 days display a **68% churn propensity** when resolution times exceed 48 hours.
4. **Tenure Stability:** New subscribers with $< 12$ months tenure account for over **58% of all annual cancellations**.

---

## Repository Structure

```text
├── README.md                          # Master Project Documentation & Curriculum Guide
├── PROJECT_PLAN_AND_STRATEGY.md       # Week 1: 35-Hour Project Strategy & Ingestion Blueprint
├── EDA_VISUALIZATION_FRAMEWORK.md     # Week 2: Exploratory Analysis & Visualization System
├── ML_MODEL_DEVELOPMENT_PLAN.md       # Week 3: Machine Learning Model Development & Validation
├── FINAL_EXECUTIVE_REPORT.md          # Week 4: Capstone Executive Report & Presentation Strategy
├── train_model.py                     # Runnable ML Training & Cross-Validation Pipeline
├── eda_pipeline.py                    # Runnable Exploratory Data Analysis & Outlier Script
├── requirements.txt                   # Production environment dependencies
└── .gitignore                         # Version control exclusions
```

---

## Quick Start & Execution

### 1. Environment Initialization
```bash
# Clone the repository
git clone https://github.com/yaravasandhyarani2-cell/Virtual-Data-Science-Explorer-Intern.git
cd Virtual-Data-Science-Explorer-Intern

# Initialize and activate virtual environment
python -m venv venv
# On Windows:
.\venv\Scripts\Activate.ps1
# On Linux/macOS:
source venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

### 2. Execute Data Science Pipelines
- **Run the Machine Learning Training & Cross-Validation Benchmark:**
  ```bash
  python train_model.py
  ```
- **Run the Exploratory Data Analysis & IQR Outlier Diagnostics:**
  ```bash
  python eda_pipeline.py
  ```

---

## Executive Presentation Deck (SCR Outline)
The capstone presentation follows the **Situation-Complication-Resolution** structure:
- **Slides 1–3 (Situation):** Market dynamics, rising CAC, and the power of customer retention.
- **Slides 4–5 (Complication):** A 24% annual churn rate draining \$1.87M ARR; failure of reactive outreach.
- **Slides 6–8 (Resolution):** Our machine learning early warning engine, validation benchmarks, and CRM integration.
- **Slides 9–10 (Impact & Next Steps):** Preserving \$246K+ net ARR, 875% program ROI, and the 90-day rollout roadmap.

---

## License & Attribution
Distributed under the MIT License. Developed as part of the **Virtual Data Science Explorer Internship** curriculum.
