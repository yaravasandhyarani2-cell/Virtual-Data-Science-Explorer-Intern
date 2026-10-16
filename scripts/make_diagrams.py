"""
make_diagrams.py
Generates all standalone, publication-quality PNG diagrams (150+ DPI)
using matplotlib, seaborn, and numpy for Weeks 1, 2, 3, and 4.
Color palette: Modern Corporate Palette (Deep Blue, Teal, Coral/Orange, Slate Gray).
"""

import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import seaborn as sns

os.makedirs('diagrams', exist_ok=True)

# Shared color palette
NAVY = '#1B365D'
TEAL = '#008080'
ORANGE = '#E87722'
GRAY = '#5C768D'
LIGHT_GRAY = '#F4F6F9'
DARK_TEXT = '#1E293B'
SUCCESS_GREEN = '#10B981'
WHITE = '#FFFFFF'

plt.rcParams.update({
    'font.size': 11,
    'font.sans-serif': ['Arial', 'Helvetica', 'DejaVu Sans'],
    'figure.autolayout': True,
    'axes.edgecolor': '#CBD5E1',
    'axes.linewidth': 1.2
})


# ==========================================
# WEEK 1 DIAGRAMS (4 Diagrams)
# ==========================================

def make_w1_fig1_workflow():
    """Week 1 - Figure 1: End-to-End Data Science Project Workflow."""
    fig, ax = plt.subplots(figsize=(10, 4.5), dpi=200)
    ax.axis('off')

    stages = [
        ("1. Ingestion &\nTelemetry Audit", "Ingest billing, CRM,\nusage logs & contract dtypes", NAVY),
        ("2. Data Hygiene &\nPreprocessing", "Impute nulls (median),\nscreen outliers & normalize", TEAL),
        ("3. Exploratory Data\nAnalysis (EDA)", "Univariate, bivariate,\ncorrelation & churn signal", GRAY),
        ("4. ML Pipelining\n& Model Training", "Ensemble modeling,\n5-fold CV & tuning", ORANGE),
        ("5. Decision Support\n& Deployment", "Cost thresholding, SHAP\nattribution & REST API", NAVY)
    ]

    for i, (title, desc, color) in enumerate(stages):
        x = i * 2.1 + 0.2
        # Draw Card
        rect = patches.FancyBboxPatch((x, 0.8), 1.7, 2.6, boxstyle="round,pad=0.15",
                                      facecolor=LIGHT_GRAY, edgecolor=color, linewidth=2.5)
        ax.add_patch(rect)
        # Header Box
        header_rect = patches.FancyBboxPatch((x, 2.5), 1.7, 0.9, boxstyle="round,pad=0.1",
                                             facecolor=color, edgecolor=color)
        ax.add_patch(header_rect)
        ax.text(x + 0.85, 2.95, title, ha='center', va='center', color=WHITE,
                weight='bold', fontsize=10.5)
        ax.text(x + 0.85, 1.6, desc, ha='center', va='center', color=DARK_TEXT,
                fontsize=9.5, linespacing=1.4)

        # Arrow
        if i < len(stages) - 1:
            ax.annotate('', xy=(x + 2.1, 2.1), xytext=(x + 1.75, 2.1),
                        arrowprops=dict(arrowstyle="->", color=ORANGE, lw=3, mutation_scale=18))

    ax.set_xlim(-0.1, 10.5)
    ax.set_ylim(0.2, 3.8)
    plt.title("Figure 1: End-to-End Enterprise Telecom Churn Project Methodology",
              fontsize=13, weight='bold', pad=15, color=NAVY)
    plt.savefig('diagrams/w1_fig1_project_workflow.png', bbox_inches='tight')
    plt.close()


def make_w1_fig2_gantt():
    """Week 1 - Figure 2: Gantt Chart of 33-Hour Operational Sprint."""
    fig, ax = plt.subplots(figsize=(10, 5), dpi=200)

    tasks = [
        "Phase 6: Exec Synthesis & Report",
        "Phase 5: ML Training & Cross-Validation",
        "Phase 4: Feature Pipeline Composition",
        "Phase 3: Exploratory Data Analysis (EDA)",
        "Phase 2: Cleaning, Imputation & Audit",
        "Phase 1: Ingestion & Environment Setup"
    ]
    starts = [28, 22, 17, 10, 5, 0]
    durations = [5, 6, 5, 7, 5, 5]
    colors = [NAVY, ORANGE, TEAL, GRAY, TEAL, NAVY]

    y_pos = np.arange(len(tasks))
    bars = ax.barh(y_pos, durations, left=starts, height=0.55, color=colors, edgecolor='#FFFFFF', linewidth=1.5)

    for bar, duration, start in zip(bars, durations, starts):
        ax.text(start + duration / 2, bar.get_y() + bar.get_height() / 2,
                f"{duration}h (Hours {start}-{start+duration})",
                ha='center', va='center', color=WHITE, weight='bold', fontsize=10)

    ax.set_yticks(y_pos)
    ax.set_yticklabels(tasks, fontsize=10.5, weight='bold', color=DARK_TEXT)
    ax.set_xlabel("Cumulative Project Sprint Hours (Total = 33 Hours)", fontsize=11, weight='bold', color=NAVY)
    ax.set_xlim(0, 35)
    ax.grid(axis='x', linestyle='--', alpha=0.5)
    ax.set_axisbelow(True)
    plt.title("Figure 2: 33-Hour Sprint Timeline Allocation (Gantt Schedule)",
              fontsize=13, weight='bold', pad=15, color=NAVY)
    plt.savefig('diagrams/w1_fig2_gantt_timeline.png', bbox_inches='tight')
    plt.close()


