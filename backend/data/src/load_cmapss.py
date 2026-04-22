import pandas as pd

COLS = (
    ['unit', 'cycle'] +
    [f'op_setting_{i+1}' for i in range(3)] +
    [f's{i+1}' for i in range(21)]
)

def load_data(path):
    return pd.read_csv(path, sep='\s+', header=None, names=COLS)

def add_rul(df):
    max_cycle = df.groupby('unit')['cycle'].transform('max')
    df['RUL'] = max_cycle - df['cycle']
    return df

def load_train(path):
    df = load_data(path)
    return add_rul(df)

def load_test(test_path, rul_path):
    test_df = load_data(test_path)
    rul = pd.read_csv(rul_path, header=None)[0]
    return test_df, rul