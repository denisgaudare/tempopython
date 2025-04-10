cursor.execute("SELECT * FROM products WHERE price > %s", (50,))
results = cursor.fetchall()
for row in results:
    print(row)
