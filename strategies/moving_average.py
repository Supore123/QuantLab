import pandas as pd

class MovingAverageStrategy:
    def __init__(self, data, short_window=10, long_window=50):
        self.data = data.copy()
        self.short_window = short_window
        self.long_window = long_window
        self.signals = pd.DataFrame(index=self.data.index)
        self.signals["signal"] = 0.0

    def generate_signals(self):
        # Compute moving averages
        self.data["short_ma"] = (
            self.data["close"].rolling(window=self.short_window, min_periods=1).mean()
        )
        self.data["long_ma"] = (
            self.data["close"].rolling(window=self.long_window, min_periods=1).mean()
        )

        # Buy when short MA > long MA, else sell
        self.signals.loc[:, "signal"] = 0
        self.signals.loc[self.data["short_ma"] > self.data["long_ma"], "signal"] = 1
        self.signals.loc[self.data["short_ma"] <= self.data["long_ma"], "signal"] = -1
        return self.signals
