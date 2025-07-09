#!/usr/bin/env python
# coding: utf-8

"""
📤 Day 12 Workshop – Data Upload and Persistence with Supabase and Streamlit

Authors:
- Dr. Grace Ugochi Nneji
- Dr. Happy Nkanta Monday

Objective:
Build a Streamlit app that allows users to upload CSV files, store them in Supabase Storage,
log upload events in a Supabase table, and view file upload history.
"""

# ------------------------------------------
# 📦 Import Required Libraries
# ------------------------------------------
import streamlit as st                    # For building the Streamlit web app
from supabase import create_client       # To connect to Supabase backend
import os                                 # For interacting with the environment (not used here but often useful)
from datetime import datetime            # To timestamp file uploads
import pandas as pd                      # To work with tabular data in memory

# ------------------------------------------
# 🔐 Supabase Credentials
# ------------------------------------------
SUPABASE_URL = "https://kyanyydvgfdjsirsjmvr.supabase.co"  # Your Supabase project URL
SUPABASE_KEY = "your_supabase_key_here"                    # Your API key (replace with actual key)
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)       # Initialize the Supabase client

# ------------------------------------------
# 📦 Define Upload Bucket
# ------------------------------------------
UPLOAD_BUCKET = "uploads"  # Name of the bucket in Supabase Storage

# ------------------------------------------
# 🎯 Streamlit UI – Title
# ------------------------------------------
st.title("📤 Data Upload & Persistence Workshop")

# ------------------------------------------
# 📁 File Uploader Widget
# ------------------------------------------
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

# If a file is uploaded, handle storage and logging
if uploaded_file:
    # Read raw file bytes
    file_bytes = uploaded_file.getvalue()
    file_name = uploaded_file.name

    # Upload the file to Supabase Storage
    supabase.storage.from_(UPLOAD_BUCKET).upload(file_name, file_bytes)

    # Log the upload in a Supabase table
    result = supabase.table("prediction_logs").insert({
        "filename": file_name,
        "timestamp": datetime.utcnow().isoformat(),  # Log current time
        "email": "test_user@example.com",            # Placeholder email; ideally fetched from session
        "prediction": "Uploaded file"                # Optional note or tag
    }).execute()

    # Success message
    st.success("✅ File uploaded and logged successfully!")

# ------------------------------------------
# 📂 View Upload History
# ------------------------------------------
st.subheader("📂 Uploaded File History")

# Query all past uploads from the 'prediction_logs' table
history = supabase.table("prediction_logs").select("*").order("timestamp", desc=True).execute()

# Convert query result to a DataFrame
df = pd.DataFrame(history.data)

# Show logs if available
if not df.empty:
    st.dataframe(df)
else:
    st.info("No file logs yet.")
