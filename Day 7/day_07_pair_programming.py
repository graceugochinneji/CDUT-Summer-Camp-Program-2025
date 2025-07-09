#!/usr/bin/env python
# coding: utf-8

# # 🤝 Chapter 7: Pair Programming – Streamlit Fundamentals

# **⏱️ Estimated Duration:** 3–4 hours  
# **🎯 Task:** Create a mini energy dashboard with interactive widgets and layout using Streamlit. Fill all blanks (`___`) and complete stretch goals.

# ## ✅ Task 1: Install and Run Streamlit

# In[ ]:


get_ipython().system('pip install ___')
# Run from terminal: streamlit run ___


# ## ✅ Task 2: Create Main UI Elements

# In[ ]:


import streamlit as st
st.title("___")
threshold = st.slider("Set Threshold", 0, 100, ___)
name = st.text_input("Enter ___")


# ## ✅ Task 3: Add Button Logic

# In[ ]:


if st.button("Predict"):
    st.write(f"Prediction triggered for {name}")


# ## ✅ Task 4: Create Sidebar Filter

# In[ ]:


with st.sidebar:
    st.header("___")
    limit = st.slider("Energy Limit", 0, 500, ___)


# ## ✅ Task 5: Layout with Columns & Expander

# In[ ]:


col1, col2 = ___
col1.metric("Predicted", "___ kWh")
with st.expander("___"):
    st.write("Provide additional info")


# ## ✅ Task 6: Add Plot and Custom HTML

# In[ ]:


st.markdown("<h3 style='color:green'>___</h3>", unsafe_allow_html=True)
st.line_chart([___])


# ## 💪 Stretch Challenge: Add Image or Video and Use st.session_state

# In[ ]:


# Upload a building image and display with st.image
# Use st.session_state to preserve slider values between runs


# ## 💬 Final Discussion

# > What real-world features could you add to make this app useful in energy policy or household monitoring?
