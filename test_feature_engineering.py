import pandas as pd
from src.feature_engineering import add_moving_average, add_volatility, add_liquidity_ratio

def test_add_moving_average():
    df = pd.DataFrame({'Close': [1, 2, 3, 4, 5]})
    df_ma = add_moving_average(df, 'Close', window=2)
    assert 'Close_MA2' in df_ma.columns, "Moving average column not added"

def test_add_volatility():
    df = pd.DataFrame({'Close': [1, 2, 3, 4, 5]})
    df_vol = add_volatility(df, 'Close', window=2)
    assert 'Close_Vol2' in df_vol.columns, "Volatility column not added"

def test_add_liquidity_ratio():
    df = pd.DataFrame({'Volume': [100, 200], 'Close': [10, 20]})
    df_ratio = add_liquidity_ratio(df, 'Volume', 'Close')
    assert 'Liquidity_Ratio' in df_ratio.columns, "Liquidity ratio column not added"
