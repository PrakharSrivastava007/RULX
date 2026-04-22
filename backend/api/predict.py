import math

import numpy as np
import joblib
import json
import os
from tensorflow.keras.models import load_model

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_DIR = os.path.abspath(os.path.join(BASE_DIR, "../models"))
DATA_DIR = os.path.abspath(os.path.join(BASE_DIR, "../data/processed"))

# Load models
gru_model = load_model(os.path.join(MODEL_DIR, "gru_model.h5"), compile=False)
xgb_model = joblib.load(os.path.join(MODEL_DIR, "xgb_model.pkl"))

# Load scaler and features
scaler = joblib.load(os.path.join(DATA_DIR, "scaler.pkl"))

with open(os.path.join(DATA_DIR, "features.json")) as f:
    FEATURES = json.load(f)


# ----------- CORE FUNCTIONS -----------

def predict_gru(sequence):
    sequence = np.array(sequence)
    sequence = np.expand_dims(sequence, axis=0)
    return float(gru_model.predict(sequence)[0][0])


def predict_xgb(row):
    row = scaler.transform([row])
    return float(xgb_model.predict(row)[0])


def calculate_probability(rul, threshold=50):
    prob = 1 / (1 + math.exp(rul / 50))
    return round(prob, 2)


def calculate_days(rul, cycle_time=0.5):
    return round(rul * cycle_time, 2)


# ----------- MAIN FUNCTION -----------

def predict_all(sequence):
    """
    sequence: list of last N cycles (same format as training)
    """
    sequence = np.array(sequence)

    if len(sequence.shape) != 2:
        raise ValueError("Input must be 2D array")

    if sequence.shape[0] != 30:
        raise ValueError("Sequence must have 30 timesteps")
    
    # GRU prediction
    rul_gru = predict_gru(sequence)

    # XGB uses last row
    last_row = sequence[-1]
    rul_xgb = predict_xgb(last_row)

    # Average prediction (simple ensemble)
    rul = (rul_gru + rul_xgb) / 2
    rul = max(0,min(rul, 125))  # Cap at max RUL
    
    probability = calculate_probability(rul)
    days = calculate_days(rul)

    return {
        "rul": round(rul, 2),
        "probability": probability,
        "days_to_failure": days
    }