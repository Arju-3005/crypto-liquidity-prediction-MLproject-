from src.models import get_models

def test_get_models():
    models = get_models()
    assert 'LinearRegression' in models, "LinearRegression missing"
    assert 'RandomForest' in models, "RandomForest missing"
