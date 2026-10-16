"""
Exploratory Data Analysis (EDA) Pipeline
Demonstrates univariate, bivariate, multivariate analysis, missing data handling,
and IQR outlier detection using Pandas, NumPy, Matplotlib, and Seaborn.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def generate_synthetic_telemetry(n_samples: int = 1000, random_seed: int = 42) -> pd.DataFrame:
    """Generates synthetic industrial telemetry data for EDA demonstration."""
    np.random.seed(random_seed)
    
    air_temp = np.random.normal(loc=300.0, scale=2.0, size=n_samples)
    process_temp = air_temp + 10.0 + np.random.normal(loc=0.0, scale=1.0, size=n_samples)
    rotational_speed = np.random.normal(loc=1500.0, scale=100.0, size=n_samples)
    torque = np.clip(100.0 - (rotational_speed - 1500.0) * 0.05 + np.random.normal(0, 5, n_samples), 10, 150)
    tool_wear = np.random.exponential(scale=50.0, size=n_samples)
    
    # Introduce intentional outliers and missingness for diagnostic demonstration
    torque[np.random.choice(n_samples, 10)] = 250.0  # Outlier spikes
    air_temp[np.random.choice(n_samples, 20)] = np.nan  # Simulated missing values
    
    machine_type = np.random.choice(["Type-L", "Type-M", "Type-H"], size=n_samples, p=[0.5, 0.3, 0.2])
    failure = (
        (torque > 90) | (tool_wear > 180) | (process_temp - air_temp > 12.5)
    ).astype(int)
    
    df = pd.DataFrame({
        "Air_Temperature_K": air_temp,
        "Process_Temperature_K": process_temp,
        "Rotational_Speed_RPM": rotational_speed,
        "Torque_Nm": torque,
        "Tool_Wear_min": tool_wear,
        "Machine_Type": machine_type,
        "Machine_Failure": failure
    })
    return df


def audit_missingness_and_impute(df: pd.DataFrame) -> pd.DataFrame:
    """Diagnoses and imputes missing continuous values via median."""
    print("--- 1. Missing Value Audit ---")
    null_counts = df.isnull().sum()
    print(null_counts[null_counts > 0])
    
    cleaned_df = df.copy()
    for col in cleaned_df.select_dtypes(include=[np.number]).columns:
        if cleaned_df[col].isnull().sum() > 0:
            median_val = cleaned_df[col].median()
            cleaned_df[col].fillna(median_val, inplace=True)
            print(f"Imputed column '{col}' with median: {median_val:.2f}")
    return cleaned_df


def detect_outliers_iqr(df: pd.DataFrame, feature: str) -> pd.Series:
    """Calculates Tukey's IQR boundaries and returns boolean outlier mask."""
    q1 = df[feature].quantile(0.25)
    q3 = df[feature].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    outlier_mask = (df[feature] < lower_bound) | (df[feature] > upper_bound)
    print(f"Feature: {feature} | IQR: {iqr:.2f} | Bounds: [{lower_bound:.2f}, {upper_bound:.2f}] | Outliers: {outlier_mask.sum()}")
    return outlier_mask


def main():
    print("Executing Exploratory Data Analysis & Quality Audit Pipeline...")
    df = generate_synthetic_telemetry()
    cleaned_df = audit_missingness_and_impute(df)
    
    print("\n--- 2. IQR Outlier Detection ---")
    for num_col in ["Torque_Nm", "Rotational_Speed_RPM", "Tool_Wear_min"]:
        detect_outliers_iqr(cleaned_df, num_col)
        
    print("\n--- 3. Summary Statistics ---")
    print(cleaned_df.describe().round(2))
    print("\nEDA Pipeline execution completed successfully.")


if __name__ == "__main__":
    main()
