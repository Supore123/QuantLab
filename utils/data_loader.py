import pandas as pd
import yfinance as yf

def load_data(ticker_or_path, start="2023-01-01", end="2025-01-01"):
    """
    Load historical data from CSV or Yahoo Finance.
    """
    try:
        # Try loading as CSV
        df = pd.read_csv(ticker_or_path, parse_dates=['date'])
    except FileNotFoundError:
        # If file not found, fetch from Yahoo Finance
        df = yf.download(ticker_or_path, start=start, end=end)
        df.reset_index(inplace=True)
    df = df[['Date','Open','High','Low','Close','Volume']] if 'Date' in df.columns else df
    df.columns = ['date','open','high','low','close','volume']
    df.sort_values('date', inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df
# Data loader placeholder
