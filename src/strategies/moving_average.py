import pandas as pd

def moving_average_strategy(data: pd.DataFrame, short_window: int = 20, long_window: int = 50):
    """Simple moving average crossover strategy."""
    data = data.copy()

    if "Close" not in data.columns:
        raise ValueError("Data must contain a 'Close' column.")
    if not pd.api.types.is_numeric_dtype(data["Close"]):
        raise TypeError("'Close' column must be numeric.")

    data["SMA_short"] = data["Close"].rolling(short_window, min_periods=1).mean()
    data["SMA_long"] = data["Close"].rolling(long_window, min_periods=1).mean()
    data["Signal"] = 0
    data.loc[data["SMA_short"] > data["SMA_long"], "Signal"] = 1
    data.loc[data["SMA_short"] <= data["SMA_long"], "Signal"] = -1
    return data
