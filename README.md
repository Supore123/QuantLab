# QuantLab: Algorithmic Backtesting Platform

**Author:** Jonathan Yohannes  
**GitHub:** [https://github.com/Supore123/QuantLab](https://github.com/Supore123/QuantLab)

---

## Overview

QuantLab is a Python-based framework for backtesting algorithmic trading strategies on historical financial data.  
The project demonstrates:

- Time-series data handling and exploration
- Implementation of algorithmic trading strategies
- Portfolio management and performance metrics
- Visualization of trading results
- Optional ML-based predictions for strategy enhancement

This project is designed to showcase quantitative and programming skills relevant to roles in quantitative research, algorithmic trading, and data analysis.

---

## Features

- Modular backtesting engine with portfolio tracking
- Support for multiple strategies:
  - Moving Average Crossover
  - RSI Strategy (optional)
- Performance metrics: cumulative P&L, Sharpe ratio, maximum drawdown
- Visualizations of trades vs. asset price
- Optional ML integration for predicting short-term price movements

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Supore123/QuantLab.git
cd QuantLab
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

### Run Backtest

```python
from backtester.engine import BacktestEngine
from strategies.moving_average import MovingAverageStrategy
from utils.data_loader import load_data

# Load historical data
data = load_data("data/sample_data.csv")

# Initialize strategy and engine
strategy = MovingAverageStrategy(data)
engine = BacktestEngine(strategy)
engine.run_backtest()

# Print performance
engine.print_metrics()
engine.plot_results()
```

### Jupyter Notebook

Open `notebooks/exploration.ipynb` to explore EDA, strategy simulations, and visualization of results.

---

## Project Structure

```
QuantLab/
├── backtester/        # Core backtesting engine and metrics
├── strategies/        # Strategy implementations
├── notebooks/         # Experimentation and visualizations
├── utils/             # Data loading and helper functions
├── data/              # Sample or downloaded datasets
├── README.md
└── requirements.txt
```

---

## Future Work

- Add additional strategies (momentum, mean-reversion, MACD)
- Integrate ML models for price prediction
- Implement live data ingestion and streaming backtests
- Improve performance and scalability
