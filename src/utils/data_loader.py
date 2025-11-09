import pandas as pd
from pathlib import Path

def load_data(ticker: str, data_path: str = "data/raw"):
    """Load and clean stock data for a given ticker."""
    file_path = Path(data_path) / f"{ticker}.csv"
    if not file_path.exists():
        raise FileNotFoundError(f"Data file not found: {file_path}")

    df = pd.read_csv(file_path)

    # If 'Date' exists, make it the index
    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
        df.set_index("Date", inplace=True)
    else:
        df.index = pd.to_datetime(df.index, errors="coerce")

    # Clean column names and ensure numeric types
    df.columns = [c.strip().capitalize() for c in df.columns]
    for col in ["Open", "High", "Low", "Close", "Adj close", "Volume"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # Drop any rows missing essential data
    df.dropna(subset=["Close"], inplace=True)
    return df
