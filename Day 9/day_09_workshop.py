#!/usr/bin/env python
# coding: utf-8

"""
📊 Smart-Energy Analysis with Streamlit

This script demonstrates how to use Streamlit to build a what-if analysis dashboard for smart energy systems.
It includes sliders, text inputs, session state handling, and visual analytics for comparing scenarios.
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------
# 🔧 1. User Inputs – Define Sliders and Text Boxes
# ------------------------------------------------
st.title("🔌 Smart-Energy What-If Analysis")

# Simulated user inputs
voltage = st.slider("Voltage Input (V)", min_value=100, max_value=250, value=220)
current = st.slider("Current (A)", min_value=1, max_value=100, value=10)
efficiency = st.slider("Efficiency (%)", min_value=50, max_value=100, value=90)
building = st.text_input("Building Name", value="Smart Plaza")

# ------------------------------------------------
# 📊 2. Calculate Savings Based on Input Scenario
# ------------------------------------------------
# Formula: Power = Voltage * Current
power = voltage * current  # in watts

# Simulated base power (e.g., older configuration)
base_power = 250 * 10  # 250V * 10A

# Compute savings in watts and %
savings = base_power - power
savings_percent = (savings / base_power) * 100

# ------------------------------------------------
# 💡 3. Display KPI Metrics
# ------------------------------------------------
st.metric("Power Usage (W)", f"{power}")
st.metric("Energy Savings (W)", f"{savings}")
st.metric("Savings (%)", f"{savings_percent:.2f}%")

# ------------------------------------------------
# 🔁 4. Persist Inputs Across Reruns
# ------------------------------------------------
# Store in session_state for reference or comparison
st.session_state['last_voltage'] = voltage
st.session_state['last_power'] = power

# ------------------------------------------------
# 🆚 5. A/B Scenario Comparison (Optional)
# ------------------------------------------------
with st.expander("📊 Compare A/B Scenarios"):
    col1, col2 = st.columns(2)
    with col1:
        voltage_a = st.slider("Scenario A Voltage", 100, 250, 220, key="va")
        current_a = st.slider("Scenario A Current", 1, 100, 10, key="ca")
    with col2:
        voltage_b = st.slider("Scenario B Voltage", 100, 250, 200, key="vb")
        current_b = st.slider("Scenario B Current", 1, 100, 10, key="cb")

    power_a = voltage_a * current_a
    power_b = voltage_b * current_b
    ab_savings = power_a - power_b

    st.write(f"Scenario A Power: {power_a} W")
    st.write(f"Scenario B Power: {power_b} W")
    st.write(f"Difference: {ab_savings} W")

# ------------------------------------------------
# 📈 6. Visual Analytics – Sensitivity Curve
# ------------------------------------------------
st.subheader("📉 Voltage vs. Power Curve")

voltages = np.linspace(100, 250, 50)
powers = voltages * current  # using selected current

fig, ax = plt.subplots()
ax.plot(voltages, powers, label="Power = V × I")
ax.axvline(voltage, color='red', linestyle='--', label="Selected Voltage")
ax.set_xlabel("Voltage (V)")
ax.set_ylabel("Power (W)")
ax.set_title("Sensitivity Curve: Voltage vs Power")
ax.legend()
st.pyplot(fig)

# ------------------------------------------------
# ✅ 7. Footer Message
# ------------------------------------------------
st.markdown("<h4 style='color:green'>Interactive What-If Dashboard Complete</h4>", unsafe_allow_html=True)
