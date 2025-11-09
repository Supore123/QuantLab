import matplotlib.pyplot as plt

def plot_backtest_multi(data, title="Backtest Multi-Strategy", save_path=None, initial_capital=10000):
    """
    Plot price, equity curve, SMA, Bollinger Bands, RSI signals, and buy/sell annotations.
    """
    plt.figure(figsize=(16,8))

    # Price
    plt.plot(data.index, data['Close'], label='Close Price', color='black', alpha=0.6)

    # SMA lines
    if 'SMA_short' in data.columns:
        plt.plot(data.index, data['SMA_short'], label='SMA Short', color='orange')
    if 'SMA_long' in data.columns:
        plt.plot(data.index, data['SMA_long'], label='SMA Long', color='purple')

    # Bollinger Bands
    if 'Upper_Band' in data.columns and 'Lower_Band' in data.columns:
        plt.plot(data.index, data['Upper_Band'], label='Upper BB', color='red', linestyle='--')
        plt.plot(data.index, data['Lower_Band'], label='Lower BB', color='green', linestyle='--')

    # Equity curve
    if 'Equity_Curve' in data.columns:
        plt.plot(data.index, data['Equity_Curve'], label='Equity Curve', color='blue', linewidth=2)

    # Signals
    signal_cols = [c for c in ['Signal', 'BB_Signal', 'RSI_Signal'] if c in data.columns]
    colors = {'Signal':'lime','BB_Signal':'cyan','RSI_Signal':'magenta'}
    markers = {'Signal':'^','BB_Signal':'o','RSI_Signal':'s'}
    for col in signal_cols:
        buys = data[data[col]==1]
        sells = data[data[col]==-1]
        plt.scatter(buys.index, buys['Close'], marker=markers[col], color=colors[col], s=80, label=f'{col} Buy')
        plt.scatter(sells.index, sells['Close'], marker=markers[col], color=colors[col], s=80, label=f'{col} Sell')

    # Metrics annotation
    final_value = data["Equity_Curve"].iloc[-1]
    total_return = (final_value / initial_capital - 1) * 100
    plt.text(0.02, 0.95, f"Final Portfolio: ${final_value:,.2f}\nTotal Return: {total_return:.2f}%",
             transform=plt.gca().transAxes, fontsize=12, verticalalignment='top', bbox=dict(boxstyle="round", facecolor="white", alpha=0.5))

    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Price / Portfolio Value")
    plt.legend()
    plt.grid(True)

    if save_path:
        plt.savefig(save_path, bbox_inches='tight')
        print(f"✅ Plot saved to {save_path}")

    plt.show()
