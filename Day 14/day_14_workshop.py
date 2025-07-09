#!/usr/bin/env python
# coding: utf-8

"""
📊 Day 14 Workshop – Monitoring and Continuous Retraining in ML

Objective:
This script simulates a real-world scenario in ML operations, covering:
- Making predictions
- Logging actual vs predicted values
- Monitoring MAE (Mean Absolute Error) over time
- Detecting model drift using rolling statistics
- Automatically triggering retraining when drift exceeds threshold
- Visualizing status with CI/CD-style feedback
"""

# ------------------------------------------
# 📦 Import Required Libraries
# ------------------------------------------
import numpy as np                      # For generating simulated numeric data
import pandas as pd                     # For working with tabular time-series data
import matplotlib.pyplot as plt         # For plotting trends and metrics
from sklearn.metrics import mean_absolute_error  # To compute prediction error

# ------------------------------------------
# 🔮 Simulate Predictions and Ground Truth
# ------------------------------------------
np.random.seed(42)  # Ensures reproducibility of results

# Create a sequence of 60 dates starting from Jan 1, 2024
days = pd.date_range(start='2024-01-01', periods=60)

# Simulate actual energy usage around a mean of 200 kWh ± 10
actual = np.random.normal(loc=200, scale=10, size=60)

# Simulate predicted values with ±5 random noise
predicted = actual + np.random.normal(loc=0, scale=5, size=60)

# Create DataFrame to hold the series
df = pd.DataFrame({'date': days, 'actual': actual, 'predicted': predicted})

# Calculate absolute error per day
df['abs_error'] = np.abs(df['actual'] - df['predicted'])

# ------------------------------------------
# 📈 Calculate 7-day Rolling MAE
# ------------------------------------------
# Rolling MAE helps smooth out noise and detect trend shifts
df['rolling_MAE'] = df['abs_error'].rolling(window=7).mean()

# ------------------------------------------
# ⚠️ Drift Detection Logic
# ------------------------------------------
# Define baseline MAE using first 14 days as calibration window
baseline_mae = df['abs_error'][:14].mean()

# Drift is flagged when rolling MAE exceeds 125% of baseline
df['drift'] = df['rolling_MAE'] > (baseline_mae * 1.25)

# Check if 3 or more consecutive drift days occurred
drift_triggered = df['drift'].rolling(window=3).sum() >= 3

# ------------------------------------------
# 🖨️ Print Monitoring Results
# ------------------------------------------
print("Baseline MAE:", baseline_mae)
print("Drift Trigger Threshold:", baseline_mae * 1.25)
print("Retraining Triggered:", drift_triggered.any())

# ------------------------------------------
# 📊 Plot Rolling MAE with Drift Threshold
# ------------------------------------------
plt.figure(figsize=(10, 5))
plt.plot(df['date'], df['rolling_MAE'], label='7-day Rolling MAE')
plt.axhline(baseline_mae * 1.25, color='red', linestyle='--', label='Drift Threshold')
plt.title('Drift Detection: Rolling MAE')
plt.xlabel('Date')
plt.ylabel('MAE')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save plot to file and display
plt.savefig('rolling_mae_plot.png')
plt.show()
