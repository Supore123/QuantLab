import numpy as np
from scipy import stats

def sharpe_ratio(portfolio_values):
    """Annualized Sharpe ratio"""
    returns = np.diff(portfolio_values) / portfolio_values[:-1]
    return np.mean(returns) / np.std(returns) * np.sqrt(252)

def max_drawdown(portfolio_values):
    """Maximum drawdown from peak"""
    cumulative_max = np.maximum.accumulate(portfolio_values)
    drawdown = (cumulative_max - portfolio_values) / cumulative_max
    return np.max(drawdown)

def calmar_ratio(portfolio_values):
    """Annualized return / Maximum drawdown"""
    annual_return = (portfolio_values[-1]/portfolio_values[0])**(252/len(portfolio_values)) - 1
    max_dd = max_drawdown(portfolio_values)
    return annual_return / max_dd if max_dd > 0 else 0

def sortino_ratio(returns, target_return=0):
    """Sharpe-like ratio that only penalizes downside volatility"""
    downside_returns = returns[returns < target_return]
    if len(downside_returns) == 0:
        return 0
    downside_std = np.std(downside_returns)
    return (np.mean(returns) - target_return) / downside_std * np.sqrt(252) if downside_std > 0 else 0

def information_ratio(strategy_returns, benchmark_returns):
    """Risk-adjusted excess return vs benchmark"""
    excess_returns = strategy_returns - benchmark_returns
    tracking_error = np.std(excess_returns)
    return np.mean(excess_returns) / tracking_error * np.sqrt(252) if tracking_error > 0 else 0

def tail_ratio(returns):
    """Ratio of 95th percentile to 5th percentile (abs value)"""
    p95 = np.percentile(returns, 95)
    p5 = np.percentile(returns, 5)
    return np.abs(p95 / p5) if p5 != 0 else 0

def statistical_comparison(returns1, returns2):
    """
    Compare two strategy return streams using statistical tests.
    Returns dict with test results and interpretation.
    """
    # T-test for difference in means
    t_stat, t_pvalue = stats.ttest_ind(returns1, returns2, equal_var=False)

    # Mann-Whitney U test (non-parametric alternative)
    try:
        u_stat, u_pvalue = stats.mannwhitneyu(returns1, returns2, alternative='two-sided')
    except ValueError:
        u_stat, u_pvalue = np.nan, np.nan

    # Effect size (Cohen's d)
    pooled_std = np.sqrt((np.var(returns1) + np.var(returns2)) / 2)
    cohens_d = (np.mean(returns1) - np.mean(returns2)) / pooled_std if pooled_std > 0 else 0

    return {
        't_statistic': t_stat,
        't_pvalue': t_pvalue,
        'significant_t': t_pvalue < 0.05,
        'u_statistic': u_stat,
        'u_pvalue': u_pvalue,
        'significant_u': u_pvalue < 0.05,
        'cohens_d': cohens_d,
        'mean_diff': np.mean(returns1) - np.mean(returns2)
    }

def value_at_risk(returns, confidence=0.95):
    """Calculate Value at Risk at given confidence level"""
    return np.percentile(returns, (1 - confidence) * 100)

def conditional_value_at_risk(returns, confidence=0.95):
    """Calculate CVaR (Expected Shortfall) - average loss beyond VaR"""
    var = value_at_risk(returns, confidence)
    return np.mean(returns[returns <= var])

def win_rate(returns):
    """Percentage of positive return periods"""
    return np.sum(returns > 0) / len(returns) if len(returns) > 0 else 0

def profit_factor(returns):
    """Ratio of gross profits to gross losses"""
    profits = np.sum(returns[returns > 0])
    losses = np.abs(np.sum(returns[returns < 0]))
    return profits / losses if losses > 0 else 0
