# Machine Learning Model Development & Evaluation Plan

**Role:** Senior Machine Learning Architect & Data Scientist  
**Deliverable:** Week 3 Strategic Blueprint — End-to-End ML System Specification  
**Project Context:** Enterprise Predictive Churn & Retention Classification System  
**Estimated Project Scope:** 30–35 Hours Operational Execution Equivalent  
**Target Environment:** Python 3.10+ / Scikit-Learn, XGBoost/LightGBM, Joblib, Docker

---

## 1. Problem Definition, Justification, & Strategic Relevance

### 1.1 Problem Statement
The enterprise operates a multi-tier SaaS / subscription platform with an observed annual customer churn rate of **24%**. A significant portion of churned accounts disengage gradually over a 60–90 day window prior to cancellation, leaving subtle behavioral signatures in usage logs, telemetry, and billing events.

The core objective is to build a **supervised binary classification engine** that predicts whether an active customer will churn ($y=1$) or remain retained ($y=0$) within the upcoming 45-day contract window.

### 1.2 Justification for Machine Learning
- **Limitations of Rule-Based Heuristics:** Traditional rule-based alerts (e.g., `"ticket_count > 3"` or `"login_count == 0 for 14 days"`) produce excessive false alarms and fail to capture non-linear, multi-factorial patterns (e.g., high-tenure customers with declining usage vs. new customers experiencing onboarding friction).
- **Scale and High-Dimensional Interactivity:** Customer engagement data spans 40+ dynamic attributes across demographic, usage telemetry, billing cadence, and support ticket interactions. Supervised machine learning algorithms are uniquely suited to uncover hidden non-linear relationships across these multi-modal feature vectors.

### 1.3 Strategic Business Relevance & Target Objectives
- **Target Performance Benchmarks:**
  - **ROC-AUC $\ge 0.85$**
  - **Precision-Recall AUC (PR-AUC) $\ge 0.65$**
  - **Top-Decile Recall $\ge 70\%$** (identifying $>70\%$ of all future churners within the top 20% highest risk segment).
- **Economic Value Proposition:** Enabling the customer success team to deploy proactive, tiered interventions (retention offers, concierge onboarding, executive sponsor calls) saving an estimated **$150,000+ in annual recurring revenue (ARR)** per 10,000 subscribers.

---

## 2. Data Preprocessing, Normalization, & Feature Engineering Pipeline

### 2.1 Data Hygiene & Cleansing Protocols
1. **Missing Data Imputation:**
   - *Continuous Features:* Median imputation via `SimpleImputer(strategy='median')` to maintain robustness against skewed usage metrics.
   - *Categorical Features:* Constant imputation (`SimpleImputer(strategy='constant', fill_value='Unknown')`) preserving potential informative missingness.
2. **Type Coercion & String Sanitization:**
   - Stripping whitespace and standardizing categorical strings to lowercase.
   - Forcing numeric type conversions on dirty numeric fields (e.g., `pd.to_numeric(errors='coerce')` for total charges).
3. **Outlier Mitigation:**
   - Capping extreme numeric distributions at the 99th percentile (winsorization) to protect linear baselines and distance-sensitive models without losing high-value account records.

### 2.2 Feature Engineering & Domain Synthesis
Raw features are transformed into high-signal behavioral indicators:
- **Usage Velocity / Deceleration:**
  $$\text{UsageVelocity} = \frac{\text{Usage}_{\text{Last 30 Days}}}{\text{Usage}_{\text{Prior 60 Days}} + 1}$$
  *(A ratio $< 0.5$ signals severe drop-off in product engagement).*
- **Spend-to-Tenure Ratio:**
  $$\text{AverageMonthlySpend} = \frac{\text{TotalCharges}}{\text{TenureMonths} + 1}$$
- **Support Burden Index:**
  $$\text{SupportIntensity} = \frac{\text{EscalatedTickets}}{\text{TenureMonths} + 1}$$
- **Contract Risk Indicator:** Binary flags capturing month-to-month contracts vs. annual/multi-year commitments.

### 2.3 Feature Transformation & Normalization
Encapsulated strictly within a `scikit-learn` `ColumnTransformer`:
- **Continuous Features:** Scaled using `RobustScaler` (resistant to outliers by utilizing interquartile ranges) or `StandardScaler`.
- **Nominal Categorical Features:** Transformed using `OneHotEncoder(drop='first', sparse_output=False, handle_unknown='ignore')`.
- **Ordinal Categorical Features:** Transformed using `OrdinalEncoder` with explicitly ordered category hierarchies.

### 2.4 Preprocessing Challenges & Mitigation Safeguards

