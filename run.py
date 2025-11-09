from utils.data_loader import load_data
from strategies.moving_average import MovingAverageStrategy
from backtester.engine import BacktestEngine
import os

# -----------------------------
# Settings
# -----------------------------
TICKER = "AAPL"                # Stock ticker to download
START_DATE = "2023-01-01"      # Start of historical data
END_DATE = "2025-01-01"        # End of historical data
DATA_PATH = f"data/{TICKER}.csv"  # Local CSV path to save data

# -----------------------------
# Step 1: Load historical data
# -----------------------------
if os.path.exists(DATA_PATH):
    print(f"Loading data from {DATA_PATH}...")
    data = load_data(DATA_PATH)
else:
    print(f"Downloading {TICKER} data from Yahoo Finance...")
    data = load_data(TICKER, start=START_DATE, end=END_DATE)
    os.makedirs("data", exist_ok=True)
    data.to_csv(DATA_PATH, index=False)
    print(f"Saved downloaded data to {DATA_PATH}")

# -----------------------------
# Step 2: Initialize strategy
# -----------------------------
strategy = MovingAverageStrategy(data, short_window=10, long_window=50)

# -----------------------------
# Step 3: Run backtest
# -----------------------------
engine = BacktestEngine(strategy)
engine.run_backtest()

# -----------------------------
# Step 4: Print metrics
# -----------------------------
engine.print_metrics()

# -----------------------------
# Step 5: Plot results
# -----------------------------
engine.plot_results()
