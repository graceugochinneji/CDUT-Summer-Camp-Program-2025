#!/usr/bin/env python
# coding: utf-8

"""
🔐 Chapter 10: Supabase Authentication & Authorization

This script walks through how to integrate Supabase into a Python or Streamlit application for user authentication,
registration, and secure user profile management.
"""

# ------------------------------------------
# ✅ Setup Supabase Client
# ------------------------------------------
from supabase import create_client, Client

# Replace these with your actual Supabase credentials
SUPABASE_URL = 'https://your-project.supabase.co'  # Supabase project URL
SUPABASE_KEY = 'your-anon-or-service-role-key'     # API key for your Supabase project

# Initialize a Supabase client for interacting with the backend
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# ------------------------------------------
# 👤 Register a New User
# ------------------------------------------
def register_user(email, password):
    """
    Registers a new user with Supabase using the provided email and password.
    Returns the response from Supabase.
    """
    response = supabase.auth.sign_up({'email': email, 'password': password})
    return response

# ------------------------------------------
# 🔑 Login Existing User
# ------------------------------------------
def login_user(email, password):
    """
    Authenticates an existing user using email and password.
    Returns the session token and user details if successful.
    """
    response = supabase.auth.sign_in_with_password({'email': email, 'password': password})
    return response.session, response.user

# ------------------------------------------
# ✅ TASK: Connect and Test
# ------------------------------------------
# 1. Go to https://app.supabase.com and create a project.
# 2. Create a table called `profiles` with fields: `id`, `email`, `role`.
# 3. Use `register_user(email, password)` to register users.
# 4. Use `login_user(email, password)` to log users in and fetch their session.
# 5. Print session token and user info for verification.
