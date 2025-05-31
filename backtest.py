def backtest_strategy(df, initial_cash=10000):
    df = df.copy()
    df['position'] = df['signal'].shift(1).fillna(0)
    df['daily_return'] = df['price'].pct_change()
    df['strategy_return'] = df['daily_return'] * df['position']
    df['portfolio_value'] = (1 + df['strategy_return']).cumprod() * initial_cash
    return df
