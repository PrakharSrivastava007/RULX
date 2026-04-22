import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib

SENSORS = [f's{i+1}' for i in range(21)]
OPS = [f'op_setting_{i+1}' for i in range(3)]

def clean(df):
    df = df.sort_values(['unit', 'cycle']).reset_index(drop=True)
    return df

def add_features(df):
    df = df.copy()

    # Rolling mean
    for s in SENSORS:
        df[f'{s}_rm'] = df.groupby('unit')[s].rolling(5, min_periods=1).mean().reset_index(0, drop=True)

    # Difference
    for s in SENSORS:
        df[f'{s}_diff'] = df.groupby('unit')[s].diff().fillna(0)

    return df

def get_features(df):
    features = OPS + SENSORS
    features += [f'{s}_rm' for s in SENSORS]
    features += [f'{s}_diff' for s in SENSORS]
    return features

def scale(df, feature_cols, save_path):
    scaler = StandardScaler()
    df[feature_cols] = scaler.fit_transform(df[feature_cols])

    joblib.dump(scaler, save_path)
    return df