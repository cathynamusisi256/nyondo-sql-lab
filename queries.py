import sqlite3

# Connect to the database you created in Task 1
conn = sqlite3.connect('nyondo_stock.db')
cursor = conn.cursor()

print("--- Query A: Select all columns from products ---")
cursor.execute("SELECT * FROM products")
for row in cursor.fetchall(): print(row)

print("\n--- Query B: Select only names and prices ---")
cursor.execute("SELECT name, price FROM products")
for row in cursor.fetchall(): print(row)

print("\n--- Query C: Select product with ID 3 ---")
cursor.execute("SELECT * FROM products WHERE id = 3")
print(cursor.fetchone())

print("\n--- Query D: Search for products containing 'sheet' ---")
cursor.execute("SELECT * FROM products WHERE name LIKE '%sheet%'")
for row in cursor.fetchall(): print(row)

print("\n--- Query E: All products sorted by price (Expensive first) ---")
cursor.execute("SELECT * FROM products ORDER BY price DESC")
for row in cursor.fetchall(): print(row)

print("\n--- Query F: Top 2 most expensive products ---")
cursor.execute("SELECT * FROM products ORDER BY price DESC LIMIT 2")
for row in cursor.fetchall(): print(row)

print("\n--- Query G: Update Cement price to 38000 ---")
cursor.execute("UPDATE products SET price = 38000 WHERE id = 1")
conn.commit() # Save the change
# Verify the update
cursor.execute("SELECT * FROM products WHERE id = 1")
print("Updated record:", cursor.fetchone())

conn.close()