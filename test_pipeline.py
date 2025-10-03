import pytest
import pandas as pd
from src.train import train_model
from src.models import get_models

def test_train_model():
    # Use 20 samples to avoid R² undefined problem
    df = pd.DataFrame({
        'Feature1': list(range(1, 21)),
        'Feature2': list(range(20, 0, -1)),
        'Liquidity_Ratio': [10, 15, 20, 25, 30, 35, 40, 45, 50, 55,
                            60, 65, 70, 75, 80, 85, 90, 95, 100, 105]
    })

    X = df[['Feature1', 'Feature2']]
    y = df['Liquidity_Ratio']

    model = get_models()['LinearRegression']
    trained_model, rmse, r2 = train_model(model, X, y)

    # Check metrics
    assert rmse >= 0, "RMSE should be non-negative"
    assert -1 <= r2 <= 1, "R² score should be in range [-1, 1]"


