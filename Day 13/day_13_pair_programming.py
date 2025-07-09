"""
Chapter 13 Pair Programming: Deploying to Streamlit Cloud

Team Objectives:
- [ ] Prepare deployment folder structure
- [ ] Create a GitHub repository and push your code
- [ ] Add a secrets.toml file locally (DO NOT upload it)
- [ ] Deploy the app via Streamlit Cloud and verify access

Task 1: Prepare Directory Structure
"""

# TODO 1: Ensure the following files exist in your local directory
# - main_app.py
# - auth_supabase.py
# - secrets.toml

# Write a function to check file structure (simulate)
import os

def check_files():
    files = ["main_app.py", "auth_supabase.py", "secrets.toml"]
    for f in files:
        print(f"{f}: {'FOUND ✅' if os.path.exists(f) else 'MISSING ❌'}")

# Call the function
# TODO: Uncomment after placing your files
# check_files()


"""
Task 2: Create secrets.toml

This file should contain your Supabase credentials securely.
Format:
[general]
SUPABASE_URL = "https://your-url.supabase.co"
SUPABASE_KEY = "your-key"
"""

# TODO 2: Create this file locally and DO NOT upload to GitHub

"""
Task 3: GitHub Deployment

1. Initialize a Git repository:
   git init

2. Add files and commit:
   git add .
   git commit -m "initial commit"

3. Create a GitHub repo and push:
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   git push -u origin main
"""

# TODO: Add GitHub link to your README

"""
Task 4: Streamlit Cloud Deployment

1. Login to https://streamlit.io/cloud
2. Click 'New App' > select your repo
3. Add required files and secrets via the web UI
4. Click 'Deploy'
5. Test and submit your public link
"""

# ✅ STRETCH TASK:
# Once deployed, update your app with a new feature and redeploy.
# Document your deployment journey in a short report.