def make_w1_fig3_hours_pie():
    """Week 1 - Figure 3: Hours Allocation per Phase."""
    fig, ax = plt.subplots(figsize=(8, 5), dpi=200)

    phases = [
        'Phase 1: Ingestion (5h)',
        'Phase 2: Cleaning (5h)',
        'Phase 3: EDA (7h)',
        'Phase 4: Pipelines (5h)',
        'Phase 5: ML Modeling (6h)',
        'Phase 6: Synthesis (5h)'
    ]
    hours = [5, 5, 7, 5, 6, 5]
    colors = [NAVY, TEAL, GRAY, ORANGE, '#0284C7', '#475569']

    wedges, texts, autotexts = ax.pie(
        hours, labels=phases, autopct='%1.1f%%', startangle=140,
        colors=colors, explode=(0.02, 0.02, 0.06, 0.02, 0.04, 0.02),
        textprops=dict(color=DARK_TEXT, fontsize=10, weight='bold'),
        wedgeprops=dict(edgecolor='white', linewidth=2)
    )
    for at in autotexts:
        at.set_color('white')
        at.set_weight('bold')
        at.set_fontsize(10.5)

    plt.title("Figure 3: Planned Effort Distribution Across Project Phases (33h Total)",
              fontsize=12.5, weight='bold', pad=15, color=NAVY)
    plt.savefig('diagrams/w1_fig3_hours_distribution.png', bbox_inches='tight')
    plt.close()


def make_w1_fig4_architecture():
    """Week 1 - Figure 4: System Architecture Diagram."""
    fig, ax = plt.subplots(figsize=(10, 5), dpi=200)
    ax.axis('off')

    # Draw 4 vertical tiers
    tiers = [
        ("Data Layer", ["Raw CRM Records", "Billing DB (SQL)", "Network Telemetry", "Support Logs"], NAVY),
        ("Processing Layer", ["Schema Validator", "Median Imputer", "Tukey IQR Filter", "ColumnTransformer"], TEAL),
        ("Analytics / ML", ["Stratified 5-Fold CV", "Random Forest Classifier", "Threshold Tuner (p*)", "SHAP Explainer"], ORANGE),
        ("Delivery Layer", ["Retention Dashboard", "FastAPI Microservice", "Daily CRM Alerts", "Executive Briefing"], GRAY)
    ]

    for col_idx, (tier_name, items, color) in enumerate(tiers):
        x = col_idx * 2.5 + 0.3
        # Main Column Container
        col_box = patches.FancyBboxPatch((x, 0.5), 2.1, 4.0, boxstyle="round,pad=0.1",
                                         facecolor=LIGHT_GRAY, edgecolor=color, linewidth=2)
        ax.add_patch(col_box)
        # Header
        h_box = patches.FancyBboxPatch((x, 3.9), 2.1, 0.6, boxstyle="round,pad=0.08",
                                       facecolor=color, edgecolor=color)
        ax.add_patch(h_box)
        ax.text(x + 1.05, 4.2, tier_name, ha='center', va='center', color=WHITE, weight='bold', fontsize=11)

        # Items
        for item_idx, item in enumerate(items):
            iy = 3.2 - (item_idx * 0.8)
            ibox = patches.FancyBboxPatch((x + 0.15, iy), 1.8, 0.55, boxstyle="round,pad=0.05",
                                          facecolor=WHITE, edgecolor='#CBD5E1', linewidth=1.2)
            ax.add_patch(ibox)
            ax.text(x + 1.05, iy + 0.27, item, ha='center', va='center', color=DARK_TEXT, fontsize=9.5, weight='bold')

        # Arrow to next tier
        if col_idx < len(tiers) - 1:
            ax.annotate('', xy=(x + 2.5, 2.5), xytext=(x + 2.15, 2.5),
                        arrowprops=dict(arrowstyle="->", color=NAVY, lw=2.5, mutation_scale=16))

    ax.set_xlim(0, 10.5)
    ax.set_ylim(0.2, 4.8)
    plt.title("Figure 4: Enterprise Predictive Maintenance & Churn Analytics System Architecture",
              fontsize=13, weight='bold', pad=15, color=NAVY)
    plt.savefig('diagrams/w1_fig4_system_architecture.png', bbox_inches='tight')
    plt.close()


# ==========================================
# WEEK 2 DIAGRAMS (6 Diagrams)
# ==========================================

