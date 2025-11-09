import pandas as pd

def rsi_strategy(data: pd.DataFrame, period=14, oversold=30, overbought=70):
    """
    RSI strategy: buy when RSI < oversold, sell when RSI > overbought.
    """
    data = data.copy()
    delta = data['Close'].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(period, min_periods=1).mean()
    avg_loss = loss.rolling(period, min_periods=1).mean()
    rs = avg_gain / avg_loss
    data['RSI'] = 100 - (100 / (1 + rs))

    data['RSI_Signal'] = 0
    data.loc[data['RSI'] < oversold, 'RSI_Signal'] = 1
    data.loc[data['RSI'] > overbought, 'RSI_Signal'] = -1

    return data
