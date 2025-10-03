import pandas as pd
from src.data_preprocessing import handle_missing_values, normalize_features

def test_handle_missing_values():
    df = pd.DataFrame({'A': [1, None, 3], 'B': [4, 5, None]})
    df_clean = handle_missing_values(df)
    assert df_clean.isnull().sum().sum() == 0, "Missing values not handled correctly"

def test_normalize_features():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    df_norm = normalize_features(df, ['A', 'B'])
    assert df_norm['A'].mean() < 1e-6, "Normalization failed"
    assert df_norm['B'].mean() < 1e-6, "Normalization failed"
