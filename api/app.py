from fastapi import FastAPI
import joblib
import pandas as pd

from api.schemas import CustomerInput
from src.features.preprocess import add_engineered_features

from src.explainability.explain import generate_explanations

from src.explainability.risk import get_risk_level

from src.logging.logger import logger 

app = FastAPI(title="Customer Churn Prediction API")

#load trained model ONCE
model = joblib.load("artifacts/churn_model.pkl")

@app.post("/predict")
def predict_churn(customer: CustomerInput):

    # Convert input to DataFrame
    df = pd.DataFrame([customer.dict()])

    # 🚨 REQUIRED: same feature engineering as training
    df = add_engineered_features(df)

    # Predict probability
    churn_proba = float(model.predict_proba(df)[:, 1][0])

    churn_label = int(churn_proba >= 0.40)

    explanations = generate_explanations(df)

    risk_level = get_risk_level(churn_proba)

    logger.info(
        f"prob={round(churn_proba,4)} | "
        f"risk={risk_level} | "
        f"reasons={explanations}"
    )

    return {
        "churn_probability": round(churn_proba, 4),
        "risk_level" : risk_level, 
        "churn_prediction": churn_label,
        "top_reasons": explanations
    }

@app.get("/health")
def health_check():
    return{
        "status":"ok",
        "model_loaded":True
    }

