
# day_12_pair_programming.py
# Pair Programming Task: Implement Persistent File Upload and Logging

import streamlit as st
from supabase import create_client
from datetime import datetime
import pandas as pd

# TODO: Initialize Supabase client
SUPABASE_URL = "__________"
SUPABASE_KEY = "__________"
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

UPLOAD_BUCKET = "uploads"

st.title("📥 Student Task: Upload with History Log")

# TODO: Add file uploader component
uploaded_file = st.______("Upload your CSV", type="___")

if uploaded_file:
    file_bytes = uploaded_file.getvalue()
    file_name = uploaded_file.____

    # TODO: Upload to Supabase Storage
    supabase.storage.from_("_____").upload(file_name, file_bytes)

    # TODO: Log metadata in SQL table
    supabase.table("__________").insert({
        "filename": file_name,
        "timestamp": datetime.utcnow().isoformat(),
        "email": "__________",
        "prediction": "__________"
    }).execute()

    st.success("✅ File uploaded and logged!")

# TODO: Add section to display user's upload history