| Challenge | Risk | Mitigation Safeguard |
| :--- | :--- | :--- |
| **Data Leakage** | Optimistic cross-validation scores failing in production | Encapsulate all transformations inside `sklearn.pipeline.Pipeline`. Encoders and scalers are strictly fitted on training folds (`fit_transform`) and applied out-of-fold (`transform`). |
| **Class Imbalance** | Model biases toward predicting majority class ($y=0$) | Apply cost-sensitive loss weighting (`class_weight='balanced'`) during estimator optimization; avoid synthetic oversampling (SMOTE) before pipeline splitting. |
| **Multicollinearity** | Inflated variance in linear baseline estimators | Calculate Variance Inflation Factor (VIF); drop redundant linear pairings (e.g., `TenureMonths` $\times$ `MonthlyCharges` $\approx$ `TotalCharges`). |

---

## 3. End-to-End Machine Learning System Architecture & Workflow

```
+--------------------------------------------------------------------------+
|                          1. INGESTION & SPLITTING                        |
|  - Raw Ingestion: Telemetry, Billing, Support & Profile Data             |
|  - Stratified 80/20 Train-Test Split (Target-Preserving, Seed = 42)      |
+--------------------------------------------------------------------------+
                                     |
                                     v
+--------------------------------------------------------------------------+
|                     2. FEATURE PIPELINE (ColumnTransformer)              |
|  - Numeric Branch: Median Imputer -> Feature Ratios -> RobustScaler      |
|  - Categorical Branch: Mode Imputer -> OneHotEncoder (handle_unknown)    |
+--------------------------------------------------------------------------+
                                     |
                                     v
+--------------------------------------------------------------------------+
|               3. CANDIDATE MODEL EVALUATION & CROSS-VALIDATION           |
|  - 5-Fold Stratified K-Fold Cross-Validation                             |
|  - Baseline: Logistic Regression (L1/L2 ElasticNet Penalties)            |
|  - Non-Linear: Random Forest Classifier (Sub-sampling, Gini/Entropy)     |
|  - Gradient Boosting: HistGradientBoosting / XGBoost / LightGBM          |
+--------------------------------------------------------------------------+
                                     |
                                     v
+--------------------------------------------------------------------------+
|                  4. HYPERPARAMETER TUNING & THRESHOLD OPTIMIZATION       |
|  - RandomizedSearchCV / Bayesian Optimization (PR-AUC objective)         |
|  - Cost-Utility Matrix Curve Analysis (Threshold optimization: e.g., 0.38)|
+--------------------------------------------------------------------------+
                                     |
                                     v
+--------------------------------------------------------------------------+
|             5. FINAL HOLDOUT VALIDATION & PRODUCTION PACKAGING           |
|  - Unseen Test Holdout Scoring (ROC-AUC, PR-AUC, Confusion Matrix)       |
|  - Global & Local Explainability (Permutation / SHAP Importance)         |
|  - Serialized Artifact (`model_pipeline.joblib`) + Dockerized Endpoint   |
+--------------------------------------------------------------------------+
```

---

## 4. Model Selection, Training Pipelines, & Hyperparameter Optimization

### 4.1 Candidate Model Taxonomy & Architectural Trade-offs

1. **Baseline Model: Regularized Logistic Regression**
   - *Rationale:* Provides an essential linear benchmark, highly interpretable odds-ratio coefficients, rapid training, and well-calibrated probabilistic outputs.
   - *Hyperparameters:* Regularization parameter $C \in [10^{-3}, 10^2]$, penalty $\in \{\ell_1, \ell_2, \text{ElasticNet}\}$.
2. **Ensemble Model: Random Forest Classifier (`RandomForestClassifier`)**
   - *Rationale:* Captures non-linear feature interactions and high-order feature thresholds without requiring monotonic relationships; highly resilient to over-fitting through bagging.
   - *Hyperparameters:* `n_estimators`, `max_depth`, `min_samples_split`, `min_samples_leaf`, `max_features='sqrt'`.
3. **Advanced Gradient Boosting: Gradient Boosted Trees (`HistGradientBoostingClassifier` / `XGBoost`)**
   - *Rationale:* State-of-the-art predictive performance on tabular data; sequential gradient error-correction excels at capturing subtle predictive signals in imbalanced datasets.
   - *Hyperparameters:* `learning_rate` ($\eta$), `max_iter`, `max_leaf_nodes`, `l2_regularization`, `min_samples_leaf`.

### 4.2 Training Strategy & Cross-Validation Protocol
- **Stratified 5-Fold Cross-Validation:** Preserves the 24% churn proportion identically across each training and validation fold.
- **Nested Cross-Validation:** Outer loop (5 folds) estimates true generalization error; inner loop (3 folds) drives hyperparameter selection to eliminate selection bias.

### 4.3 Hyperparameter Tuning Methodology
- **Coarse-to-Fine Search:**
  - *Stage 1:* `RandomizedSearchCV` across a broad parameter grid (100 iterations) targeting maximal **PR-AUC**.
  - *Stage 2:* `GridSearchCV` focused on tight bounds surrounding the optimal hyperparameter basin.
- **Scoring Function:** Scored strictly on `average_precision` (PR-AUC) rather than accuracy or ROC-AUC to prioritize precision in the minority churn class.

---

