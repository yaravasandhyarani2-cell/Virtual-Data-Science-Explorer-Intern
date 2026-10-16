"""
build_week4.py
Constructs the complete Week 4 Word Document:
"Week4_Report_and_Presentation_Plan.docx" (10-15 pages equivalent)
STANDALONE FINAL REPORT: Does NOT mention "Week 1/2/3" or earlier tasks.
Sections:
 1. Executive Summary (Purpose and 4-5 key findings with mock numbers)
 2. Methodology Overview (End-to-end data pipeline, modeling, CV)
 3. Analytical Insights & Visual Evidence (Mock charts + justification for each chart type)
 4. Actionable Business Insights (Table: insight, action, expected impact)
 5. Presentation Strategy for Non-Technical Audience (Storytelling SCR arc, slide outline, do's/don'ts, jargon table)
 6. Strategic Recommendations, Implementation Roadmap, and Future Work
 7. Conclusion
Diagrams: 7 Embedded figures (mock data, labeled illustrative)
"""

import os
import sys
sys.path.append(os.path.dirname(__file__))
from doc_helper import (
    create_styled_document, add_cover_page, add_table_of_contents,
    add_heading_1, add_heading_2, add_heading_3, add_bullet_point,
    add_styled_table, add_figure_with_caption
)


def build_week4_docx():
    print("Building Week 4 Capstone Report & Presentation Plan Document...")
    doc = create_styled_document()

    # Cover Page (Standalone Capstone Report)
    add_cover_page(
        doc,
        title="Predictive Subscriber Retention Engine: Final Report & Strategic Executive Briefing",
        subtitle="Empirical Insights, Machine Learning Architecture, Financial ROI & Presentation Strategy",
        doc_ref="CAPSTONE-EXEC-FINAL-REPORT"
    )

    # Table of Contents
    toc_data = [
        ("1. Executive Summary & Financial Value Creation", 3),
        ("2. Data Science Methodology & Architectural Overview", 5),
        ("3. Analytical Insights & Empirical Visual Evidence", 6),
        ("4. Actionable Business Insights & Intervention Matrix", 9),
        ("5. Executive Presentation Strategy for Non-Technical Stakeholders", 10),
        ("6. Strategic Recommendations & 90-Day Implementation Roadmap", 12),
        ("7. Conclusion & Long-Term Strategic Outlook", 14)
    ]
    add_table_of_contents(doc, toc_data)

    # Section 1
    add_heading_1(doc, "1. Executive Summary & Financial Value Creation")
    doc.add_paragraph(
        "This capstone report delivers the final strategic synthesis and executive briefing for the enterprise Predictive "
        "Subscriber Retention Engine. Designed for C-suite decision-makers and operational leaders, this document establishes "
        "how predictive data science transforms subscriber retention from a reactive, costly damage-control exercise into a "
        "high-precision, proactive revenue engine."
    )
    doc.add_paragraph(
        "In the telecommunications sector, acquiring a new customer is estimated to be 5 to 7 times more expensive than "
        "retaining an active account holder. With an unmitigated annual churn rate of 24.0% across 10,000 active subscribers, "
        "the enterprise faces an annual revenue exposure of $1,872,000 in Annual Recurring Revenue (ARR). "
        "Our machine learning solution identifies at-risk subscribers 45 days in advance, allowing customer success teams to "
        "deploy customized retention offers before irreversible cancellation occurs."
    )
    doc.add_paragraph(
        "Figure 6 provides the Executive Churn Mitigation and Machine Learning KPI Scorecard summarizing the core operational benchmarks:"
    )
    add_figure_with_caption(
        doc,
        "diagrams/w4_fig6_kpi_dashboard.png",
        "Figure 6: Executive Churn Mitigation & Machine Learning KPI Scorecard (Illustrative)",
        width_inches=5.8
    )

    doc.add_paragraph("The five primary analytical and financial findings are summarized below:")
    add_bullet_point(doc, "Predictive Accuracy Superiority:", "The calibrated Random Forest ensemble achieved a ROC-AUC of 0.865 and a PR-AUC of 0.682 under 5-fold stratified cross-validation, outperforming linear baselines by over 9%.")
    add_bullet_point(doc, "High-Risk Decile Capture Rate:", "Targeting the top 20% highest-risk account quintile captures 73.4% of all future churn events (1,761 at-risk accounts captured).")
    add_bullet_point(doc, "The Month-to-Month Contract Cliff:", "Subscribers on month-to-month contracts exhibit an annualized churn rate of 42.7%, compared to just 11.2% for one-year and 2.8% for two-year contracts.")
    add_bullet_point(doc, "Support Ticket Escalation Friction:", "Accounts lodging 3 or more support tickets within 30 days display a 68% churn probability when resolution times exceed 48 hours.")
    add_bullet_point(doc, "Measurable Financial ROI:", "Preserving 352 high-value accounts protects $274,560 in ARR against $28,160 in operational incentive costs, generating $246,400 in net annual profit—an 875% program ROI.")

    # Section 2
    add_heading_1(doc, "2. Data Science Methodology & Architectural Overview")
    doc.add_paragraph(
        "The project methodology enforces an end-to-end, leak-free machine learning architecture spanning four core technical phases:"
    )
    add_bullet_point(doc, "Phase 1 - Ingestion & Schema Assertion:", "Consolidated 40+ attributes across customer demographics, billing history, and network telemetry. Validated data types and confirmed zero duplicate CustomerID records.")
    add_bullet_point(doc, "Phase 2 - Exploratory Data Analysis & Outlier Scrubbing:", "Diagnosed missing data patterns; imputed numeric missingness via training fold medians; screened outliers via Tukey's IQR rule; evaluated feature correlations via Spearman rank matrices.")
    add_bullet_point(doc, "Phase 3 - Leak-Free Feature Pipelines:", "Synthesized high-signal domain features (Usage Velocity Deceleration Index, Support Ticket Friction Index); encapsulated scalers (RobustScaler) and encoders (OneHotEncoder) within Scikit-Learn ColumnTransformers.")
    add_bullet_point(doc, "Phase 4 - Model Training & Threshold Calibration:", "Trained and benchmarked Logistic Regression, Decision Trees, and Random Forest ensembles under 5-Fold Stratified Cross-Validation; optimized classification threshold to p* = 0.36 based on asymmetric financial loss matrices.")

    # Section 3
    add_heading_1(doc, "3. Analytical Insights & Empirical Visual Evidence")
    doc.add_paragraph(
        "The exploratory and predictive modeling phases uncovered critical behavioral dynamics driving subscriber churn. "
        "Each insight is supported below by an empirical visual aid, accompanied by the architectural rationale for selecting that specific chart type:"
    )

    add_heading_2(doc, "3.1 Insight 1: Projected Churn Trajectory Post-Deployment")
    doc.add_paragraph(
        "Tracking monthly churn rates reveals that proactive model-assisted retention reduces annual churn from a historical baseline "
        "of 24.0% down to 14.8% over an 8-month rollout window (Figure 1). "
        "Chart Type Justification: A dual-line time series chart is the optimal visual mechanism for demonstrating temporal trajectory "
        "and visualizing the clear inflection point created by model pilot deployment."
    )
    add_figure_with_caption(
        doc,
        "diagrams/w4_fig1_churn_trend.png",
        "Figure 1: Projected Churn Rate Reduction Post-ML Model Deployment (Illustrative)",
        width_inches=5.6
    )

    add_heading_2(doc, "3.2 Insight 2: The Contract Commitment Horizon")
    doc.add_paragraph(
        "Contract type represents the single strongest structural determinant of churn risk. Month-to-month subscribers churn at "
        "42.7%, while two-year contracts experience near-zero attrition (2.8%) (Figure 2). "
        "Chart Type Justification: A discrete vertical bar chart with high-contrast color coding is chosen because it emphasizes "
        "sharp categorical disparities across ordinal commitment tiers with immediate clarity."
    )
    add_figure_with_caption(
        doc,
        "diagrams/w4_fig2_contract_churn.png",
        "Figure 2: Empirical Churn Rates Segmented by Contract Horizon (Illustrative)",
        width_inches=5.2
    )

    add_heading_2(doc, "3.3 Insight 3: The 'Onboarding Valley' Anomaly in Tenure")
    doc.add_paragraph(
        "Dissecting churn volume across customer tenure brackets reveals that 61% of all customer cancellations occur during the first "
        "12 months of service—a phenomenon termed the 'Onboarding Valley' (Figure 3). "
        "Chart Type Justification: A tenure-binned frequency histogram with explicit callout annotations was chosen to highlight "
        "the heavy early-tenure concentration and justify dedicated onboarding retention interventions."
    )
    add_figure_with_caption(
        doc,
        "diagrams/w4_fig3_tenure_anomaly.png",
        "Figure 3: Churn Volume by Customer Tenure Bracket (Illustrative)",
        width_inches=5.6
    )

    add_heading_2(doc, "3.4 Insight 4: Global Predictive Feature Importance Rankings")
    doc.add_paragraph(
        "Global SHAP feature attribution confirms that contract type (28%), usage velocity decay (22%), and support ticketing friction (18%) "
        "dominate model predictions, far outweighing demographic factors (Figure 4). "
        "Chart Type Justification: A horizontal bar chart sorted descending by SHAP importance share is the industry standard for "
        "communicating feature attribution, ensuring text labels remain readable without rotation."
    )
    add_figure_with_caption(
        doc,
        "diagrams/w4_fig4_feature_importance.png",
        "Figure 4: Global Predictive Feature Importance Rankings (Illustrative)",
        width_inches=5.6
    )

    add_heading_2(doc, "3.5 Insight 5: Financial Impact & Net Value Creation")
    doc.add_paragraph(
        "Evaluating gross ARR exposure against protected revenue and program costs highlights the exceptional financial return of "
        "predictive retention (Figure 5). "
        "Chart Type Justification: A waterfall-style financial breakdown chart provides executives with transparent visibility into "
        "revenue protection, incentive expenses, and net EBITDA impact."
    )
    add_figure_with_caption(
        doc,
        "diagrams/w4_fig5_retention_savings.png",
        "Figure 5: Annualized Financial Impact & Net Value Creation (Illustrative)",
        width_inches=5.2
    )

    # Section 4
    add_heading_1(doc, "4. Actionable Business Insights & Intervention Matrix")
    doc.add_paragraph(
        "Analytical discoveries are only valuable when mapped directly to concrete, operational business actions. "
        "The matrix below connects each analytical finding to an operational business intervention, assigned department, and projected financial outcome:"
    )
    action_headers = ["Core Analytical Finding", "Operational Business Intervention", "Owner Department", "Expected Business Impact"]
    action_data = [
        ["Month-to-month contracts account for 78% of all churn volume.", "Deploy automated contract migration incentives (15% annual discount or hardware upgrade) at Month 6-9 tenure.", "Marketing & Retention", "Projected to reduce contract-driven churn by 18%, preserving ~$85,000 ARR."],
        ["Support tickets >= 3 within 30 days trigger a 68% churn spike.", "Configure automated high-priority routing in ticketing system; dispatch VIP care supervisor for ticket 2+.", "Customer Support Operations", "Lowers support friction attrition by 25%, saving ~60 accounts annually."],
        ["A >40% usage drop precedes cancellation by 38 days.", "Trigger automated in-app re-engagement walkthroughs and personalized concierge check-in calls.", "Customer Success Team", "Recovers 20% of disengaged users before cancellation intent solidifies."],
        ["First-year tenure accounts for 61% of total churn.", "Overhaul Day-1 to Day-90 onboarding cadence with automated milestone satisfaction surveys.", "Onboarding & Product Growth", "Decreases Year-1 onboarding attrition by 12%, protecting ~$45,000 ARR."],
        ["Electronic check payment method correlates with 34% higher churn.", "Offer a one-time $10 billing credit to incentivize migration to automated credit card / bank autopay.", "Billing & Finance Desk", "Reduces involuntary billing churn and payment friction by 15%."]
    ]
    add_styled_table(doc, action_headers, action_data, [1.4, 2.3, 1.3, 1.5])

    # Section 5
    add_heading_1(doc, "5. Executive Presentation Strategy for Non-Technical Stakeholders")
    doc.add_paragraph(
        "To achieve executive buy-in across non-technical C-suite stakeholders, the presentation strategy relies on the "
        "Situation-Complication-Resolution (SCR) storytelling framework popularized by top-tier management consultancies. "
        "Figure 7 illustrates the narrative progression from current market realities to data-driven resolution."
    )
    add_figure_with_caption(
        doc,
        "diagrams/w4_fig7_storytelling_arc.png",
        "Figure 7: Executive Data Storytelling Arc (Situation-Complication-Resolution)",
        width_inches=5.8
    )

    add_heading_2(doc, "5.1 Slide-by-Slide Executive Deck Outline (10 Slides / 20 Minutes)")
    doc.add_paragraph(
        "The table below outlines the precise narrative architecture of the 10-slide executive presentation deck:"
    )
    slide_headers = ["Slide #", "Slide Title", "Core Executive Message", "Primary Visual Anchor"]
    slide_data = [
        ["Slide 1", "Executive Briefing: Revenue Retention", "Why customer retention is our highest-ROI profit lever this fiscal year.", "Scorecard callout: $246.4K net ARR preserved."],
        ["Slide 2", "The Situation: Market & CAC Dynamics", "Customer acquisition costs are rising; retaining existing subscribers is critical.", "3-year historical CAC vs. CLV chart."],
        ["Slide 3", "The Complication: The Hidden Leak", "A 24% annual churn rate erodes $1.87M in ARR; reactive outreach arrives too late.", "Waterfall chart showing revenue leakage."],
        ["Slide 4", "The Anatomy of Churn: Root Drivers", "Churn is preceded by clear behavioral indicators: contract type, ticket volume, usage drops.", "Top 5 SHAP feature importance plot."],
        ["Slide 5", "The Solution: Predictive Churn Engine", "Introducing a machine learning pipeline that flags churn risk 45 days in advance.", "High-level system architecture flowchart."],
        ["Slide 6", "Model Accuracy & Validation Rigor", "Random Forest ensemble achieves 0.865 ROC-AUC; captures 73.4% of at-risk users in top decile.", "Cumulative gains / Lift chart."],
        ["Slide 7", "Threshold Optimization: Balancing Risk", "Decision boundary adjusted to minimize business costs ($C_fn vs. $C_fp).", "Cost-loss curve vs. probability threshold."],
        ["Slide 8", "Operational Blueprint: CRM Actioning", "How Customer Success teams will use automated risk scores and SHAP reason codes.", "Mockup of Customer Success CRM card."],
        ["Slide 9", "Financial ROI & Business Case", "Preserving 352 accounts yields $274.5K in preserved ARR with an 875% program ROI.", "Cost-benefit comparison bar chart."],
        ["Slide 10", "Strategic Roadmap & Decision Gate", "Phased 90-day rollout plan: Pilot, CRM integration, full automated scoring.", "3-phase Gantt timeline & sign-off gate."]
    ]
    add_styled_table(doc, slide_headers, slide_data, [0.8, 1.8, 2.5, 1.4])

    add_heading_2(doc, "5.2 Executive Communication Guidelines: Do's and Don'ts")
    add_bullet_point(doc, "DO Focus on Financial & Strategic Impact:", "Frame every analytical discovery in terms of protected revenue, customer lifetime value, and operational margin expansion.")
    add_bullet_point(doc, "DO Use Intuitive Business Analogies:", "Describe ROC-AUC as 'the model's ability to rank an at-risk subscriber above a happy subscriber 87 times out of 100.'")
    add_bullet_point(doc, "DON'T Overwhelm with Algorithmic Mechanics:", "Avoid lecturing the C-suite on Gini impurity, gradient boosting loss functions, or hyperparameter regularization math.")
    add_bullet_point(doc, "DON'T Present Raw Accuracy Metrics:", "Always clarify why an 80% accuracy score is deceptive in an imbalanced churn environment, using concrete cost examples.")

    add_heading_2(doc, "5.3 Jargon-to-Plain-Language Translation Matrix")
    doc.add_paragraph(
        "To ensure seamless communication between data science teams and executive leadership, technical jargon must be translated into plain business terms:"
    )
    jargon_headers = ["Technical Machine Learning Term", "Executive Plain-Language Translation", "Business Context Example"]
    jargon_data = [
        ["ROC-AUC = 0.865", "Discrimination Accuracy Score", "'The model correctly ranks an at-risk customer ahead of a retained customer 86.5% of the time.'"],
        ["Top Decile Recall = 73.4%", "High-Risk Capture Rate", "'Focusing on our top 20% highest-risk accounts successfully catches 73.4% of all future cancellations.'"],
        ["Stratified 5-Fold Cross-Validation", "Stress-Testing across Data Slices", "'We validated the model across 5 independent customer segments to ensure it generalizes to future subscribers.'"],
        ["SHAP Feature Attribution", "Customer 'Why' Reason Codes", "'The system provides frontline agents with the top 3 specific reasons a subscriber was flagged as at-risk.'"],
        ["Cost-Weighted Threshold (p* = 0.36)", "Profit-Maximizing Sensitivity Trigger", "'We calibrated the model trigger so we never risk losing a $500 customer just to save a $35 retention offer.'"],
        ["Population Stability Index (PSI)", "Model Health & Trend Drift Detector", "'An automated alarm that alerts our engineers if customer behavior changes significantly over time.'"]
    ]
    add_styled_table(doc, jargon_headers, jargon_data, [1.6, 2.0, 2.9])

    # Section 6
    add_heading_1(doc, "6. Strategic Recommendations & 90-Day Implementation Roadmap")
    doc.add_paragraph(
        "To ensure successful operational adoption and realize the projected $246,400 net ARR value creation, "
        "the deployment is structured into a disciplined 90-day phased execution roadmap:"
    )
    add_heading_2(doc, "6.1 Phase 1: Controlled Pilot & CS Alignment (Days 1–30)")
    add_bullet_point(doc, "Pilot Deployment:", "Deploy daily batch scoring output to a 10-person dedicated Customer Success pilot squad.")
    add_bullet_point(doc, "Surgical Targeting:", "Target accounts falling into Risk Deciles 1 and 2 (top 20% risk), deploying personalized contract migration offers.")
    add_bullet_point(doc, "Feedback Loop:", "Track daily outreach logs, customer response rates, and intervention conversion efficiency to calibrate outreach messaging.")

    add_heading_2(doc, "6.2 Phase 2: CRM & Enterprise Systems Integration (Days 31–60)")
    add_bullet_point(doc, "Automated Ingestion Pipeline:", "Automate daily data ingestion from billing, usage, and ticketing databases via scheduled Airflow DAGs.")
    add_bullet_point(doc, "CRM Native Integration:", "Write churn risk probabilities and the top 3 localized SHAP drivers directly into Salesforce and HubSpot contact cards.")
    add_bullet_point(doc, "Frontline Training:", "Conduct mandatory enablement workshops for all customer success managers, teaching interpretation of risk scores.")

    add_heading_2(doc, "6.3 Phase 3: Real-Time Serving & Continuous MLOps (Days 61–90)")
    add_bullet_point(doc, "Containerized REST API:", "Launch the containerized FastAPI microservice delivering sub-50ms inference for web portal and customer care calls.")
    add_bullet_point(doc, "Automated Drift Monitoring:", "Deploy automated Population Stability Index (PSI) and Kolmogorov-Smirnov monitoring dashboards.")
    add_bullet_point(doc, "Champion-Challenger Retraining:", "Establish bi-monthly automated retraining schedules with 14-day shadow validation before production promotion.")

    # Section 7
    add_heading_1(doc, "7. Conclusion & Long-Term Strategic Outlook")
    doc.add_paragraph(
        "This capstone report proves that an enterprise-grade, machine learning-powered predictive retention system delivers "
        "transformational operational and financial value to subscription telecommunications providers. "
        "By replacing slow, reactive damage-control processes with automated, probabilistic early warning signals 45 days in advance, "
        "the enterprise safeguards over $274,560 in Annual Recurring Revenue, captures 73.4% of all future churn events, and delivers an "
        "exceptional 875% program return on investment."
    )
    doc.add_paragraph(
        "The methodology, architectural flowcharts, and executive presentation framework established in this report provide a complete, "
        "scientifically sound, and boardroom-ready blueprint. Executive leadership is respectfully requested to approve the 90-day "
        "operational implementation roadmap and authorize Phase 1 pilot execution."
    )

    out_file = "Week4_Report_and_Presentation_Plan.docx"
    doc.save(out_file)
    print(f"Successfully generated '{out_file}' (Size: {os.path.getsize(out_file) / 1024:.1f} KB)")


if __name__ == '__main__':
    build_week4_docx()
