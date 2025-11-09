import pandas as pd

class BollingerBandsStrategy:
    def __init__(self, data, window=20, num_std=2):
        self.data = data.copy()
        self.window = window
        self.num_std = num_std
        self.signals = pd.DataFrame(index=self.data.index)
        self.signals["signal"] = 0.0

    def generate_signals(self):
        # Compute rolling mean and std
        self.data["rolling_mean"] = self.data["close"].rolling(self.window).mean()
        self.data["rolling_std"] = self.data["close"].rolling(self.window).std()

        # Upper and lower bands
        self.data["upper_band"] = self.data["rolling_mean"] + (self.data["rolling_std"] * self.num_std)
        self.data["lower_band"] = self.data["rolling_mean"] - (self.data["rolling_std"] * self.num_std)

        # Generate buy/sell signals
        self.signals.loc[self.data["close"] < self.data["lower_band"], "signal"] = 1   # Buy
        self.signals.loc[self.data["close"] > self.data["upper_band"], "signal"] = -1  # Sell
        self.signals["signal"].fillna(method="ffill", inplace=True)

        return self.signals

