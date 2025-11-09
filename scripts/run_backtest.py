from pathlib import Path
from src.utils.data_loader import load_data
from src.strategies.moving_average import moving_average_strategy
from src.strategies.bollinger_bands import bollinger_bands_strategy
from src.strategies.rsi import rsi_strategy
from src.backtest import run_backtest
from src.utils.plotter import plot_backtest_multi

ticker = "AAPL"
df = load_data(ticker)

# Apply strategies
df = moving_average_strategy(df)
df = bollinger_bands_strategy(df)
df = rsi_strategy(df)

# Run backtest (currently using SMA signals)
results = run_backtest(df)
print(results)

# Equity curve for visualization
df["Equity_Curve"] = (1 + df["Signal"].shift(1) * df["Close"].pct_change()).cumprod() * 10000

# Save plot
save_dir = Path("notebooks/plots")
save_dir.mkdir(parents=True, exist_ok=True)

plot_backtest_multi(df,
                    title=f"{ticker} Multi-Strategy Backtest",
                    save_path=save_dir / f"{ticker}_multi_backtest.png",
                    initial_capital=10000)
