import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GRU, Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.abspath(os.path.join(BASE_DIR, "../../../data/processed"))
MODEL_DIR = os.path.abspath(os.path.join(BASE_DIR, "../../../models"))
print("DATA_DIR:", DATA_DIR)

os.makedirs(MODEL_DIR, exist_ok=True)

def load_data():
    X = np.load(os.path.join(DATA_DIR, "X.npy"))
    y = np.load(os.path.join(DATA_DIR, "y.npy"))
    return X, y

def build_model(input_shape):
    model = Sequential([
        GRU(64, return_sequences=True, input_shape=input_shape),
        Dropout(0.2),
        GRU(32),
        Dropout(0.2),
        Dense(16, activation='relu'),
        Dense(1)
    ])
    
    model.compile(
        optimizer='adam',
        loss='mse',
        metrics=['mae']
    )
    return model

def train():
    X, y = load_data()

    # Train-validation split
    split = int(0.8 * len(X))
    X_train, X_val = X[:split], X[split:]
    y_train, y_val = y[:split], y[split:]

    model = build_model((X.shape[1], X.shape[2]))

    early_stop = EarlyStopping(
        monitor='val_loss',
        patience=5,
        restore_best_weights=True
    )

    model.fit(
        X_train, y_train,
        validation_data=(X_val, y_val),
        epochs=30,
        batch_size=64,
        callbacks=[early_stop],
        verbose=1
    )

    model.save(os.path.join(MODEL_DIR, "gru_model.h5"))
    print("GRU model saved!")

if __name__ == "__main__":
    train()