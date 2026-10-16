"""
Machine Learning Training & Cross-Validation Pipeline
Demonstrates preprocessing, model training, 5-Fold Stratified Cross-Validation,
and evaluation for subscription customer churn prediction using Scikit-Learn.
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import StratifiedKFold, cross_validate
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import RobustScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score, average_precision_score, classification_report
import joblib


def generate_synthetic_churn_dataset(n_samples: int = 1500, random_seed: int = 42) -> pd.DataFrame:
    """Generates synthetic subscription dataset for churn modeling demonstration."""
    np.random.seed(random_seed)
    
    tenure_months = np.random.randint(1, 72, size=n_samples)
    monthly_charges = np.random.uniform(20.0, 120.0, size=n_samples)
    total_charges = monthly_charges * tenure_months + np.random.normal(0, 50, size=n_samples)
    support_tickets = np.random.poisson(lam=1.5, size=n_samples)
    
    contract_type = np.random.choice(["Month-to-month", "One year", "Two year"], size=n_samples, p=[0.55, 0.25, 0.20])
    payment_method = np.random.choice(["Electronic check", "Mailed check", "Bank transfer", "Credit card"], size=n_samples)
    
    # Generate realistic churn probability based on latent features
    churn_prob = (
        (contract_type == "Month-to-month") * 0.35 +
        (support_tickets > 2) * 0.25 +
        (monthly_charges > 80.0) * 0.15 -
        (tenure_months > 36) * 0.25 +
        np.random.normal(0, 0.1, size=n_samples)
    )
    churn_prob = 1 / (1 + np.exp(-churn_prob * 3))
    churn = (churn_prob > 0.5).astype(int)
    
    df = pd.DataFrame({
        "Tenure_Months": tenure_months,
        "Monthly_Charges": monthly_charges,
        "Total_Charges": total_charges,
        "Support_Tickets": support_tickets,
        "Contract_Type": contract_type,
        "Payment_Method": payment_method,
        "Churn": churn
    })
    return df


def build_preprocessing_pipeline() -> ColumnTransformer:
    """Builds scikit-learn ColumnTransformer for leak-free transformations."""
    numeric_features = ["Tenure_Months", "Monthly_Charges", "Total_Charges", "Support_Tickets"]
    categorical_features = ["Contract_Type", "Payment_Method"]
    
    numeric_transformer = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", RobustScaler())
    ])
    
    categorical_transformer = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="constant", fill_value="Unknown")),
        ("onehot", OneHotEncoder(drop="first", sparse_output=False, handle_unknown="ignore"))
    ])
    
    preprocessor = ColumnTransformer(transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features)
    ])
    return preprocessor


def evaluate_models(X: pd.DataFrame, y: pd.Series):
    """Compares Logistic Regression, Decision Tree, and Random Forest using 5-Fold Stratified CV."""
    preprocessor = build_preprocessing_pipeline()
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    
    models = {
        "Logistic Regression": LogisticRegression(class_weight="balanced", max_iter=500, random_state=42),
        "Decision Tree": DecisionTreeClassifier(max_depth=5, class_weight="balanced", random_state=42),
        "Random Forest Classifier": RandomForestClassifier(n_estimators=100, max_depth=8, class_weight="balanced", random_state=42)
    }
    
    scoring = ["roc_auc", "average_precision", "f1_macro"]
    
    print("=" * 60)
    print("5-FOLD STRATIFIED CROSS-VALIDATION BENCHMARK RESULTS")
    print("=" * 60)
    
    trained_pipelines = {}
    for name, model in models.items():
        pipeline = Pipeline(steps=[
            ("preprocessor", preprocessor),
            ("classifier", model)
        ])
        
        cv_results = cross_validate(pipeline, X, y, cv=cv, scoring=scoring, return_train_score=False)
        mean_roc = cv_results["test_roc_auc"].mean()
        mean_pr = cv_results["test_average_precision"].mean()
        mean_f1 = cv_results["test_f1_macro"].mean()
        
        print(f"\nModel: {name}")
        print(f"  - ROC-AUC:            {mean_roc:.4f} (+/- {cv_results['test_roc_auc'].std():.4f})")
        print(f"  - PR-AUC (Avg Prec):  {mean_pr:.4f} (+/- {cv_results['test_average_precision'].std():.4f})")
        print(f"  - F1-Macro:           {mean_f1:.4f} (+/- {cv_results['test_f1_macro'].std():.4f})")
        
        pipeline.fit(X, y)
        trained_pipelines[name] = pipeline
        
    return trained_pipelines["Random Forest Classifier"]


def main():
    print("Starting Machine Learning Model Development & Evaluation Workflow...")
    df = generate_synthetic_churn_dataset()
    X = df.drop(columns=["Churn"])
    y = df["Churn"]
    
    print(f"Dataset Loaded: {X.shape[0]} samples, {X.shape[1]} features.")
    print(f"Target Distribution: Churned={y.sum()} ({y.mean():.1%}), Retained={len(y) - y.sum()} ({(1-y.mean()):.1%})")
    
    best_pipeline = evaluate_models(X, y)
    
    model_filename = "churn_pipeline_rf.joblib"
    joblib.dump(best_pipeline, model_filename)
    print(f"\nSaved production-ready model pipeline artifact to '{model_filename}'.")
    print("Workflow execution completed successfully.")


if __name__ == "__main__":
    main()
