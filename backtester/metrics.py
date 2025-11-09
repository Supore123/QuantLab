import numpy as np

def sharpe_ratio(portfolio_values):
    returns = np.diff(portfolio_values) / portfolio_values[:-1]
    return np.mean(returns) / np.std(returns) * np.sqrt(252)  # Annualized

def max_drawdown(portfolio_values):
    cumulative_max = np.maximum.accumulate(portfolio_values)
    drawdown = (cumulative_max - portfolio_values) / cumulative_max
    return np.max(drawdown)
# Metrics calculation placeholder
