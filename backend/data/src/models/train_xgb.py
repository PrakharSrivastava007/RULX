import pandas as pd
import xgboost as xgb
import joblib
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.abspath(os.path.join(BASE_DIR, "../../../data/processed"))
MODEL_DIR = os.path.abspath(os.path.join(BASE_DIR, "../../../models"))

os.makedirs(MODEL_DIR, exist_ok=True)

def load_data():
    df = pd.read_parquet(os.path.join(DATA_DIR, "processed.parquet"))
    
    with open(os.path.join(DATA_DIR, "features.json")) as f:
        features = json.load(f)

    X = df[features]
    y = df['RUL']

    return X, y

def train():
    X, y = load_data()

    model = xgb.XGBRegressor(
        n_estimators=200,
        max_depth=6,
        learning_rate=0.05,
        subsample=0.8,
        colsample_bytree=0.8
    )

    model.fit(X, y)

    joblib.dump(model, os.path.join(MODEL_DIR, "xgb_model.pkl"))
    print("XGBoost model saved!")

if __name__ == "__main__":
    train()