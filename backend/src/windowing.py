import numpy as np

def create_sequences(df, features, seq_len=30):
    X, y = [], []

    for unit in df['unit'].unique():
        data = df[df['unit'] == unit].sort_values('cycle')
        values = data[features].values
        rul = data['RUL'].values

        for i in range(len(values) - seq_len):
            X.append(values[i:i+seq_len])
            y.append(rul[i+seq_len])

    return np.array(X), np.array(y)