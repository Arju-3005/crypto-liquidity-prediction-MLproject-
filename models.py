from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression

def get_models():
    """Return dictionary of ML models."""
    models = {
        'LinearRegression': LinearRegression(),
        'RandomForest': RandomForestRegressor(n_estimators=100, random_state=42)
    }
    return models
