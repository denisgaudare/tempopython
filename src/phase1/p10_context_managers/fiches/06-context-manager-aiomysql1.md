### **Cas pratique : Gestion d'une connexion MySQL asynchrone avec `aiomysql`**
Lorsqu'on utilise **`aiomysql`**, un context manager asynchrone est très utile pour s'assurer que la connexion et les curseurs sont correctement ouverts et fermés.

---

### **1. Installation d'`aiomysql` (si besoin)**
Si tu n'as pas encore `aiomysql`, installe-le avec :
```sh
pip install aiomysql
```

---

### **2. Gestion d’une connexion MySQL avec un context manager asynchrone**
On va créer un **context manager asynchrone** pour gérer automatiquement la connexion et s'assurer qu'elle est fermée proprement.

```python
import aiomysql
import asyncio

class AsyncMySQLConnection:
    def __init__(self, host, port, user, password, db):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db
        self.conn = None

    async def __aenter__(self):
        """Établit la connexion à MySQL au début du `async with`"""
        self.conn = await aiomysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.db
        )
        print("Connexion MySQL ouverte")
        return self.conn  # Permet d'utiliser `conn` dans le `async with`

    async def __aexit__(self, exc_type, exc_value, traceback):
        """Ferme la connexion à MySQL proprement à la sortie du `async with`"""
        if self.conn:
            self.conn.close()
            await self.conn.wait_closed()
            print("Connexion MySQL fermée")

# Utilisation :
async def fetch_data():
    async with AsyncMySQLConnection(
        host="localhost", port=3306, user="root", password="password", db="test_db"
    ) as conn:
        async with conn.cursor() as cursor:
            await cursor.execute("SELECT * FROM users")
            result = await cursor.fetchall()
            print("Données récupérées :", result)

asyncio.run(fetch_data())
```

✅ **Pourquoi utiliser un context manager ici ?**
- **Gestion propre** de la connexion MySQL (évite les fuites).
- **Facilité d'utilisation** avec `async with`.
- **Restaure la connexion proprement** en cas d'erreur.

---

### **3. Version avec `contextlib.asynccontextmanager` (plus concise)**
Si tu veux une version plus rapide et plus lisible, on peut utiliser `contextlib.asynccontextmanager` :

```python
from contextlib import asynccontextmanager
import aiomysql

@asynccontextmanager
async def mysql_connection(host, port, user, password, db):
    """Context manager asynchrone pour gérer la connexion MySQL"""
    conn = await aiomysql.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        db=db
    )
    print("Connexion MySQL ouverte")
    try:
        yield conn  # Retourne la connexion pour utilisation dans `async with`
    finally:
        conn.close()
        await conn.wait_closed()
        print("Connexion MySQL fermée")

# Utilisation :
async def fetch_data():
    async with mysql_connection("localhost", 3306, "root", "password", "test_db") as conn:
        async with conn.cursor() as cursor:
            await cursor.execute("SELECT * FROM users")
            result = await cursor.fetchall()
            print("Données récupérées :", result)

asyncio.run(fetch_data())
```

✅ **Pourquoi cette approche ?**
- **Moins de code** qu'avec une classe.
- **Utilisation intuitive** avec `async with`.
- **Gère proprement la connexion et sa fermeture**.

---

### **📌 Conclusion**
| Méthode | Cas d'utilisation | Avantages | Inconvénients |
|---------|------------------|-----------|--------------|
| **Classe avec `__aenter__` et `__aexit__`** | Connexion MySQL persistante | Plus de contrôle, extensible | Plus de code |
| **`asynccontextmanager`** | Connexion rapide et temporaire | Plus concis, facile à lire | Moins flexible si besoin d'ajouter des options |
