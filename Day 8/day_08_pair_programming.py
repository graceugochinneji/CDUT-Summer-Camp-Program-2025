#!/usr/bin/env python
# coding: utf-8

# # 🤝 Chapter 8: Pair Programming – Prediction UI

# **⏱️ Estimated Duration:** 3–4 hours  
# **🎯 Task:** Build an interactive prediction form with input validation and real-time output using `st.metric`. Fill all blanks and complete the stretch goals.

# ## ✅ Task 1: Set Up and Imports

# In[ ]:


import streamlit as st
import numpy as ___
import joblib


# ## ✅ Task 2: UI Title & Input Form

# In[ ]:


st.title("___")
with st.form("___"):
    hour = st.slider("Hour", 0, 23, 12)
    temp = st.number_input("Temp (°C)", -10.0, 50.0, ___)
    submitted = ___


# ## ✅ Task 3: Load Model and Validate

# In[ ]:


if submitted:
    if temp < -5 or temp > 45:
        st.warning("⚠️ Temperature out of range")
    model = joblib.load("___")
    X = np.array([[hour, temp]])
    y_pred = model.predict(X)[0]


# ## ✅ Task 4: Display Output

# In[ ]:


st.metric("Predicted Load (kW)", f"{y_pred:.2f}")


# ## 💪 Stretch Challenge 1: Modularize Prediction Code

# In[ ]:


def predict_energy(hour, temp):
    model = joblib.load("models/xgb_energy_model.pkl")
    return model.predict(np.array([[hour, temp]]))[0]


# ## 💪 Stretch Challenge 2: Add Time Logging

# In[ ]:


import datetime
with open("logs/predictions_log.csv", "a") as f:
    f.write(f"{datetime.datetime.now()},{hour},{temp},{y_pred:.2f}\n")


# ## 💬 Final Reflection

# > How might this UI design improve user trust and usability in a real-world scenario?
