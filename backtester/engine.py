import matplotlib.pyplot as plt
from .portfolio import Portfolio
from .metrics import sharpe_ratio, max_drawdown

class BacktestEngine:
    def __init__(self, strategy):
        self.strategy = strategy
        self.data = strategy.data
        self.signals = strategy.generate_signals()
        self.portfolio = Portfolio(self.data, self.signals)

    def run_backtest(self):
        self.results = self.portfolio.backtest()

    def print_metrics(self):
        print(f"Sharpe Ratio: {sharpe_ratio(self.results):.2f}")
        print(f"Max Drawdown: {max_drawdown(self.results)*100:.2f}%")
        print(f"Final Portfolio Value: ${self.results.iloc[-1]:.2f}")

    def plot_results(self):
        plt.figure(figsize=(12,6))
        plt.plot(self.data['date'], self.results, label='Portfolio Value')
        plt.plot(self.data['date'], self.data['close'], label='Asset Price', alpha=0.5)
        plt.legend()
        plt.xlabel("Date")
        plt.ylabel("Portfolio / Price")
        plt.title("Backtest Results")
        plt.show()
# Backtesting engine placeholder
