import pandas as pd

class Portfolio:
    def __init__(self, data, signals, initial_cash=10000):
        self.data = data.copy()
        self.signals = signals.copy()
        self.initial_cash = initial_cash

    def backtest(self):
        df = pd.DataFrame(index=self.data.index)
        df["price"] = self.data["close"]
        df["signal"] = self.signals["signal"]

        # Shift signal so trade happens next day
        df["position"] = df["signal"].shift(1).fillna(0)

        # Daily returns
        df["returns"] = df["price"].pct_change().fillna(0)

        # Strategy returns (position * daily return)
        df["strategy_returns"] = df["position"] * df["returns"]

        # Portfolio value over time
        df["portfolio_value"] = self.initial_cash * (1 + df["strategy_returns"]).cumprod()

        self.results = df
        return df["portfolio_value"]
