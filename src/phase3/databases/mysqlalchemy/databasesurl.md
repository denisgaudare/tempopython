---

### 🟦 **SQLite**
```python
sqlite:///chemin/vers/fichier.db          # Fichier local (relatif)
sqlite:////chemin/absolu/fichier.db       # Fichier local (chemin absolu)
sqlite:///:memory:                        # Base en mémoire (temporaire)
```

---

### 🟨 **MySQL / MariaDB** (avec PyMySQL ou mysqlclient)
```python
mysql+pymysql://user:password@localhost/dbname
mysql+mysqlconnector://user:password@localhost/dbname
mysql+mysqldb://user:password@localhost/dbname
```

> `pymysql` est souvent plus simple à installer que `mysqldb` (qui requiert des bindings natifs C).

---

### 🟪 **PostgreSQL** (avec psycopg2)
```python
postgresql+psycopg2://user:password@localhost/dbname
```

---

### 🟫 **Oracle** (avec cx_Oracle)
```python
oracle+cx_oracle://user:password@localhost:1521/dbname
```

---

### ⬛ **Microsoft SQL Server** (avec pyodbc ou mssql+aioodbc pour async)
```python
mssql+pyodbc://user:password@server/dbname?driver=ODBC+Driver+17+for+SQL+Server
```

---

### ✅ Bonnes pratiques
- **URL encodée** : les mots de passe avec caractères spéciaux doivent être encodés (ex : `%40` pour `@`).
- **Variables d’environnement** : pour ne pas stocker les credentials en clair dans le code.
