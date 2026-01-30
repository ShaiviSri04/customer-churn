import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder,StandardScaler\

def add_engineered_features(df : pd.DataFrame) -> pd.DataFrame:
    df=df.copy()

    df["TotalCharges_numeric"] = pd.to_numeric(
        df["TotalCharges"],
        errors="coerce"
    )

    return df

def build_preprocessor(cat_features,num_features):
    return ColumnTransformer(
        transformers=[
            ("num",StandardScaler(),num_features),
            ("cat",OneHotEncoder(handle_unknown="ignore", sparse_output=False),cat_features)
        ]
    )

