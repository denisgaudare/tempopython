### **Cas pratique : Gestion de Transactions MySQL Asynchrones avec `aiomysql` et Context Manager**
Les **transactions** permettent de garantir l'intégrité des données en s'assurant que toutes les requêtes d'un bloc soient exécutées **entièrement** (`COMMIT`) ou **annulées** (`ROLLBACK`) en cas d'erreur.

---

## **1. Installation d'`aiomysql` (si besoin)**
Si ce n'est pas encore fait, installe `aiomysql` :
```sh
pip install aiomysql
```

---

## **2. Création d’un context manager gérant automatiquement les transactions**
On va créer une classe qui **ouvre une connexion MySQL**, **démarre une transaction** et **valide ou annule** en fonction du résultat.

```python
import aiomysql
import asyncio

class AsyncMySQLTransaction:
    def __init__(self, host, port, user, password, db):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db
        self.conn = None
        self.cursor = None

    async def __aenter__(self):
        """Connexion MySQL et début de transaction"""
        self.conn = await aiomysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.db,
            autocommit=False  # Désactive l'autocommit pour gérer la transaction manuellement
        )
        self.cursor = await self.conn.cursor()
        print("Connexion MySQL ouverte et début de transaction")
        return self.cursor  # Retourne le curseur pour exécuter les requêtes SQL

    async def __aexit__(self, exc_type, exc_value, traceback):
        """Validation (COMMIT) ou annulation (ROLLBACK) de la transaction"""
        if exc_type is None:
            await self.conn.commit()
            print("Transaction validée (COMMIT)")
        else:
            await self.conn.rollback()
            print(f"Transaction annulée (ROLLBACK) à cause de : {exc_value}")

        await self.cursor.close()
        self.conn.close()
        await self.conn.wait_closed()
        print("Connexion MySQL fermée")

# Utilisation :
async def insert_data():
    async with AsyncMySQLTransaction(
        host="localhost", port=3306, user="root", password="password", db="test_db"
    ) as cursor:
        await cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ("Alice", 30))
        await cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ("Bob", 25))
        # raise Exception("Simulation d'erreur")  # Décommenter pour tester le ROLLBACK

asyncio.run(insert_data())
```

✅ **Pourquoi utiliser un context manager ici ?**
- **Démarre automatiquement une transaction.**
- **Si tout se passe bien → `COMMIT` (valide les changements).**
- **Si une erreur survient → `ROLLBACK` (annule les changements).**
- **Ferme proprement la connexion MySQL et le curseur.**

---

## **3. Version avec `contextlib.asynccontextmanager` (plus compacte)**
Si tu préfères une **version plus concise**, on peut utiliser `contextlib.asynccontextmanager` :

```python
from contextlib import asynccontextmanager
import aiomysql

@asynccontextmanager
async def mysql_transaction(host, port, user, password, db):
    """Context manager asynchrone pour gérer une transaction MySQL"""
    conn = await aiomysql.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        db=db,
        autocommit=False  # On gère manuellement la transaction
    )
    cursor = await conn.cursor()
    print("Connexion MySQL ouverte et début de transaction")
    try:
        yield cursor
        await conn.commit()
        print("Transaction validée (COMMIT)")
    except Exception as e:
        await conn.rollback()
        print(f"Transaction annulée (ROLLBACK) à cause de : {e}")
    finally:
        await cursor.close()
        conn.close()
        await conn.wait_closed()
        print("Connexion MySQL fermée")

# Utilisation :
async def insert_data():
    async with mysql_transaction("localhost", 3306, "root", "password", "test_db") as cursor:
        await cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ("Charlie", 40))
        await cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ("Diana", 22))
        # raise Exception("Simulation d'erreur")  # Tester l'annulation automatique

asyncio.run(insert_data())
```

✅ **Pourquoi utiliser cette approche ?**
- **Évite d’écrire une classe.**
- **Même logique : `COMMIT` si tout va bien, `ROLLBACK` en cas d'erreur.**
- **Facilement réutilisable** pour plusieurs transactions.

---

### **📌 Comparatif des Approches**
| Méthode | Cas d'utilisation | Avantages | Inconvénients |
|---------|------------------|-----------|--------------|
| **Classe avec `__aenter__` et `__aexit__`** | Gestion avancée des transactions | Plus flexible, extensible | Plus de code |
| **`asynccontextmanager`** | Transactions rapides et temporaires | Plus concis, plus lisible | Moins flexible si besoin d'ajouter des fonctionnalités supplémentaires |

---

### **📌 Conclusion**
- **Si tu veux une gestion fine des transactions (logs, diagnostics, métriques, etc.)** → **Utilise une classe.**
- **Si tu veux une version rapide et simple** → **Utilise `asynccontextmanager`.**
- **Dans tous les cas, un context manager permet de garantir que la connexion est bien fermée et que la transaction est bien gérée**.

Tu veux un exemple avec **une connexion à PostgreSQL (`asyncpg`)** ou avec **une transaction plus avancée** (ex. plusieurs bases de données) ? 🚀