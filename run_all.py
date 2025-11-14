#!/usr/bin/env python3
import subprocess
import os

# Ensure working directory is project root
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Step 1: Run backtests (no plot display, just save)
print("⏳ Running backtests and saving plots...")
subprocess.run(["python", "-m", "scripts.run_backtest_multi", "--no-plot"], check=True)

# Step 2: Launch dashboard
print("⏳ Launching dashboard...")
subprocess.run(["python", "dashboard.py"], check=True)

