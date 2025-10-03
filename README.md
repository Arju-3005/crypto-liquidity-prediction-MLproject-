# 🚀 Cryptocurrency Liquidity Prediction for Market Stability

## 📌 Project Overview
Cryptocurrency markets are **highly volatile**, and liquidity plays a crucial role in ensuring **market stability**.  
In this project, we build a **Machine Learning model** that predicts cryptocurrency **liquidity levels** based on factors like trading volume, volatility, exchange listings, and social media activity.  

The objective is to **detect liquidity crises early** and help traders, investors, and financial institutions make **informed decisions**.  

---

## 📊 Problem Statement
Liquidity refers to the ease with which assets can be bought or sold **without drastically impacting the price**.  
A lack of liquidity can cause **increased price fluctuations** and **market instability**.  

This project aims to:  
- Predict cryptocurrency liquidity using **historical data**  
- Perform **feature engineering** (moving averages, volatility, liquidity ratios)  
- Build & evaluate **ML/DL models** for prediction  
- Deploy a simple **Streamlit/Flask app** for testing predictions  

---

## 📂 Project Structure 
---

## 🗂️ Dataset
- **Source:** [Google Drive Dataset (2016-2017)](https://drive.google.com/drive/folders/10BRgPip2Zj_56is3DilJCowjfyT6E9AM)  
- **Contents:** Historical cryptocurrency price, volume, and trading activity  

---

## 🔧 Steps in Project Development
1. **Data Collection** – Gather price, volume & liquidity data  
2. **Data Preprocessing** – Handle missing values, normalize features  
3. **EDA (Exploratory Data Analysis)** – Identify trends, correlations & distributions  
4. **Feature Engineering** – Create liquidity features (moving averages, volatility, ratios)  
5. **Model Selection** – Try ML (Random Forest, XGBoost) & DL (LSTM, GRU) models  
6. **Model Training & Tuning** – Train & optimize models with hyperparameter tuning  
7. **Evaluation** – Metrics: RMSE, MAE, R²  
8. **Deployment** – Local app using **Streamlit/Flask**  

---

## ⚙️ Tech Stack
- **Programming:** Python (Pandas, NumPy, Scikit-Learn, TensorFlow, PyTorch)  
- **Visualization:** Matplotlib, Seaborn, Plotly  
- **Deployment:** Streamlit / Flask  
- **Version Control:** Git, GitHub  

---

## 📈 Results & Insights
- Feature importance showed **trading volume & volatility** were the strongest predictors  
- Models tested: **Linear Regression, Random Forest, XGBoost, LSTM**  
- Best model achieved **R² = XX%**, **RMSE = XX** (to be updated after experiments)  

---

## 🚀 Deployment
Run the app locally:
```bash
streamlit run deployment/app.py
 