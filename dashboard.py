import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

CSV_PATH = "data/all_tickers_results.csv"
df = pd.read_csv(CSV_PATH)

# Basic summary
df['Risk-Adjusted'] = df['Total Return'] / df['Volatility']

app = Dash(__name__)
fig_returns = px.bar(df.sort_values("Total Return", ascending=False),
                     x="Ticker", y="Total Return",
                     title="Total Return per Ticker")

fig_volatility = px.bar(df.sort_values("Volatility", ascending=False),
                        x="Ticker", y="Volatility",
                        title="Volatility per Ticker")

fig_risk_adj = px.bar(df.sort_values("Risk-Adjusted", ascending=False),
                      x="Ticker", y="Risk-Adjusted",
                      title="Risk-Adjusted Return per Ticker")

app.layout = html.Div([
    html.H1("QuantLab Backtest Dashboard"),
    dcc.Graph(figure=fig_returns),
    dcc.Graph(figure=fig_volatility),
    dcc.Graph(figure=fig_risk_adj)
])

if __name__ == "__main__":
    app.run(debug=True)