## 5. Performance Evaluation Metrics & Validation Strategy

### 5.1 Metric Selection & Justification

| Metric | Business & Technical Rationale | Priority |
| :--- | :--- | :---: |
| **PR-AUC (Average Precision)** | Evaluates the tradeoff between precision and recall across all thresholds specifically for the minority class without being inflated by true negatives. | **Primary** |
| **ROC-AUC** | Quantifies the model's global ability to rank a random churner higher than a random non-churner across all possible operating thresholds. | **Primary** |
| **Recall at Top 20% Decile** | Represents operational capacity: Customer success teams can only contact the top 20% highest-risk customers per month; this metric measures what % of all churners are captured within that cohort. | **Primary Business KPI** |
| **Cost-Weighted Loss** | $\text{Cost} = (C_{\text{FN}} \times \text{FN}) + (C_{\text{FP}} \times \text{FP})$, where $C_{\text{FN}} = \$500$ (lost customer) and $C_{\text{FP}} = \$35$ (cost of incentive offer). | **Decision Threshold Metric** |
| **F1-Score / Accuracy** | Accuracy is explicitly rejected as a primary metric due to class imbalance vulnerability. F1-score is tracked as a harmonic reference. | **Secondary** |

### 5.2 Operating Threshold Tuning
Default classification thresholds ($p = 0.5$) are inherently sub-optimal when misclassification costs are asymmetric.
- The optimal threshold $p^*$ is derived empirically by plotting the **Total Cost Curve** across candidate thresholds $p \in [0.05, 0.95]$:
  $$p^* = \arg\min_p \left( C_{\text{FN}} \cdot \text{FN}(p) + C_{\text{FP}} \cdot \text{FP}(p) \right)$$
- Typical optimal thresholds in churn domains shift between **$0.30$ and $0.42$**, significantly boosting operational recall without excessive incentive waste.

---

## 6. Model Interpretability & Explainability Framework

To achieve operational buy-in from business stakeholders and customer success representatives:
1. **Global Interpretability:**
   - **Permutation Feature Importance:** Measures the drop in PR-AUC when individual features are randomly permuted, isolating the genuine global drivers of churn.
2. **Local Instance-Level Interpretability:**
   - **SHAP (SHapley Additive exPlanations):** For each customer flagged at risk, produce top 3 contributing factors (e.g., `+0.22 churn probability due to Month-to-Month Contract`, `+0.18 due to 65% drop in login activity`, `-0.08 due to 3-year tenure`).
   - Customer success dashboards display these top 3 drivers alongside customer contact cards to tailor retention conversations.

---

## 7. Model Deployment, Monitoring, & Lifecycle Maintenance

### 7.1 Serving Architecture & Deployment Pipeline
- **Packaging:** The finalized preprocessing transformer and tuned estimator are serialized into a single hermetic artifact using `joblib.dump(pipeline, 'churn_pipeline_v1.joblib')`.
- **Inference Service:**
  - *Batch Scoring Mode:* A scheduled daily/weekly batch scoring job runs on the customer database, writing churn probabilities and risk deciles directly into the Customer Relationship Management (CRM) platform.
  - *Real-Time Microservice Mode:* A lightweight FastAPI endpoint containerized via Docker exposes a `/predict` REST route responding within $< 50\text{ ms}$.

### 7.2 Post-Deployment Monitoring Protocols

```
+--------------------------------------------------------------------------+
|                      PRODUCTION MONITORING ENGINE                        |
+--------------------------------------------------------------------------+
| 1. Data & Feature Drift (Drift Detector):                                |
|    - Population Stability Index (PSI > 0.25 indicates significant shift) |
|    - Kolmogorov-Smirnov (KS) test comparing inference vs. training data  |
+--------------------------------------------------------------------------+
| 2. Concept Drift & Target Monitoring:                                    |
|    - Track actual realized churn rates vs. predicted probability buckets |
|    - Calibration curves (Brier score tracking)                           |
+--------------------------------------------------------------------------+
| 3. System Health & Operational SLAs:                                     |
|    - Latency (p95 < 100ms), error rates (< 0.01%), CPU/Memory footprint   |
+--------------------------------------------------------------------------+
```

### 7.3 Model Retraining & Continuous Maintenance Lifecycle
1. **Trigger Conditions:**
   - **Scheduled Retraining:** Bi-monthly cadenced retraining incorporating the latest 60 days of telemetry.
   - **Event-Driven Retraining:** Triggered automatically if Population Stability Index ($\text{PSI}$) exceeds $0.25$ or if 45-day rolling ROC-AUC drops below $0.78$.
2. **Champion-Challenger (Shadow / Canary) Validation:**
   - Newly trained candidate models are deployed in "shadow mode" for 14 days, evaluating predictions against ground-truth outcomes alongside the incumbent production champion before automated traffic cutover.
3. **Rollback Safeguard:**
   - Deterministic model versioning in an artifact registry ensures instantaneous one-click rollback to the prior model version if downstream inference anomalies are detected.
