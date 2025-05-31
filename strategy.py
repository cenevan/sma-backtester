def apply_sma_strategy(df, short_window=20, long_window=50):
    df = df.copy()
    df['sma_short'] = df['price'].rolling(window=short_window).mean()
    df['sma_long'] = df['price'].rolling(window=long_window).mean()
    df['signal'] = 0
    df.loc[df['sma_short'] > df['sma_long'], 'signal'] = 1
    df.loc[df['sma_short'] < df['sma_long'], 'signal'] = -1
    df['positions'] = df['signal'].diff()
    return df
