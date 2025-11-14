import pandas as pd
from pathlib import Path
import yfinance as yf

def load_data(ticker_or_path, start=None, end=None, save_path="data/raw"):
    file_path = Path(save_path) / f"{ticker_or_path}.csv"

    if file_path.exists():
        try:
            # Let pandas automatically parse dates from the index column
            df = pd.read_csv(file_path, index_col="Date", parse_dates=True)
            print(f"📂 Loaded local data for {ticker_or_path} (with 'Date' column)")
        except ValueError:
            # fallback if no 'Date' column exists
            df = pd.read_csv(file_path, index_col=0, parse_dates=True)
            print(f"📂 Loaded local data for {ticker_or_path} (index as date)")
    else:
        if start is None or end is None:
            raise ValueError("Must provide start and end dates if downloading data")
        df = yf.download(ticker_or_path, start=start, end=end)
        Path(save_path).mkdir(parents=True, exist_ok=True)
        df.to_csv(file_path)
        print(f"✅ Saved downloaded data to {file_path}")

    # --- CLEAN COLUMN NAMES AND FORCE NUMERIC ---
    df.columns = df.columns.str.strip()  # remove spaces
    for col in ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    df.dropna(subset=['Close'], inplace=True)  # remove rows where Close is NaN
    return df
