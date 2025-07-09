#!/usr/bin/env python
# coding: utf-8

"""
🎓 Chapter 8: Building the Prediction Page UI

This script demonstrates how to create a Streamlit-based prediction interface for energy load forecasting.
It covers layout design, input validation, model loading, metric display, and logging.
"""

# ------------------------------------------
# 📦 1. Setup – Import Libraries
# ------------------------------------------
import streamlit as st       # For creating the web UI
import pandas as pd          # Optional: useful for data handling
import numpy as np           # For numerical operations
import joblib                # For loading the trained model

# ------------------------------------------
# 🧱 2. UI Layout – Title and Input Form
# ------------------------------------------
# Set the main title of the dashboard
st.title("Energy Forecast Dashboard")

# Create a form for user input to trigger prediction on submission
with st.form("prediction_form"):
    # Slider input for selecting hour of day (0–23)
    hour = st.slider("Hour of Day", 0, 23, 12)

    # Numeric input box for temperature (°C)
    temperature = st.number_input("Temperature (°C)", min_value=-10.0, max_value=50.0, value=25.0)

    # Button to submit the form
    submitted = st.form_submit_button("Predict")

# ------------------------------------------
# ✅ 3. Load Model and Validate Inputs
# ------------------------------------------
if submitted:
    # Input validation for temperature
    if temperature < -5 or temperature > 45:
        st.warning("⚠️ Unusual temperature entered!")

    # Load the pre-trained XGBoost model using joblib
    model = joblib.load("models/xgb_energy_model.pkl")

    # Prepare input features as a 2D NumPy array for prediction
    features = np.array([[hour, temperature]])

    # Predict the load using the model
    prediction = model.predict(features)[0]

    # ------------------------------------------
    # 📊 4. Display Prediction Using st.metric
    # ------------------------------------------
    # Show the predicted load using a metric widget
    st.metric("Predicted Load (kW)", f"{prediction:.2f}")

    # ------------------------------------------
    # 📝 5. Optional Logging of Prediction
    # ------------------------------------------
    # Append the prediction details to a CSV log file
    with open("logs/predictions_log.csv", "a") as f:
        f.write(f"{hour},{temperature},{prediction:.2f}\n")

# ------------------------------------------
# 🎨 6. Final Layout Suggestions
# ------------------------------------------
# Styled message for the footer using Markdown and inline HTML
st.markdown("<h4 style='color:green'>Thank you for using the dashboard!</h4>", unsafe_allow_html=True)
