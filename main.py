from data_loader import load_data
from strategy import apply_sma_strategy
from backtest import backtest_strategy
from plot_results import plot_results

symbol = "AAPL"
data = load_data(symbol, start="2020-01-01", end="2023-01-01")
signals = apply_sma_strategy(data, short_window=20, long_window=50)
portfolio = backtest_strategy(signals)
plot_results(signals, portfolio)
