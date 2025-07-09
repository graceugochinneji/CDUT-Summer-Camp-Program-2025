
# day_14_pair_programming.py

"""
Pair Programming Challenge: Monitor & Retrain Your ML Model

Complete the blanks and TODO sections below.

Objective:
- Simulate predictions and ground truth
- Calculate MAE and rolling averages
- Detect drift and trigger retraining logic
- BONUS: Visualize with matplotlib
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error

# Step 1: Simulate a 60-day dataset
# TODO: Use np.random to simulate actual and predicted values
days = pd.date_range(start='2024-01-01', periods=60)
actual = ________
predicted = ________

# Step 2: Calculate absolute error
df = pd.DataFrame({
    'date': days,
    'actual': actual,
    'predicted': predicted
})
df['abs_error'] = ________

# Step 3: Calculate rolling MAE
# TODO: Use a 7-day window
df['rolling_MAE'] = ________

# Step 4: Define drift threshold using baseline (first 2 weeks)
baseline_mae = ________
threshold = ________
print("Baseline MAE:", baseline_mae)
print("Drift Threshold:", threshold)

# Step 5: Mark where drift occurs
df['drift'] = ________

# Step 6: Apply drift trigger rule (3+ days breach in a row)
# Stretch Task: Create drift_triggered boolean series
drift_triggered = ________
print("Retraining Triggered:", drift_triggered.any())

# Step 7: Visualize (optional)
# TODO: Plot MAE and drift threshold
plt.figure(figsize=(10, 5))
plt.plot(df['date'], df['rolling_MAE'], label='7-day Rolling MAE')
plt.axhline(______, color='red', linestyle='--', label='Drift Threshold')
plt.title('Drift Detection')
plt.xlabel('Date')
plt.ylabel('MAE')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('rolling_mae_pair_programming_plot.png')
plt.show()
