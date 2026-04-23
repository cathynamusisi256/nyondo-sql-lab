import sqlite3

def search_product_secure(name):
    conn = sqlite3.connect('nyondo_stock.db')
    # FIX: Use '?' placeholder instead of f-strings
    query = "SELECT * FROM products WHERE name LIKE ?"
    params = (f'%{name}%',)
    
    print(f"Executing secure query for: {name}")
    rows = conn.execute(query, params).fetchall()
    conn.close()
    return rows

def login_secure(username, password):
    conn = sqlite3.connect('nyondo_stock.db')
    # FIX: Use '?' placeholders for both username and password
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    params = (username, password)
    
    print(f"Executing secure login for: {username}")
    user = conn.execute(query, params).fetchone()
    conn.close()
    return user

# --- TESTING THE SAME ATTACKS FROM TASK 3 ---

print("\n--- Testing Login Bypass Attack ---")
hacker_user = login_secure("admin'--", "wrong_password")
if hacker_user:
    print(f"Result: Success! Logged in as: {hacker_user}")
else:
    print("Result: Failed! The system is now secure.")

print("\n--- Testing UNION Attack ---")
stolen_data = search_product_secure("' UNION SELECT id, username, password, role FROM users--")
if len(stolen_data) > 0:
    print(f"Found {len(stolen_data)} items.")
else:
    print("Result: No products found. The attack was blocked.")