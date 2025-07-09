"""
📘 Chapter 11 – Pair Programming Task
Topic: Supabase Authentication Integration

Instructions:
Complete the following tasks step-by-step. This will take approximately 3–4 hours.

1. 🧠 Implement `register_user()` and `login_user()` functions using `supabase.auth`:
   - [ ] Use `email`, `password` as input.
   - [ ] Register user and add them to the `profiles` table with role="user".
   - [ ] Catch exceptions and return appropriate status and messages.

2. 🔐 Design a terminal-based interface that:
   - [ ] Asks user to choose: [1] Login [2] Register
   - [ ] Collects user input (email, password)
   - [ ] Calls the appropriate function

3. 📊 After login, fetch the user role using `get_user_role(user_id)`:
   - [ ] Display role and confirm session setup

4. 🔄 Implement `logout_user()` function:
   - [ ] Call `supabase.auth.sign_out()`

5. 🧪 Test all the above with different emails and passwords.

NOTE: Fill in the code below where indicated.
"""

# Task 1 – Authentication Functions
from supabase import create_client, Client

SUPABASE_URL = "https://kyanyydvgfdjsirsjmvr.supabase.co"
SUPABASE_KEY = "<YOUR_SUPABASE_KEY>"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def register_user(email: str, password: str, role: str = "user"):
    # TODO: Register user and insert into profiles
    pass

def login_user(email: str, password: str):
    # TODO: Login user and return session
    pass

def get_user_role(user_id: str):
    # TODO: Query Supabase profiles table and return role
    pass

def logout_user():
    # TODO: Sign out user from Supabase
    pass

# Task 2 – Interface and Testing
def main():
    print("🔐 Welcome to Supabase Auth Terminal")
    choice = input("Choose an option: [1] Login [2] Register: ")

    email = input("Enter your email: ")
    password = input("Enter your password: ")

    if choice == "2":
        success, msg = register_user(email, password)
        print("✅" if success else "❌", msg)
    elif choice == "1":
        session, user = login_user(email, password)
        if session:
            print(f"✅ Login successful. User ID: {user.id}")
            role = get_user_role(user.id)
            print(f"🎓 Role: {role}")
        else:
            print("❌ Login failed.")
    else:
        print("Invalid option")

    logout_user()
    print("🚪 Logged out.")

if __name__ == "__main__":
    main()
