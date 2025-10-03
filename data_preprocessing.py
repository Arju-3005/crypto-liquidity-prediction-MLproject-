import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_data(file_path):
    """Load CSV data."""
    return pd.read_csv(file_path)

def handle_missing_values(df):
    """Fill or drop missing values."""
    return df.ffill()


def normalize_features(df, columns):
    """Normalize selected numerical features."""
    scaler = StandardScaler()
    df[columns] = scaler.fit_transform(df[columns])
    return df
