from src.data.load_data import load_data
from src.features.preprocess import build_preprocessor
from src.features.preprocess import add_engineered_features
from src.models.train import train_model, save_model
from src.evaluation.metrics import evaluate
from sklearn.model_selection import train_test_split
import mlflow
import mlflow.sklearn 

mlflow.set_experiment("customer_churn")

if __name__ == "__main__":
    df = load_data("data/Telco-Customer-Churn.csv")
    print(df.shape)
    print(df.head())

    df = add_engineered_features(df)

    X = df.drop(columns=["Churn"])
    df["Churn"] = df["Churn"].str.strip()
    y = df["Churn"].map({"Yes": 1, "No": 0}).astype(int)

    categorical_features = [
        "gender", "Partner", "Dependents", "PhoneService",
        "MultipleLines", "InternetService", "OnlineSecurity",
        "OnlineBackup", "DeviceProtection", "TechSupport",
        "StreamingTV", "StreamingMovies", "Contract",
        "PaperlessBilling", "PaymentMethod"
    ]

    numerical_features = [
        "SeniorCitizen", "tenure",
        "MonthlyCharges", "TotalCharges_numeric"
    ]

    preprocessor = build_preprocessor(
        categorical_features,
        numerical_features
    )

    X_transformed = preprocessor.fit_transform(X)
    print("Transformed shape:",X_transformed.shape)

    X_train,X_test,y_train,y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        stratify=y,
        random_state=42
    )


    with mlflow.start_run():

       model_pipeline = train_model(preprocessor, X_train, y_train)
       save_model(model_pipeline)
       print("Model trained and saved")

       y_proba = model_pipeline.predict_proba(X_test)[:, 1]
       metrics = evaluate(y_test, y_proba)

       print("Evaluation metrics:")
       for k, v in metrics.items():
           print(f"{k}: {v:.4f}")
           mlflow.log_metric(k, v)

       mlflow.sklearn.log_model(model_pipeline, name="model")
