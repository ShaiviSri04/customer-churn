def get_risk_level(churn_probability: float) -> str:
    if churn_probability < 0.20:
        return "Low"
    elif churn_probability < 0.50:
        return "Medium"
    else:
        return "High"