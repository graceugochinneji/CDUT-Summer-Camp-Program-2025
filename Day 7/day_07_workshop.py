#!/usr/bin/env python
# coding: utf-8

"""
🎓 Chapter 7: Streamlit Fundamentals

This script introduces how to build a basic interactive energy dashboard using Streamlit.
It walks through the installation, widget creation, layout, and simple data visualization.
"""

# ------------------------------------------
# 📦 1. Install Streamlit (run in terminal)
# ------------------------------------------
# Run this in a terminal, not within a script
# pip install streamlit

# ------------------------------------------
# 🚀 2. First Run (from terminal)
# ------------------------------------------
# Use this command to launch the app
# streamlit run app.py

# ------------------------------------------
# 🧩 3. Widgets Overview
# ------------------------------------------
import streamlit as st  # Import Streamlit module

# Set the main title of the dashboard
st.title("Energy Dashboard")

# Add an interactive slider widget for selecting a threshold value
st.slider("Threshold", 0, 100, 25)

# Add a text input widget for users to enter a building name
st.text_input("Building Name")

# Add a clickable button labeled "Predict"
st.button("Predict")

# ------------------------------------------
# 🎚️ 4. Sidebar Filters
# ------------------------------------------
# Use a sidebar section for filter controls
with st.sidebar:
    st.header("Filters")
    # Sidebar slider to select an energy limit value
    st.slider("Energy Limit", 0, 500, 200)

# ------------------------------------------
# 🖼️ 5. Layout and Expander
# ------------------------------------------
# Create two columns for layout
col1, col2 = st.columns(2)

# Display a key metric inside the first column
col1.metric("Predicted Usage", "500 kWh")

# Use an expander section for extra details
with st.expander("See Explanation"):
    st.write("Details about prediction")

# ------------------------------------------
# 🎨 6. Styling with Markdown and Plot
# ------------------------------------------
# Add styled markdown with HTML tags for formatting
st.markdown("<h3 style='color:blue'>Energy Trends</h3>", unsafe_allow_html=True)

# Show a simple line chart with mock energy data
st.line_chart([10, 20, 15, 30, 40])
