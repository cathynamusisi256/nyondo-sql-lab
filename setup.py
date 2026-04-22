import sqlite3

conn = sqlite3.connect('nyondo_stock.db')

# Create tables
conn.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    price REAL NOT NULL
)''')

conn.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    role TEXT DEFAULT 'attendant'
)''')

# [span_9](start_span)Insert Products[span_9](end_span)
products = [
    ('Cement (bag)', 'Portland cement 50kg bag', 35000),
    ('Iron Sheet 3m', 'Gauge 30 roofing sheet 3m long', 110000),
    ('Paint 5L', 'Exterior wall paint white 5L', 60000),
    ('Nails 1kg', 'Common wire nails 1kg pack', 12000),
    ('Timber 2x4', 'Pine timber plank 2x4 per metre', 25000)
]
conn.executemany('INSERT INTO products (name, description, price) VALUES (?, ?, ?)', products)

# [span_10](start_span)Insert Users[span_10](end_span)
users = [
    ('admin', 'admin123', 'admin'),
    ('fatuma', 'pass456', 'attendant'),
    ('wasswa', 'pass789', 'manager')
]
conn.executemany('INSERT OR IGNORE INTO users (username, password, role) VALUES (?, ?, ?)', users)

conn.commit()

# [span_11](start_span)Verify[span_11](end_span)
rows = conn.execute('SELECT * FROM products').fetchall()
for r in rows: print(r)
conn.close()

