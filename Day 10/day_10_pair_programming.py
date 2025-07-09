# --- Markdown Cell ---
# # 🤝 Chapter 10: Supabase Authentication
# **Pair Programming Task (3–4 hrs)**
# 
# In pairs, you’ll integrate a full authentication layer using Supabase in your Streamlit project.
# Leave no code blank! Fill in the missing pieces and test your app.
# --- Code Cell ---
# 🔐 Setup Supabase Client
from supabase import create_client, Client
SUPABASE_URL = '___'
SUPABASE_KEY = '___'
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
# --- Code Cell ---
# 👥 Function to Register Users
def register_user(email, password):
    try:
        response = supabase.auth.sign_up({___})  # Fill in
        user = response.user
        if user:
            supabase.table("profiles").insert({___}).execute()  # Fill in
        return True, "User registered"
    except Exception as e:
        return False, str(e)
# --- Code Cell ---
# 🔐 Function to Log in Users
def login_user(email, password):
    try:
        result = supabase.auth.sign_in_with_password({___})
        return result.session, result.user
    except Exception:
        return None, None
# --- Markdown Cell ---
# ### 🚀 STRETCH TASKS
# - Add a logout function.
# - Protect access to pages based on roles.
# - Add RLS to Supabase for table security.
# - Log prediction results into a user-specific table.
# - Visualize authenticated user dashboard.
