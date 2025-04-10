

### 🔧 Connexion à la base

```python
import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password',
    database='testdb'
)
cursor = conn.cursor()
```

---

### 📦 Création d'une table

```python
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    price DECIMAL(10, 2)
)
""")
conn.commit()
```

---

### ✍️ Insertion de données

```python
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
```

---

### 📖 Lecture de toutes les données

```python
cursor.execute("SELECT * FROM products")
for row in cursor.fetchall():
    print(row)
```

---

### 🔍 Recherche avec condition

```python
cursor.execute("SELECT * FROM products WHERE price > %s", (50,))
results = cursor.fetchall()
for row in results:
    print(row)
```

---

### ✏️ Mise à jour de données

```python
cursor.execute("UPDATE products SET price = %s WHERE name = %s", (899.99, "Ordinateur"))
conn.commit()
```

---

### ❌ Suppression de données

```python
cursor.execute("DELETE FROM products WHERE name = %s", ("Souris",))
conn.commit()
```

---

### 🧹 Fermeture propre

```python
cursor.close()
conn.close()
```