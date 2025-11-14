import argparse
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from src.utils.data_loader import load_data

DATA_PATH = Path("data")
RESULTS_CSV = DATA_PATH / "all_tickers_results.csv"
PLOTS_PATH = DATA_PATH / "plots"
PLOTS_PATH.mkdir(parents=True, exist_ok=True)

def run_backtest(ticker, start="2023-01-01", end="2025-01-01", save_plot=True):
    df = load_data(ticker, start=start, end=end, save_path=DATA_PATH / "raw")
    df['Return'] = df['Close'].pct_change()
    total_return = df['Return'].sum()
    volatility = df['Return'].std()

    if save_plot:
        plt.figure(figsize=(10, 5))
        df['Close'].plot(title=f"{ticker} Closing Prices")
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.tight_layout()
        plt.savefig(PLOTS_PATH / f"{ticker}.png")
        plt.close()

    return {"Ticker": ticker, "Total Return": total_return, "Volatility": volatility}

def main(no_plot=False):
    tickers = pd.read_csv(DATA_PATH / "sp100_tickers.csv")['Ticker'].tolist()
    results = []

    for ticker in tickers:
        try:
            print(f"⏳ Running backtest for {ticker}...")
            res = run_backtest(ticker, save_plot=not no_plot)
            results.append(res)
        except Exception as e:
            print(f"⚠️ Failed for {ticker}: {e}")

    df_results = pd.DataFrame(results)
    df_results.to_csv(RESULTS_CSV, index=False)
    print(f"✅ All backtests completed. Metrics saved to '{RESULTS_CSV}'")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--no-plot", action="store_true", help="Run backtests without displaying plots")
    args = parser.parse_args()
    main(no_plot=args.no_plot)

