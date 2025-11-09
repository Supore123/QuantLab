import pandas as pd

def run_backtest(data: pd.DataFrame, initial_balance: float = 10000):
    """Run a simple backtest using provided trading signals."""
    data = data.copy()
    data["Returns"] = data["Close"].pct_change()
    data["Strategy_Returns"] = data["Signal"].shift(1) * data["Returns"]
    data["Equity_Curve"] = (1 + data["Strategy_Returns"]).cumprod() * initial_balance

    final_value = data["Equity_Curve"].iloc[-1]
    total_return = (final_value / initial_balance - 1) * 100
    sharpe_ratio = (
        data["Strategy_Returns"].mean() / data["Strategy_Returns"].std() * (252 ** 0.5)
        if data["Strategy_Returns"].std() != 0 else 0
    )

    return {
        "Final Portfolio Value": round(final_value, 2),
        "Total Return (%)": round(total_return, 2),
        "Sharpe Ratio": round(sharpe_ratio, 2),
    }

