import argparse
import yfinance as yf
from pathlib import Path

def download_data(ticker: str, start: str, end: str, save_path: str = "data/raw"):
    """Download OHLC stock data and save to CSV."""
    Path(save_path).mkdir(parents=True, exist_ok=True)
    print(f"📥 Downloading {ticker} data from {start} to {end}...")
    df = yf.download(ticker, start=start, end=end)
    file_path = Path(save_path) / f"{ticker}.csv"
    df.to_csv(file_path)
    print(f"✅ Saved data to {file_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download stock data using yfinance")
    parser.add_argument("--ticker", required=True, help="Ticker symbol (e.g. AAPL)")
    parser.add_argument("--start", required=True, help="Start date (YYYY-MM-DD)")
    parser.add_argument("--end", required=True, help="End date (YYYY-MM-DD)")
    args = parser.parse_args()
    download_data(args.ticker, args.start, args.end)