def make_w2_fig1_eda_flow():
    """Week 2 - Figure 1: EDA Workflow Architecture."""
    fig, ax = plt.subplots(figsize=(10, 4.5), dpi=200)
    ax.axis('off')

    steps = [
        ("Step 1:\nSchema & Types", "Data type casting,\ncardinality scan &\ncompleteness check", NAVY),
        ("Step 2:\nData Hygiene", "MCAR/MAR audit,\nmedian imputation &\nIQR outlier bounds", TEAL),
        ("Step 3:\nUnivariate EDA", "Histograms + KDE,\nskewness/kurtosis &\nfrequency counts", GRAY),
        ("Step 4:\nBivariate EDA", "Scatter + OLS,\ngrouped boxplots &\nchurn cross-tabs", ORANGE),
        ("Step 5:\nMultivariate EDA", "Spearman heatmap,\ninteraction ratios &\nfeature blueprints", NAVY)
    ]

    for i, (title, desc, color) in enumerate(steps):
        x = i * 2.1 + 0.2
        card = patches.FancyBboxPatch((x, 0.8), 1.7, 2.7, boxstyle="round,pad=0.15",
                                      facecolor=LIGHT_GRAY, edgecolor=color, linewidth=2.2)
        ax.add_patch(card)
        hcard = patches.FancyBboxPatch((x, 2.65), 1.7, 0.85, boxstyle="round,pad=0.1",
                                       facecolor=color, edgecolor=color)
        ax.add_patch(hcard)
        ax.text(x + 0.85, 3.05, title, ha='center', va='center', color=WHITE, weight='bold', fontsize=10.5)
        ax.text(x + 0.85, 1.65, desc, ha='center', va='center', color=DARK_TEXT, fontsize=9.5, linespacing=1.4)

        if i < len(steps) - 1:
            ax.annotate('', xy=(x + 2.1, 2.1), xytext=(x + 1.75, 2.1),
                        arrowprops=dict(arrowstyle="->", color=TEAL, lw=2.5, mutation_scale=16))

    ax.set_xlim(-0.1, 10.5)
    ax.set_ylim(0.2, 3.8)
    plt.title("Figure 1: Systematic Exploratory Data Analysis & Diagnostic Process Flow",
              fontsize=13, weight='bold', pad=15, color=NAVY)
    plt.savefig('diagrams/w2_fig1_eda_workflow.png', bbox_inches='tight')
    plt.close()


def make_w2_fig2_hist_kde():
    """Week 2 - Figure 2: Histogram with KDE overlay."""
    np.random.seed(42)
    fig, ax = plt.subplots(figsize=(8, 4.5), dpi=200)

    retained = np.random.normal(loc=55, scale=18, size=1200)
    churned = np.random.normal(loc=82, scale=14, size=600)
    retained = np.clip(retained, 18, 120)
    churned = np.clip(churned, 25, 120)

    sns.histplot(retained, kde=True, color=TEAL, label='Retained Customers (Mean: $55)',
                 stat="density", bins=25, alpha=0.45, ax=ax)
    sns.histplot(churned, kde=True, color=ORANGE, label='Churned Customers (Mean: $82)',
                 stat="density", bins=25, alpha=0.45, ax=ax)

    ax.axvline(np.mean(retained), color=TEAL, linestyle='--', linewidth=2)
    ax.axvline(np.mean(churned), color=ORANGE, linestyle='--', linewidth=2)

    ax.set_title("Figure 2: Monthly Charges Distribution with KDE Overlay by Churn Status",
                 fontsize=12, weight='bold', pad=12, color=NAVY)
    ax.set_xlabel("Monthly Charges ($ USD)", fontsize=10.5, weight='bold')
    ax.set_ylabel("Probability Density", fontsize=10.5, weight='bold')
    ax.legend(frameon=True, facecolor=WHITE, edgecolor='#CBD5E1', fontsize=9.5)
    ax.grid(True, linestyle=':', alpha=0.6)
    plt.savefig('diagrams/w2_fig2_histogram_kde.png', bbox_inches='tight')
    plt.close()


def make_w2_fig3_boxplot():
    """Week 2 - Figure 3: Box plot of Tenure by Contract Type."""
    np.random.seed(42)
    fig, ax = plt.subplots(figsize=(8, 4.5), dpi=200)

    m2m = np.random.exponential(scale=12, size=500) + 1
    one_yr = np.random.normal(loc=34, scale=10, size=350)
    two_yr = np.random.normal(loc=56, scale=11, size=300)
    m2m = np.clip(m2m, 1, 72)
    one_yr = np.clip(one_yr, 1, 72)
    two_yr = np.clip(two_yr, 1, 72)

    data = [m2m, one_yr, two_yr]
    box = ax.boxplot(data, tick_labels=['Month-to-Month', 'One-Year', 'Two-Year'],
                     patch_artist=True, notch=True, widths=0.5,
                     boxprops=dict(linewidth=1.5),
                     medianprops=dict(color=ORANGE, linewidth=2.5),
                     whiskerprops=dict(color=NAVY, linewidth=1.5))

    colors = [LIGHT_GRAY, '#E0F2FE', '#DCFCE7']
    edge_colors = [GRAY, '#0284C7', SUCCESS_GREEN]
    for patch, c, ec in zip(box['boxes'], colors, edge_colors):
        patch.set_facecolor(c)
        patch.set_edgecolor(ec)

    # Jitter overlay
    for i, d in enumerate(data):
        y = np.random.choice(d, size=min(len(d), 100), replace=False)
        x = np.random.normal(i + 1, 0.04, size=len(y))
        ax.scatter(x, y, alpha=0.35, color=NAVY, s=15, zorder=3)

    ax.set_title("Figure 3: Customer Tenure Variance across Contract Types with Strip Jitter",
                 fontsize=12, weight='bold', pad=12, color=NAVY)
    ax.set_xlabel("Contract Commitment Tier", fontsize=10.5, weight='bold')
    ax.set_ylabel("Tenure (Months)", fontsize=10.5, weight='bold')
    ax.grid(axis='y', linestyle='--', alpha=0.5)
    plt.savefig('diagrams/w2_fig3_boxplot_tenure.png', bbox_inches='tight')
    plt.close()


