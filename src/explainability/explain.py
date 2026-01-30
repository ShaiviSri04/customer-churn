def generate_explanations(df_row):
    reasons=[]

    if df_row["Contract"].iloc[0] == "Month-to-month":
        reasons.append("Month-to-month contract increases churn risk")

    if df_row["tenure"].iloc[0] < 12:
        reasons.append("Low tenure increases churn risk")

    if df_row["MonthlyCharges"].iloc[0] > 70:
        reasons.append("High monthly charges increase churn risk")
    
    if df_row["TechSupport"].iloc[0] == "No":
        reasons.append("No tech support increases churn risk")

    if df_row["PaymentMethod"].iloc[0] == "Electronic check":
        reasons.append("Electronic check payment method increases churn risk")

    return reasons