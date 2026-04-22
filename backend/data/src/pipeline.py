import os
import pandas as pd
import numpy as np
import json

from load_cmapss import load_train
from preprocess import clean, add_features, get_features, scale
from windowing import create_sequences

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RAW_PATH = os.path.join(BASE_DIR, "../../data/raw/train_FD001.txt")
OUT_DIR = os.path.join(BASE_DIR, "../../data/processed")

os.makedirs(OUT_DIR, exist_ok=True)

def run_pipeline():
    print("Loading data...")
    df = load_train(RAW_PATH)

    print("Cleaning...")
    df = clean(df)

    print("Feature Engineering...")
    df = add_features(df)

    features = get_features(df)

    print("Scaling...")
    scaler_path = os.path.join(OUT_DIR, "scaler.pkl")
    df = scale(df, features, scaler_path)

    print("Saving processed data...")
    df.to_parquet(os.path.join(OUT_DIR, "processed.parquet"))

    with open(os.path.join(OUT_DIR, "features.json"), "w") as f:
        json.dump(features, f)

    print("Creating sequences...")
    X, y = create_sequences(df, features)

    np.save(os.path.join(OUT_DIR, "X.npy"), X)
    np.save(os.path.join(OUT_DIR, "y.npy"), y)

    print("Done!")
    print("Shape:", X.shape, y.shape)

if __name__ == "__main__":
    run_pipeline()