def make_w2_fig4_scatter():
    """Week 2 - Figure 4: Scatter Plot of Monthly Charges vs Total Charges with OLS."""
    np.random.seed(42)
    fig, ax = plt.subplots(figsize=(8, 4.5), dpi=200)

    monthly = np.random.uniform(20, 115, size=400)
    tenure = np.random.uniform(2, 70, size=400)
    total = monthly * tenure + np.random.normal(0, 80, size=400)
    churn = (monthly > 75) & (tenure < 25)

    ax.scatter(monthly[~churn], total[~churn], color=TEAL, alpha=0.55, s=28, label='Retained Customers')
    ax.scatter(monthly[churn], total[churn], color=ORANGE, alpha=0.8, s=36, marker='^', label='Churned Accounts')

    # Trendline
    m, b = np.polyfit(monthly, total, 1)
    ax.plot(monthly, m * monthly + b, color=NAVY, linewidth=2.2, linestyle='-', label=f'OLS Trend (Slope: {m:.1f})')

    ax.set_title("Figure 4: Bivariate Interaction: Monthly Charges vs. Total Charges",
                 fontsize=12, weight='bold', pad=12, color=NAVY)
    ax.set_xlabel("Monthly Charges ($ USD)", fontsize=10.5, weight='bold')
    ax.set_ylabel("Cumulative Total Charges ($ USD)", fontsize=10.5, weight='bold')
    ax.legend(frameon=True, facecolor=WHITE, edgecolor='#CBD5E1', fontsize=9.5)
    ax.grid(True, linestyle=':', alpha=0.6)
    plt.savefig('diagrams/w2_fig4_scatter_charges.png', bbox_inches='tight')
    plt.close()


def make_w2_fig5_heatmap():
    """Week 2 - Figure 5: Correlation Heatmap."""
    fig, ax = plt.subplots(figsize=(8, 6), dpi=200)

    features = ['Tenure', 'MonthlyCharges', 'TotalCharges', 'SupportTickets', 'OverdueDays', 'Churn']
    corr_matrix = np.array([
        [ 1.00,  0.25,  0.83, -0.28, -0.19, -0.42],
        [ 0.25,  1.00,  0.65,  0.34,  0.22,  0.38],
        [ 0.83,  0.65,  1.00, -0.12, -0.05, -0.21],
        [-0.28,  0.34, -0.12,  1.00,  0.48,  0.51],
        [-0.19,  0.22, -0.05,  0.48,  1.00,  0.33],
        [-0.42,  0.38, -0.21,  0.51,  0.33,  1.00]
    ])

    cmap = sns.diverging_palette(220, 20, as_cmap=True)
    sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap=cmap, vmin=-0.6, vmax=0.6,
                xticklabels=features, yticklabels=features, ax=ax,
                cbar_kws={'label': 'Spearman Rank Correlation Coefficient'},
                linewidths=1.2, linecolor='white')

    ax.set_title("Figure 5: Spearman Correlation Matrix of Key Behavioral & Financial Attributes",
                 fontsize=12, weight='bold', pad=15, color=NAVY)
    plt.xticks(rotation=30, ha='right', fontsize=9.5, weight='bold')
    plt.yticks(rotation=0, fontsize=9.5, weight='bold')
    plt.savefig('diagrams/w2_fig5_correlation_heatmap.png', bbox_inches='tight')
    plt.close()


def make_w2_fig6_missing_bar():
    """Week 2 - Figure 6: Missing Values Audit Heatmap / Bar."""
    fig, ax = plt.subplots(figsize=(8, 4), dpi=200)

    attributes = ['CustomerID', 'TenureMonths', 'MonthlyCharges', 'TotalCharges',
                  'SupportTickets', 'PaymentMethod', 'ContractType']
    missing_pct = [0.0, 0.0, 0.0, 1.8, 3.4, 0.0, 0.0]
    colors = [SUCCESS_GREEN if p == 0 else ORANGE for p in missing_pct]

    bars = ax.barh(attributes, missing_pct, color=colors, edgecolor=NAVY, linewidth=1)
    for bar, pct in zip(bars, missing_pct):
        text = f"{pct:.1f}% Missing (Imputed)" if pct > 0 else "100% Complete"
        ax.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height() / 2, text,
                va='center', fontsize=9.5, weight='bold', color=DARK_TEXT)

    ax.set_xlim(0, 5.5)
    ax.set_xlabel("Missing Data Percentage (%)", fontsize=10.5, weight='bold')
    ax.set_title("Figure 6: Telemetry Ingestion Missingness Diagnostic Audit",
                 fontsize=12, weight='bold', pad=12, color=NAVY)
    ax.grid(axis='x', linestyle='--', alpha=0.5)
    plt.savefig('diagrams/w2_fig6_missing_audit.png', bbox_inches='tight')
    plt.close()


# ==========================================
# WEEK 3 DIAGRAMS (5 Diagrams)
# ==========================================

