import pandas as pd

def bollinger_bands_strategy(data: pd.DataFrame, window=20, num_std=2):
    """
    Bollinger Bands strategy: buy when price < lower band, sell when price > upper band.
    """
    data = data.copy()
    data['SMA'] = data['Close'].rolling(window).mean()
    data['STD'] = data['Close'].rolling(window).std()
    data['Upper_Band'] = data['SMA'] + num_std * data['STD']
    data['Lower_Band'] = data['SMA'] - num_std * data['STD']

    # Signal: 1 = buy, -1 = sell
    data['BB_Signal'] = 0
    data.loc[data['Close'] < data['Lower_Band'], 'BB_Signal'] = 1
    data.loc[data['Close'] > data['Upper_Band'], 'BB_Signal'] = -1

    return data
