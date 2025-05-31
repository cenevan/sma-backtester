import yfinance as yf

def load_data(symbol, start, end):
    df = yf.download(symbol, start=start, end=end)
    df = df[['Close']]
    df.rename(columns={'Close': 'price'}, inplace=True)
    return df
