cursor.execute("UPDATE products SET price = %s WHERE name = %s", (899.99, "Ordinateur"))
conn.commit()


cursor.execute("DELETE FROM products WHERE name = %s", ("Souris",))
conn.commit()


cursor.close()
conn.close()
