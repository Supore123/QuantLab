import pandas as pd
from download_data import download_data

tickers = pd.read_csv("tickers.csv")['Ticker'].tolist()

for ticker in tickers:
    download_data(ticker, start="2018-01-01", end="2025-11-01")

