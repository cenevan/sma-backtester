import matplotlib.pyplot as plt

def plot_results(df, portfolio):
    fig, axs = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

    # Price and SMAs
    axs[0].plot(df.index, df['price'], label='Price')
    axs[0].plot(df.index, df['sma_short'], label='SMA Short')
    axs[0].plot(df.index, df['sma_long'], label='SMA Long')
    axs[0].set_title("Price with SMA Crossovers")
    axs[0].legend()

    # Portfolio value
    axs[1].plot(portfolio.index, portfolio['portfolio_value'], label='Portfolio Value', color='green')
    axs[1].set_title("Portfolio Value Over Time")
    axs[1].legend()

    plt.tight_layout()
    plt.show()
