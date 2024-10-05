import pandas as pd

def load_csv(file):
    df = pd.read_csv(file, delimiter=',')
    df['date_added'] = pd.to_datetime(df['date_added'], format='%Y-%m-%d %H:%M:%S', errors='coerce')
    return df