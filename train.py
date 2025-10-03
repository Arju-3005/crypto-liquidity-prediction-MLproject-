# src/train.py

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

def train_model(model, X, y, test_size=0.2, random_state=42):
    """
    Train a machine learning model and return trained model, RMSE, and R2 score.
    
    Parameters:
        model: scikit-learn compatible model
        X (DataFrame): Features
        y (Series): Target variable (Liquidity_Ratio)
        test_size (float): Fraction of data to use as test set
        random_state (int): Random seed
        
    Returns:
        model: Trained model
        rmse (float): Root Mean Squared Error on test set
        r2 (float): R2 score on test set
    """
    # Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    
    # Fit model
    model.fit(X_train, y_train)
    
    # Make predictions
    y_pred = model.predict(X_test)
    
    # Evaluation metrics
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)
    
    return model, rmse, r2
