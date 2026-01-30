from sklearn.pipeline import Pipeline
from xgboost import XGBClassifier
import joblib

def train_model(preprocessor,X_train,y_train):
    model = XGBClassifier(
        n_estimators=300,
        max_depth=4,
        learning_rate=0.05,
        subsample=0.8,
        colsample_bytree=0.8,
        eval_metric="logloss",
        random_state=42
    )

    pipeline = Pipeline([
        ("preprocessor",preprocessor),
        ("model",model)
    ])

    pipeline.fit(X_train,y_train)
    return pipeline

def save_model(model_pipeline, path="artifacts/churn_model.pkl"):
    joblib.dump(model_pipeline,path)