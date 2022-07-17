import sqlite3


conn = sqlite3.connect("db.db")
cur = conn.cursor()


cur.execute("""
CREATE TABLE IF NOT EXISTS categories(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER,
    is_published BOOLEAN DEFAULT (false),
    name TEXT NOT NULL,
FOREIGN KEY (parent_id) REFERENCES categories(id)
);
""")
conn.commit()
cur.execute("""
CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_id INTEGER,
    price REAL DEFAUL (0),
    total INTEGER DEFAULT (0),
    name TEXT NOT NULL,
    FOREIGN KEY (category_id) REFERENCES (categories_id)
);
""")
conn.commit()

