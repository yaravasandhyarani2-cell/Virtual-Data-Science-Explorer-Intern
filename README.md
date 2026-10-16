# Subscription Customer Churn Prediction & Model Evaluation Plan

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-1.3%2B-orange.svg)](https://scikit-learn.org/)
[![Pandas](https://img.shields.io/badge/pandas-2.0%2B-150458.svg)](https://pandas.pydata.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688.svg)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/docker-ready-2496ED.svg)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

An enterprise-grade **Machine Learning Model Development and Evaluation Plan** engineered to predict customer churn in recurring subscription services. This repository details the end-to-end modeling blueprint—spanning problem formulation, leak-free preprocessing, candidate model benchmarking, threshold optimization, and containerized cloud deployment with drift monitoring.

---

## Table of Contents
1. [Business Problem & Financial Justification](#1-business-problem--financial-justification)
2. [Data Preprocessing & Feature Engineering Pipeline](#2-data-preprocessing--feature-engineering-pipeline)
3. [Model Architecture & Selection Rationale](#3-model-architecture--selection-rationale)
4. [Evaluation Metrics & Validation Strategy](#4-evaluation-metrics--validation-strategy)
5. [Conceptual Production Deployment & Drift Monitoring](#5-conceptual-production-deployment--drift-monitoring)
6. [Repository Structure](#6-repository-structure)
7. [Quick Start & Execution Steps](#7-quick-start--execution-steps)

---

## 1. Business Problem & Financial Justification

### 1.1 The Business Problem
Subscription-based businesses (SaaS, Streaming, Telecommunications) face constant attrition risks. Acquiring a new customer is estimated to be **5 to 7 times more expensive** than retaining an existing subscriber. 

Unmonitored churn erodes Monthly Recurring Revenue (MRR), degrades Customer Lifetime Value (CLV), and drives up marketing acquisition strain. Traditional retention programs act **reactively**—dispatching discounts only after cancellation tickets are opened or accounts go dark.

### 1.2 Predictive Formulation & Financial ROI
This project establishes a **supervised binary classification engine** that identifies at-risk subscribers **30 to 45 days prior to renewal**, enabling customer success desks to execute precision incentives and proactive onboarding check-ins.

#### Quantifiable Financial Model
- **Cohort Size:** 10,000 active subscribers
- **Average Revenue Per User (ARPU):** \$65 / month (\$780 / year)
- **Baseline Annual Churn Rate:** 24% (2,400 churned accounts/year)
- **Model-Assisted Retention:** Retaining just **15% of at-risk accounts** (360 accounts preserved) protects over **\$280,800 in Annual Recurring Revenue (ARR)**, against an operational retention cost of less than \$25,000.

---

## 2. Data Preprocessing & Feature Engineering Pipeline

To prevent data leakage and guarantee modular maintainability, preprocessing operations are orchestrated using `scikit-learn` `Pipeline` and `ColumnTransformer` primitives:

```
+--------------------------------------------------------------------------+
|                     RAW FEATURE VECTORS (40+ DIMENSIONS)                 |
+--------------------------------------------------------------------------+
                                     |
                                     v
+------------------------------------+-------------------------------------+
|                                    |                                     |
v                                    v                                     v
[ Continuous Telemetry ]             [ Nominal Attributes ]                [ Ordinal Attributes ]
  - Monthly Spend, Usage Hours         - Contract, Payment Method            - Tier, SLA Level
  - Inactivity Days, Ticket Volume     - Partner, Device Type                - Commitment Band
         |                                    |                                     |
         v                                    v                                     v
[ SimpleImputer(median) ]            [ SimpleImputer(constant='Unknown') ] [ SimpleImputer(most_frequent) ]
         |                                    |                                     |
         v                                    v                                     v
[ Feature Engineering ]              [ OneHotEncoder(drop='first') ]       [ OrdinalEncoder ]
  - Spend / Tenure Ratio                              |                                     |
  - Ticket Frequency Intensity                        |                                     |
         |                                            |                                     |
         v                                            |                                     |
[ RobustScaler ]                                      |                                     |
         |                                            |                                     |
         +------------------------------------+-------+-------------------------------------+
                                              |
                                              v
                              [ Transformed Feature Matrix ]
                              (Leak-Free Fitted on X_train only)
```

### Pipeline Key Elements:
1. **Missing Data Imputation:**
   - *Continuous:* `SimpleImputer(strategy='median')` to resist heavy tails and sensor spikes.
   - *Categorical:* Constant imputation (`'Unknown'`) to preserve informative missingness signals.
2. **Feature Engineering:**
   - *Spend-to-Tenure Ratio:* $\text{AvgSpend} = \frac{\text{TotalCharges}}{\text{TenureMonths} + 1}$
   - *Support Friction Index:* $\text{SupportIntensity} = \frac{\text{EscalatedTickets}}{\text{TenureMonths} + 1}$
3. **Scaling & Encoding:**
   - *Numeric Features:* `RobustScaler` scales based on interquartile ranges, protecting estimators from extreme usage outliers.
   - *Categorical Features:* `OneHotEncoder(drop='first', sparse_output=False, handle_unknown='ignore')`.

---

## 3. Model Architecture & Selection Rationale

Three distinct model families are systematically evaluated to establish an empirical performance curve:

```
+------------------------------------------------------------------------------+
|                              MODEL COMPARISON                                |
+--------------------------+-----------------------+---------------------------+
| 1. Logistic Regression   | 2. Decision Trees     | 3. Random Forest (Target) |
|    (Baseline Benchmark)  |    (Single Tree)      |    (Production Choice)    |
| - Fast & linear          | - Non-linear rules    | - Ensemble Bagging        |
| - Odds-ratio visibility  | - High variance       | - Variance reduction      |
| - High bias boundary     | - Prone to overfit    | - Superior ROC/PR-AUC     |
+--------------------------+-----------------------+---------------------------+
```

### Architectural Comparison Matrix

| Evaluation Dimension | Logistic Regression (Baseline) | Decision Tree Classifier | Random Forest Classifier (Selected) |
| :--- | :--- | :--- | :--- |
| **Model Type** | Generalized Linear Model (GLM) | Single Non-Parametric Tree | Bagged Ensemble of De-correlated Trees |
| **Complexity & Non-Linearity** | Low (Linear decision boundaries) | High (Step-function boundaries) | Very High (Smooth non-linear surfaces) |
| **Risk of Overfitting** | Very Low ($L_1 / L_2$ penalized) | High (Memorizes training noise) | Low (Averaging across bootstrapped trees) |
| **Interpretability** | Global odds-ratio coefficients | Direct conditional flowcharts | Permutation Feature Importance & SHAP |
| **Expected PR-AUC** | $\approx 0.52 - 0.58$ | $\approx 0.50 - 0.55$ | **$\ge 0.65 - 0.72$** |
| **Target Decision Rationale** | Essential benchmark for baseline comparison. | Useful educational baseline; rejected due to high variance. | **Primary production selection:** Delivers robust generalization on imbalanced tabular data. |

---

## 4. Evaluation Metrics & Validation Strategy

### 4.1 Evaluation Metric Hierarchy
Due to typical class imbalance in subscription churn ($75-80\%$ retained vs. $20-25\%$ churned), raw accuracy is explicitly rejected as a primary performance metric:

- **Primary Metrics:**
  - **PR-AUC (Average Precision):** Directly benchmarks precision-recall trade-offs on the minority churn class.
  - **ROC-AUC:** Measures global discrimination capability across all probability thresholds (Target: $\ge 0.85$).
  - **Recall at Top 20% Decile:** Measures operational capture rate—ensuring that at least **$70\%$ of all future churners** appear within the highest-risk quintile.
- **Secondary Metrics:**
  - Precision, Recall, and F1-macro score.

### 4.2 Cross-Validation Protocol
- **5-Fold Stratified K-Fold Cross-Validation:** Folds are partitioned such that the exact churn percentage is maintained consistently across each training and validation fold.
- **Leakage Elimination:** Transformations (`ColumnTransformer`) are embedded inside the `scikit-learn` `Pipeline` so that encodings and scalings are fitted strictly on the $4$ training folds and applied out-of-fold to the validation fold.

### 4.3 Cost-Utility Threshold Optimization
Rather than using an arbitrary default probability threshold ($p = 0.5$), the decision threshold $p^*$ is optimized against an empirical cost matrix:
$$\text{Cost}(p) = C_{\text{FN}} \cdot \text{FN}(p) + C_{\text{FP}} \cdot \text{FP}(p)$$
- Where $C_{\text{FN}} = \$500$ (lost customer lifetime value) and $C_{\text{FP}} = \$35$ (cost of customer success incentive offer).
- Optimal threshold shifts to **$p^* \approx 0.32 - 0.40$**, substantially driving operational recall.

---

## 5. Conceptual Production Deployment & Drift Monitoring

```
+--------------------------------------------------------------------------+
|                     PRODUCTION SERVING ARCHITECTURE                      |
+--------------------------------------------------------------------------+
|  [ CRM / Client App ] ---> [ FastAPI Microservice (Dockerized REST) ]    |
|                                       |                                  |
|                                       v                                  |
|                        [ In-Memory Pipeline (Joblib) ]                   |
|                        - Preprocessing Transformer                       |
|                        - Calibrated Random Forest Model                  |
|                                       |                                  |
|                                       v                                  |
|               [ Inference Response: Churn Prob + Top 3 SHAP Drivers ]    |
+--------------------------------------------------------------------------+
                                        |
                                        v
+--------------------------------------------------------------------------+
|                     LIFECYCLE & DRIFT MONITORING                         |
|  - Feature Drift: Population Stability Index (PSI > 0.25 flags alert)    |
|  - Data Distribution Drift: Kolmogorov-Smirnov (KS) hypothesis tests     |
|  - Automated Retraining: Scheduled bi-monthly + shadow model validation  |
+--------------------------------------------------------------------------+
```

### 5.1 Containerized REST API (FastAPI + Docker)
- **Serialization:** Full pipelines are packaged into a hermetic artifact using `joblib.dump(pipeline, 'churn_model_v1.joblib')`.
- **FastAPI Endpoint:** Exposes a `/predict` REST route taking customer telemetry JSON and returning:
  - Churn Probability ($p$) and Binary Risk Classification ($0/1$).
  - Top 3 localized risk drivers derived from SHAP attribution (e.g., steep login drop, high ticketing friction).
- **Latency SLA:** Sub-$50\text{ ms}$ response time per customer record.

### 5.2 Drift Detection & Continuous Maintenance
1. **Feature & Data Drift:** Monitored using the **Population Stability Index (PSI)** and two-sample Kolmogorov-Smirnov (KS) tests comparing production inference batches against baseline training data.
2. **Concept Drift:** Tracking realized churn rates vs. predicted risk bins over rolling 60-day windows.
3. **Champion-Challenger Shadowing:** Retrained candidate models run in shadow mode for 14 days before automated production promotion.

---

## 6. Repository Structure

```text
├── README.md                          # Week 3: Master ML Model Development & Evaluation Plan
├── PROJECT_PLAN_AND_STRATEGY.md       # Week 1: Project Planning & Strategic Architecture
├── EDA_VISUALIZATION_FRAMEWORK.md     # Week 2: Exploratory Data Analysis & Visualization Blueprint
├── ML_MODEL_DEVELOPMENT_PLAN.md       # Week 3: Comprehensive ML Model Development Specification
├── train_model.py                     # Pipeline execution: Preprocessing, Training, CV & Evaluation
├── eda_pipeline.py                    # Exploratory Data Analysis & Quality Audit script
├── requirements.txt                   # Production environment dependencies
└── .gitignore                         # Git tracking exclusions
```

---

## 7. Quick Start & Execution Steps

### 1. Environment Setup
```bash
# Clone the repository
git clone https://github.com/yaravasandhyarani2-cell/Virtual-Data-Science-Explorer-Intern.git
cd Virtual-Data-Science-Explorer-Intern

# Create and activate virtual environment
python -m venv venv
# On Windows:
.\venv\Scripts\Activate.ps1
# On Linux/macOS:
source venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

### 2. Run the Machine Learning Pipeline
Execute model training, 5-fold cross-validation, and performance evaluation:
```bash
python train_model.py
```

### 3. Run the Exploratory Data Analysis Suite
Execute the data hygiene and outlier detection pipeline:
```bash
python eda_pipeline.py
```

---

## License & Attribution
Distributed under the MIT License. Developed as part of the **Virtual Data Science Explorer Internship** curriculum.
