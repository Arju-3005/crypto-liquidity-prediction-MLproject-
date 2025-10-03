def add_moving_average(df, column, window=5):
    df[f'{column}_MA{window}'] = df[column].rolling(window).mean()
    return df

def add_volatility(df, column, window=5):
    df[f'{column}_Vol{window}'] = df[column].rolling(window).std()
    return df

def add_liquidity_ratio(df, volume_col, price_col):
    df['Liquidity_Ratio'] = df[volume_col] / df[price_col]
    return df
