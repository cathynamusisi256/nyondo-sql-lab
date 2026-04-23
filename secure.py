import sqlite3

def login_safe(username, password):
    # 1. VALIDATION RULES
    # Rule: No spaces in username
    if " " in username:
        return "Rejected: Username cannot contain spaces"
    
    # Rule: Password must be at least 6 characters
    if len(password) < 6:
        return "Rejected: Password too short"

    # 2. DATABASE LOGIC (Only runs if validation passes)
    conn = sqlite3.connect('nyondo_stock.db')
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    user = conn.execute(query, (username, password)).fetchone()
    conn.close()
    
    if user:
        return f"Success: Welcome {username}"
    else:
        return "Failed: Invalid credentials"

# --- TASK 5 TEST CASES ---
print("--- Testing Task 5 Validation ---")

# Test 1: Valid Login
print(f"Test 1 (Valid): {login_safe('admin', 'admin123')}")

# Test 2: Password too short
print(f"Test 2 (Short Pass): {login_safe('admin', 'ab')}")

# Test 3: Space in username
print(f"Test 3 (Spaces): {login_safe('ad min', 'pass123')}")