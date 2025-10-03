import streamlit as st
import pandas as pd
from src.data_preprocessing import load_data, handle_missing_values
from src.models import get_models

st.title("Cryptocurrency Liquidity Prediction")

uploaded_file = st.file_uploader("Upload CSV", type="csv")

if uploaded_file:
    df = load_data(uploaded_file)
    df = handle_missing_values(df)
    st.write("Preview of data:")
    st.dataframe(df.head())

    # Dummy model selection
    models = get_models()
    st.write("Available models:", list(models.keys()))
