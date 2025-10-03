import matplotlib.pyplot as plt
import seaborn as sns

def plot_correlation(df):
    plt.figure(figsize=(10,8))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
    plt.show()

def plot_trend(df, column):
    plt.figure(figsize=(12,6))
    plt.plot(df[column])
    plt.title(f'Trend of {column}')
    plt.show()
