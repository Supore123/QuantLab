from utils.data_loader import load_data
from strategies.moving_average import MovingAverageStrategy
from strategies.bollinger_bands import BollingerBandsStrategy
from backtester.engine import BacktestEngine
import matplotlib.pyplot as plt
import os

# -----------------------------
# Settings
# -----------------------------
TICKER = "AAPL"
START_DATE = "2023-01-01"
END_DATE = "2025-01-01"
DATA_PATH = f"data/{TICKER}.csv"

# -----------------------------
# Load or download data
# -----------------------------
if os.path.exists(DATA_PATH):
    print(f"Loading data from {DATA_PATH}...")
    data = load_data(DATA_PATH)
else:
    print(f"Downloading {TICKER} data from Yahoo Finance...")
    data = load_data(TICKER, start=START_DATE, end=END_DATE)
    os.makedirs("data", exist_ok=True)
    data.to_csv(DATA_PATH, index=False)
    print(f"Saved data to {DATA_PATH}")

# -----------------------------
# Initialize strategies
# -----------------------------
ma_strategy = MovingAverageStrategy(data, short_window=10, long_window=50)
bb_strategy = BollingerBandsStrategy(data, window=20, num_std=2)

# -----------------------------
# Run backtests
# -----------------------------
engine_ma = BacktestEngine(ma_strategy)
engine_ma.run_backtest()

engine_bb = BacktestEngine(bb_strategy)
engine_bb.run_backtest()

# -----------------------------
# Print metrics
# -----------------------------
print("\n=== Moving Average Strategy ===")
engine_ma.print_metrics()

print("\n=== Bollinger Bands Strategy ===")
engine_bb.print_metrics()

# -----------------------------
# Plot comparison
# -----------------------------
plt.figure(figsize=(12,6))
plt.plot(data['date'], engine_ma.results, label='Moving Average', linewidth=2)
plt.plot(data['date'], engine_bb.results, label='Bollinger Bands', linewidth=2)
plt.plot(data['date'], data['close'], label='Asset Price', alpha=0.4, linestyle='--')
plt.legend()
plt.xlabel("Date")
plt.ylabel("Portfolio Value")
plt.title(f"Strategy Comparison: {TICKER}")
plt.show()
