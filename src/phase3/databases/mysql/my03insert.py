# Une insertion
cursor.execute("INSERT INTO products (name, price) VALUES (%s, %s)", ("Ordinateur", 999.99))

# Insertion multiple
data = [
    ("Clavier", 49.99),
    ("Souris", 19.90),
    ("Écran", 199.99)
]
cursor.executemany("INSERT INTO products (name, price) VALUES (%s, %s)", data)

conn.commit()