def make_w3_fig1_ml_flow():
    """Week 3 - Figure 1: Machine Learning Lifecycle Workflow."""
    fig, ax = plt.subplots(figsize=(10, 4.5), dpi=200)
    ax.axis('off')

    stages = [
        ("1. Data Split &\nPartitioning", "Stratified 80/20 split\nPreserve 24% churn\nSeed=42 for reproducibility", NAVY),
        ("2. Leak-Free\nColumnTransformer", "Median Imputer\nRobustScaler for numeric\nOneHotEncoder (ignore unk)", TEAL),
        ("3. Model Benchmark\n& Stratified 5-Fold", "Logistic Reg, Decision Tree,\nRandom Forest, XGBoost\nScored on PR-AUC", ORANGE),
        ("4. Tuning &\nThreshold Tuning", "RandomizedSearchCV\nAsymmetric cost matrix:\np* optimal at 0.36", GRAY),
        ("5. Serialization\n& MLOps Ready", "Joblib hermetic pipeline\nFastAPI microservice\nPSI drift monitoring", NAVY)
    ]

    for i, (title, desc, color) in enumerate(stages):
        x = i * 2.1 + 0.2
        card = patches.FancyBboxPatch((x, 0.8), 1.7, 2.7, boxstyle="round,pad=0.15",
                                      facecolor=LIGHT_GRAY, edgecolor=color, linewidth=2.2)
        ax.add_patch(card)
        hcard = patches.FancyBboxPatch((x, 2.65), 1.7, 0.85, boxstyle="round,pad=0.1",
                                       facecolor=color, edgecolor=color)
        ax.add_patch(hcard)
        ax.text(x + 0.85, 3.05, title, ha='center', va='center', color=WHITE, weight='bold', fontsize=10.5)
        ax.text(x + 0.85, 1.65, desc, ha='center', va='center', color=DARK_TEXT, fontsize=9.5, linespacing=1.4)

        if i < len(stages) - 1:
            ax.annotate('', xy=(x + 2.1, 2.1), xytext=(x + 1.75, 2.1),
                        arrowprops=dict(arrowstyle="->", color=ORANGE, lw=2.5, mutation_scale=16))

    ax.set_xlim(-0.1, 10.5)
    ax.set_ylim(0.2, 3.8)
    plt.title("Figure 1: End-to-End Machine Learning Model Training & Deployment Pipeline",
              fontsize=13, weight='bold', pad=15, color=NAVY)
    plt.savefig('diagrams/w3_fig1_ml_workflow.png', bbox_inches='tight')
    plt.close()


def make_w3_fig2_cv_diag():
    """Week 3 - Figure 2: Stratified 5-Fold Cross-Validation Diagram."""
    fig, ax = plt.subplots(figsize=(9, 4.5), dpi=200)

    n_splits = 5
    for fold in range(n_splits):
        for part in range(n_splits):
            is_val = (part == fold)
            color = ORANGE if is_val else TEAL
            label_text = "Val" if is_val else "Train"

            rect = patches.Rectangle((part * 1.8 + 0.2, (4 - fold) * 0.8 + 0.2), 1.6, 0.55,
                                     facecolor=color, edgecolor=WHITE, linewidth=1.5)
            ax.add_patch(rect)
            ax.text(part * 1.8 + 1.0, (4 - fold) * 0.8 + 0.47, label_text,
                    ha='center', va='center', color=WHITE, weight='bold', fontsize=10)

    ax.set_yticks([i * 0.8 + 0.47 for i in range(5)][::-1])
    ax.set_yticklabels([f"Fold {i+1}" for i in range(5)], fontsize=10.5, weight='bold', color=DARK_TEXT)
    ax.set_xticks([])
    ax.set_xlim(0, 9.4)
    ax.set_ylim(0, 4.4)

    # Legend
    train_patch = patches.Patch(color=TEAL, label='Training Fold (80% Partition, Preserves Class Ratio)')
    val_patch = patches.Patch(color=ORANGE, label='Validation Fold (20% Partition, Out-of-Fold Evaluation)')
    ax.legend(handles=[train_patch, val_patch], loc='upper center', bbox_to_anchor=(0.5, -0.05),
              ncol=2, frameon=True, facecolor=WHITE, edgecolor='#CBD5E1', fontsize=9.5)

    ax.set_title("Figure 2: Stratified 5-Fold Cross-Validation Partitioning Scheme",
                 fontsize=12.5, weight='bold', pad=15, color=NAVY)
    plt.savefig('diagrams/w3_fig2_kfold_cv.png', bbox_inches='tight')
    plt.close()


def make_w3_fig3_confusion_matrix():
    """Week 3 - Figure 3: Illustrative Confusion Matrix."""
    fig, ax = plt.subplots(figsize=(6, 5), dpi=200)

    cm = np.array([[724, 76],
                   [ 58, 142]])

    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False,
                xticklabels=['Pred: Retained (0)', 'Pred: Churned (1)'],
                yticklabels=['Actual: Retained (0)', 'Actual: Churned (1)'],
                annot_kws={'size': 14, 'weight': 'bold'}, ax=ax, linewidths=1.5, linecolor='white')

    ax.set_title("Figure 3: Confusion Matrix on Test Holdout (Illustrative Benchmark)",
                 fontsize=11.5, weight='bold', pad=12, color=NAVY)
    plt.savefig('diagrams/w3_fig3_confusion_matrix.png', bbox_inches='tight')
    plt.close()


