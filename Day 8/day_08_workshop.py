#!/usr/bin/env python
# coding: utf-8

"""
🎓 Chapter 8: Building the Prediction Page UI

This script demonstrates how to create a Streamlit-based prediction interface for energy load forecasting.
It covers layout design, user input, input validation, model loading, making predictions, displaying results,
and logging user interactions and outputs.
"""

# ------------------------------------------
# 📦 1. Setup – Import Required Libraries
# ------------------------------------------

import streamlit as st        # Streamlit for building the interactive web UI
import numpy as np            # NumPy for numerical operations like sin/cos
import xgboost as xgb         # XGBoost for loading and using the trained prediction model
from datetime import datetime # To timestamp predictions in the log file
import os                     # For checking/creating directories and file operations

# ------------------------------------------
# 🧱 2. UI Layout – Title and User Input Form
# ------------------------------------------

# Set the title of the Streamlit app (displayed at the top of the web interface)
st.title("⚡ Energy Forecast Dashboard")

# Create a form for taking multiple input fields and submitting them together
with st.form("prediction_form"):
    # Section heading inside the form
    st.subheader("📥 Enter Required Inputs:")

    # Collect user input for each feature used by the model, with labels and default values
    voltage = st.number_input("Voltage (Volt)", 100.0, 250.0, 219.58)
    global_reactive_power = st.number_input("Global Reactive Power (kW)", 0.0, 2.0, 0.42)
    global_intensity = st.number_input("Global Intensity (amp)", 0.0, 50.0, 18.40)
    sub1 = st.number_input("Sub-metering 1", 0.0, 30.0, 0.00)
    sub2 = st.number_input("Sub-metering 2", 0.0, 30.0, 1.00)
    sub3 = st.number_input("Sub-metering 3", 0.0, 30.0, 17.00)
    hour = st.slider("Hour of Day", 0, 23, 17)  # Hour in 24-hour format
    day_of_week = st.selectbox("Day of Week", options=[0,1,2,3,4,5,6],
                               format_func=lambda x: ['Mon','Tue','Wed','Thu','Fri','Sat','Sun'][x])

    # Submit button to trigger prediction logic
    submitted = st.form_submit_button("🔍 Predict")

# ------------------------------------------
# ✅ 3. Prediction Logic – Run when form is submitted
# ------------------------------------------

if submitted:
    # Calculate time-based cyclical features using sine and cosine
    hour_sin = np.sin((hour / 24) * 2 * np.pi)  # Encodes hour into cyclical pattern (0–1)
    hour_cos = np.cos((hour / 24) * 2 * np.pi)  # Encodes hour into cyclical pattern (0–1)

    # Calculate apparent power (Volt × Amp = Watts ÷ 1000 = kW)
    apparent_power = voltage * global_intensity / 1000

    # Prepare feature vector in the exact order used during model training
    features = np.array([[global_reactive_power, voltage, global_intensity,
                          sub1, sub2, sub3,
                          hour, day_of_week, hour_sin, hour_cos, apparent_power]])

    # Define the corresponding feature names (must match those used when the model was trained)
    feature_names = ['Global_reactive_power', 'Voltage', 'Global_intensity',
                     'Sub_metering_1', 'Sub_metering_2', 'Sub_metering_3',
                     'hour', 'day_of_week', 'hour_sin', 'hour_cos', 'Apparent_power']

    # Convert the input features into a DMatrix (XGBoost’s preferred data format for prediction)
    dinput = xgb.DMatrix(features, feature_names=feature_names)

    # Load the previously trained XGBoost model from disk
    model = xgb.Booster()
    model.load_model("xgb_energy_model.json")  # Path to the saved model file

    # Use the model to make a prediction based on user inputs
    prediction = model.predict(dinput)[0]  # Get the first (and only) prediction

    # Display the result in a nice Streamlit metric widget
    st.metric("Predicted Load (kW)", f"{prediction:.2f}")

    # ------------------------------------------
    # 📝 Log prediction results to a CSV file
    # ------------------------------------------

    # Create the logs directory if it doesn't exist
    os.makedirs("logs", exist_ok=True)

    # Open or create the log file and append the prediction info
    with open("logs/predictions_log.csv", "a") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Current time
        f.write(f"{timestamp},{voltage},{global_reactive_power},{global_intensity},{sub1},{sub2},{sub3},{hour},{day_of_week},{prediction:.2f}\n")

# ------------------------------------------
# 🎨 4. Footer – Thank you message
# ------------------------------------------

# Display a thank-you footer using HTML styling within markdown
st.markdown("<h4 style='color:green'>✅ Prediction complete. Thank you for using the dashboard!</h4>", unsafe_allow_html=True)
