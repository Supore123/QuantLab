from pathlib import Path
import pandas as pd
from src.utils.data_loader import load_data
from src.strategies.moving_average import moving_average_strategy
from src.strategies.bollinger_bands import bollinger_bands_strategy
from src.strategies.rsi import rsi_strategy
from src.backtest import run_backtest
from src.utils.plotter import plot_backtest_multi

# Load tickers
tickers_df = pd.read_csv("tickers.csv")  # CSV with column 'Ticker'
tickers = tickers_df['Ticker'].tolist()

save_dir = Path("notebooks/plots")
save_dir.mkdir(parents=True, exist_ok=True)

all_results = []

for ticker in tickers:
    print(f"Running backtest for {ticker}...")

    # Load and prepare data
    df = load_data(ticker)
    df = moving_average_strategy(df)
    df = bollinger_bands_strategy(df)
    df = rsi_strategy(df)

    # Run SMA backtest
    results = run_backtest(df)
    results['Ticker'] = ticker
    all_results.append(results)

    # Compute equity curve for plotting
    df["Equity_Curve"] = (1 + df["Signal"].shift(1) * df["Close"].pct_change()).cumprod() * 10000

    # Save annotated plot
    plot_backtest_multi(df,
                        title=f"{ticker} Multi-Strategy Backtest",
                        save_path=save_dir / f"{ticker}_multi_backtest.png",
                        initial_capital=10000)

# Save all results to CSV for analysis
results_df = pd.DataFrame(all_results)
results_df.to_csv("notebooks/plots/all_tickers_results.csv", index=False)
print("✅ Backtests completed for all tickers!")