def make_w3_fig4_roc_model_cmp():
    """Week 3 - Figure 4: ROC Curves & Model Comparison."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5), dpi=200)

    # Left: ROC Curves
    fpr = np.linspace(0, 1, 100)
    tpr_rf = 1 / (1 + np.exp(-5 * (fpr - 0.15)))
    tpr_rf = np.clip(tpr_rf, 0, 1)
    tpr_lr = 1 / (1 + np.exp(-3 * (fpr - 0.25)))
    tpr_lr = np.clip(tpr_lr, 0, 1)

    ax1.plot(fpr, tpr_rf, color=ORANGE, linewidth=2.5, label='Random Forest (AUC = 0.865)')
    ax1.plot(fpr, tpr_lr, color=TEAL, linewidth=2, label='Logistic Reg (AUC = 0.792)')
    ax1.plot([0, 1], [0, 1], color=GRAY, linestyle='--', label='Random Chance (AUC = 0.500)')
    ax1.set_xlabel('False Positive Rate (FPR)', fontsize=10, weight='bold')
    ax1.set_ylabel('True Positive Rate (TPR / Recall)', fontsize=10, weight='bold')
    ax1.set_title('Receiver Operating Characteristic (ROC)', fontsize=11, weight='bold', color=NAVY)
    ax1.legend(loc='lower right', fontsize=8.5, frameon=True)
    ax1.grid(True, linestyle=':', alpha=0.6)

    # Right: Bar Chart
    models = ['LogReg', 'DecTree', 'RandForest', 'XGBoost']
    pr_auc = [0.548, 0.482, 0.682, 0.691]
    bars = ax2.bar(models, pr_auc, color=[GRAY, '#94A3B8', ORANGE, TEAL], edgecolor=NAVY, linewidth=1)
    for bar in bars:
        ax2.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.015,
                 f"{bar.get_height():.3f}", ha='center', va='bottom', fontsize=9.5, weight='bold')
    ax2.set_ylim(0, 0.8)
    ax2.set_ylabel('PR-AUC Score (Avg Precision)', fontsize=10, weight='bold')
    ax2.set_title('Model PR-AUC Benchmark Comparison', fontsize=11, weight='bold', color=NAVY)
    ax2.grid(axis='y', linestyle='--', alpha=0.5)

    plt.suptitle("Figure 4: Predictive Model Discriminative Power & Benchmark Comparison (Illustrative)",
                 fontsize=12, weight='bold', color=NAVY, y=1.02)
    plt.tight_layout()
    plt.savefig('diagrams/w3_fig4_roc_model_cmp.png', bbox_inches='tight')
    plt.close()


def make_w3_fig5_mlops():
    """Week 3 - Figure 5: MLOps & Production Loop."""
    fig, ax = plt.subplots(figsize=(9, 4.5), dpi=200)
    ax.axis('off')

    components = [
        ("1. Batch / REST API", "FastAPI Docker Container\nSub-50ms latency SLA", NAVY, (1.0, 3.2)),
        ("2. Production Inference", "Daily scoring of active accounts\nProbability + risk deciles", TEAL, (5.0, 3.2)),
        ("3. CRM Integration", "Push to Salesforce/HubSpot\nAlert CS managers with SHAP", ORANGE, (5.0, 1.0)),
        ("4. Drift & Health Monitor", "Population Stability Index\nKS tests & automated retrain", GRAY, (1.0, 1.0))
    ]

    for title, desc, color, (x, y) in components:
        box = patches.FancyBboxPatch((x, y), 3.2, 1.4, boxstyle="round,pad=0.1",
                                     facecolor=LIGHT_GRAY, edgecolor=color, linewidth=2)
        ax.add_patch(box)
        ax.text(x + 1.6, y + 1.05, title, ha='center', va='center', color=color, weight='bold', fontsize=10.5)
        ax.text(x + 1.6, y + 0.5, desc, ha='center', va='center', color=DARK_TEXT, fontsize=9.5, linespacing=1.3)

    # Connecting Arrows
    ax.annotate('', xy=(4.9, 3.9), xytext=(4.3, 3.9), arrowprops=dict(arrowstyle="->", color=NAVY, lw=2.5, mutation_scale=15))
    ax.annotate('', xy=(6.6, 2.5), xytext=(6.6, 3.1), arrowprops=dict(arrowstyle="->", color=TEAL, lw=2.5, mutation_scale=15))
    ax.annotate('', xy=(4.3, 1.7), xytext=(4.9, 1.7), arrowprops=dict(arrowstyle="->", color=ORANGE, lw=2.5, mutation_scale=15))
    ax.annotate('', xy=(2.6, 3.1), xytext=(2.6, 2.5), arrowprops=dict(arrowstyle="->", color=GRAY, lw=2.5, mutation_scale=15))

    ax.set_xlim(0, 9.2)
    ax.set_ylim(0.2, 5.0)
    plt.title("Figure 5: Closed-Loop Production Deployment & Continuous MLOps Lifecycle",
              fontsize=12.5, weight='bold', pad=15, color=NAVY)
    plt.savefig('diagrams/w3_fig5_mlops_lifecycle.png', bbox_inches='tight')
    plt.close()


# ==========================================
# WEEK 4 DIAGRAMS (7 Diagrams)
# ==========================================

def make_w4_fig1_trend():
    """Week 4 - Figure 1: Churn Trend Line Over 12 Months."""
    fig, ax = plt.subplots(figsize=(8, 4.5), dpi=200)

    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    baseline_churn = [24.2, 23.8, 24.5, 25.1, 24.9, 25.4, 24.8, 25.0, 24.3, 23.9, 24.1, 24.0]
    projected_churn = [24.2, 23.8, 24.5, 25.1, 22.8, 20.4, 18.2, 16.9, 16.0, 15.5, 15.2, 14.8]

    ax.plot(months, baseline_churn, color=GRAY, linestyle='--', marker='o', label='Historical Baseline Churn (~24.5%)')
    ax.plot(months, projected_churn, color=ORANGE, linewidth=2.8, marker='s', label='Model-Assisted Proactive Retention Path')

    ax.axvline('Apr', color=TEAL, linestyle=':', linewidth=2, label='Model Pilot Launch (Month 4)')
    ax.set_ylabel("Monthly Churn Rate (%)", fontsize=10.5, weight='bold')
    ax.set_title("Figure 1: Projected Churn Rate Reduction Post-ML Model Deployment (Illustrative)",
                 fontsize=12, weight='bold', pad=12, color=NAVY)
    ax.legend(frameon=True, facecolor=WHITE, edgecolor='#CBD5E1', fontsize=9.5)
    ax.grid(True, linestyle=':', alpha=0.6)
    plt.savefig('diagrams/w4_fig1_churn_trend.png', bbox_inches='tight')
    plt.close()


def make_w4_fig2_contract_bar():
    """Week 4 - Figure 2: Churn by Contract Type."""
    fig, ax = plt.subplots(figsize=(7, 4.5), dpi=200)

    contracts = ['Month-to-Month', 'One-Year Contract', 'Two-Year Contract']
    churn_rates = [42.7, 11.2, 2.8]
    colors = [ORANGE, TEAL, SUCCESS_GREEN]

    bars = ax.bar(contracts, churn_rates, color=colors, edgecolor=NAVY, linewidth=1.2, width=0.5)
    for bar in bars:
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1.0,
                f"{bar.get_height():.1f}%", ha='center', va='bottom', fontsize=11, weight='bold')

    ax.set_ylim(0, 50)
    ax.set_ylabel("Annualized Churn Rate (%)", fontsize=10.5, weight='bold')
    ax.set_title("Figure 2: Empirical Churn Rates Segmented by Contract Horizon (Illustrative)",
                 fontsize=12, weight='bold', pad=12, color=NAVY)
    ax.grid(axis='y', linestyle='--', alpha=0.5)
    plt.savefig('diagrams/w4_fig2_contract_churn.png', bbox_inches='tight')
    plt.close()


def make_w4_fig3_tenure_anomaly():
    """Week 4 - Figure 3: Tenure Distribution with Anomaly Highlight."""
    fig, ax = plt.subplots(figsize=(8, 4.5), dpi=200)

    tenure_bins = ['0-6 Mo', '7-12 Mo', '13-24 Mo', '25-36 Mo', '37-48 Mo', '49-60 Mo', '61-72 Mo']
    churn_counts = [480, 390, 210, 150, 95, 60, 35]
    colors = [ORANGE, '#FB923C', TEAL, TEAL, GRAY, GRAY, GRAY]

    bars = ax.bar(tenure_bins, churn_counts, color=colors, edgecolor=NAVY, linewidth=1.2)
    for bar in bars:
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 10,
                f"{int(bar.get_height())}", ha='center', va='bottom', fontsize=10, weight='bold')

    ax.annotate('The "Onboarding Valley":\n61% of churn occurs in Year 1',
                xy=(0.5, 450), xytext=(1.8, 460),
                arrowprops=dict(facecolor=NAVY, shrink=0.08, width=1.5, headwidth=8),
                fontsize=9.5, weight='bold', color=NAVY,
                bbox=dict(boxstyle="round,pad=0.3", fc=WHITE, ec=NAVY, lw=1))

    ax.set_ylim(0, 550)
    ax.set_ylabel("Number of Churned Accounts", fontsize=10.5, weight='bold')
    ax.set_title("Figure 3: Churn Volume by Customer Tenure Bracket (Illustrative)",
                 fontsize=12, weight='bold', pad=12, color=NAVY)
    ax.grid(axis='y', linestyle='--', alpha=0.5)
    plt.savefig('diagrams/w4_fig3_tenure_anomaly.png', bbox_inches='tight')
    plt.close()


def make_w4_fig4_feature_importance():
    """Week 4 - Figure 4: Feature Importance Ranking."""
    fig, ax = plt.subplots(figsize=(8, 4.5), dpi=200)

    features = [
        'Contract Type: Month-to-Month',
        'Usage Velocity Decay (Last 30d/60d)',
        'Support Ticket Escalation Index',
        'Tenure (< 12 Months)',
        'Monthly Charges (> $80/mo)',
        'Payment: Electronic Check',
        'Overdue Billing Status'
    ][::-1]

    importance = [0.28, 0.22, 0.18, 0.14, 0.09, 0.05, 0.04][::-1]
    colors = [ORANGE if imp >= 0.18 else TEAL for imp in importance]

    bars = ax.barh(features, importance, color=colors, edgecolor=NAVY, linewidth=1.2, height=0.6)
    for bar in bars:
        ax.text(bar.get_width() + 0.008, bar.get_y() + bar.get_height() / 2,
                f"{bar.get_width() * 100:.1f}%", va='center', fontsize=10, weight='bold')

    ax.set_xlim(0, 0.33)
    ax.set_xlabel("Normalized Relative Feature Importance (SHAP Value Share)", fontsize=10.5, weight='bold')
    ax.set_title("Figure 4: Global Predictive Feature Importance Rankings (Illustrative)",
                 fontsize=12, weight='bold', pad=12, color=NAVY)
    ax.grid(axis='x', linestyle='--', alpha=0.5)
    plt.savefig('diagrams/w4_fig4_feature_importance.png', bbox_inches='tight')
    plt.close()


def make_w4_fig5_retention_savings():
    """Week 4 - Figure 5: Retention-Savings Impact Chart."""
    fig, ax = plt.subplots(figsize=(7, 4.5), dpi=200)

    categories = ['At-Risk ARR\nExposure', 'Gross Revenue\nProtected', 'Program Retention\nIncentive Cost', 'Net Annual\nValue Created']
    values = [1872.0, 274.5, 28.1, 246.4]
    colors = [GRAY, TEAL, ORANGE, SUCCESS_GREEN]

    bars = ax.bar(categories, values, color=colors, edgecolor=NAVY, linewidth=1.2, width=0.5)
    for bar in bars:
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 30,
                f"${bar.get_height():.1f}K", ha='center', va='bottom', fontsize=10.5, weight='bold')

    ax.set_ylim(0, 2150)
    ax.set_ylabel("Financial Capital ($ Thousands USD)", fontsize=10.5, weight='bold')
    ax.set_title("Figure 5: Annualized Financial Impact & Net Value Creation (Illustrative)",
                 fontsize=12, weight='bold', pad=12, color=NAVY)
    ax.grid(axis='y', linestyle='--', alpha=0.5)
    plt.savefig('diagrams/w4_fig5_retention_savings.png', bbox_inches='tight')
    plt.close()


def make_w4_fig6_kpi_dashboard():
    """Week 4 - Figure 6: Executive KPI Dashboard Mockup."""
    fig, ax = plt.subplots(figsize=(9, 4.5), dpi=200)
    ax.axis('off')

    kpis = [
        ("Current Churn Rate", "24.0%", "Target: < 16.0%", ORANGE),
        ("Model ROC-AUC", "0.865", "Benchmark: > 0.850", SUCCESS_GREEN),
        ("Decile 1 Recall", "73.4%", "Target: > 70.0%", SUCCESS_GREEN),
        ("Net ARR Protected", "$246.4K", "ROI: 875%", TEAL)
    ]

    for i, (title, value, sub, color) in enumerate(kpis):
        x = i * 2.2 + 0.2
        box = patches.FancyBboxPatch((x, 1.0), 1.9, 2.5, boxstyle="round,pad=0.15",
                                     facecolor=LIGHT_GRAY, edgecolor=color, linewidth=2.5)
        ax.add_patch(box)
        ax.text(x + 0.95, 3.0, title, ha='center', va='center', color=DARK_TEXT, fontsize=10, weight='bold')
        ax.text(x + 0.95, 2.2, value, ha='center', va='center', color=color, fontsize=18, weight='bold')
        ax.text(x + 0.95, 1.5, sub, ha='center', va='center', color=GRAY, fontsize=9, weight='bold')

    ax.set_xlim(0, 9.2)
    ax.set_ylim(0.5, 4.0)
    plt.title("Figure 6: Executive Churn Mitigation & Machine Learning KPI Scorecard (Illustrative)",
              fontsize=12.5, weight='bold', pad=15, color=NAVY)
    plt.savefig('diagrams/w4_fig6_kpi_dashboard.png', bbox_inches='tight')
    plt.close()


def make_w4_fig7_storytelling():
    """Week 4 - Figure 7: Storytelling Arc Diagram (Situation-Complication-Resolution)."""
    fig, ax = plt.subplots(figsize=(9.5, 4.5), dpi=200)
    ax.axis('off')

    stages = [
        ("SITUATION\n(Where We Stand)", "• Stable market growth\n• Increasing CAC (5-7x)\n• Retention is top profit lever", NAVY),
        ("COMPLICATION\n(The Threat)", "• 24% annual churn rate\n• $1.87M ARR leakage\n• Reactive triage arrives too late", ORANGE),
        ("RESOLUTION\n(Our Data-Driven Solution)", "• Predictive ML early warning\n• Target top 20% risk cohort\n• $246K+ net ARR protected", TEAL)
    ]

    for i, (title, points, color) in enumerate(stages):
        x = i * 3.1 + 0.3
        box = patches.FancyBboxPatch((x, 0.8), 2.5, 2.8, boxstyle="round,pad=0.15",
                                     facecolor=LIGHT_GRAY, edgecolor=color, linewidth=2.5)
        ax.add_patch(box)
        hbox = patches.FancyBboxPatch((x, 2.8), 2.5, 0.8, boxstyle="round,pad=0.1",
                                      facecolor=color, edgecolor=color)
        ax.add_patch(hbox)
        ax.text(x + 1.25, 3.2, title, ha='center', va='center', color=WHITE, weight='bold', fontsize=10.5)
        ax.text(x + 1.25, 1.7, points, ha='center', va='center', color=DARK_TEXT, fontsize=9.5, linespacing=1.5)

        if i < len(stages) - 1:
            ax.annotate('', xy=(x + 3.1, 2.2), xytext=(x + 2.65, 2.2),
                        arrowprops=dict(arrowstyle="->", color=NAVY, lw=3, mutation_scale=18))

    ax.set_xlim(0, 9.6)
    ax.set_ylim(0.2, 4.0)
    plt.title("Figure 7: Executive Data Storytelling Arc (Situation-Complication-Resolution)",
              fontsize=13, weight='bold', pad=15, color=NAVY)
    plt.savefig('diagrams/w4_fig7_storytelling_arc.png', bbox_inches='tight')
    plt.close()


def main():
    print("Generating Week 1 Diagrams...")
    make_w1_fig1_workflow()
    make_w1_fig2_gantt()
    make_w1_fig3_hours_pie()
    make_w1_fig4_architecture()

    print("Generating Week 2 Diagrams...")
    make_w2_fig1_eda_flow()
    make_w2_fig2_hist_kde()
    make_w2_fig3_boxplot()
    make_w2_fig4_scatter()
    make_w2_fig5_heatmap()
    make_w2_fig6_missing_bar()

    print("Generating Week 3 Diagrams...")
    make_w3_fig1_ml_flow()
    make_w3_fig2_cv_diag()
    make_w3_fig3_confusion_matrix()
    make_w3_fig4_roc_model_cmp()
    make_w3_fig5_mlops()

    print("Generating Week 4 Diagrams...")
    make_w4_fig1_trend()
    make_w4_fig2_contract_bar()
    make_w4_fig3_tenure_anomaly()
    make_w4_fig4_feature_importance()
    make_w4_fig5_retention_savings()
    make_w4_fig6_kpi_dashboard()
    make_w4_fig7_storytelling()

    print("All 22 publication-grade diagrams successfully generated in /diagrams!")


if __name__ == '__main__':
    main()
