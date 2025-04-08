### **Cas Pratique : Gestionnaire de Connexion à une Base de Données (Singleton + Métaclasse)**

Quand une application interagit fréquemment avec une base de données, il est préférable de **réutiliser une connexion unique** plutôt que d’en ouvrir une nouvelle à chaque requête. Un **Singleton avec Métaclasse** garantit que **seule une instance de la connexion est créée**.

---

## **1. Implémentation d'un Gestionnaire de Connexion DB en Singleton**
On va utiliser `aiomysql` pour une connexion MySQL asynchrone avec un **singleton**.

```python
import aiomysql
import asyncio

class SingletonMeta(type):
    """Métaclasse Singleton pour s'assurer qu'une seule connexion DB est créée"""
    _instances = {}

    async def __call__(cls, *args, **kwargs):
        """Surcharge de __call__ pour créer une seule instance"""
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
            await cls._instances[cls].connect()  # Création de la connexion async
        return cls._instances[cls]

class AsyncDBConnection(metaclass=SingletonMeta):
    """Gestionnaire de connexion à la base de données en mode Singleton"""
    def __init__(self, host, port, user, password, db):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db
        self.pool = None

    async def connect(self):
        """Établit la connexion en utilisant un pool de connexions"""
        self.pool = await aiomysql.create_pool(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.db,
            autocommit=True  # Permet de valider automatiquement les big_transactions
        )
        print("Connexion MySQL ouverte (Singleton)")

    async def execute(self, query, params=None):
        """Exécute une requête SQL et retourne le résultat"""
        async with self.pool.acquire() as conn:  # Récupère une connexion du pool
            async with conn.cursor() as cursor:
                await cursor.execute(query, params or ())
                return await cursor.fetchall()  # Retourne le résultat

    async def close(self):
        """Ferme proprement la connexion"""
        if self.pool:
            self.pool.close()
            await self.pool.wait_closed()
            print("Connexion MySQL fermée (Singleton)")

# Utilisation
async def main():
    db = await AsyncDBConnection("localhost", 3306, "root", "password", "test_db")

    # Exécution d'une requête SQL
    result = await db.execute("SELECT * FROM users")
    print("Résultats de la requête :", result)

    # Fermeture propre de la connexion
    await db.close()

asyncio.run(main())
```

---

## **🔍 Explication**
1. **Métaclasse `SingletonMeta`** :
   - Vérifie si une instance existe déjà (`_instances`).
   - Si non, elle en crée une et **appelle `connect()`**.
   - **Surcharge de `__call__` avec `async`** pour gérer une connexion asynchrone.

2. **Classe `AsyncDBConnection`** :
   - Utilise un **pool de connexions** pour optimiser l'accès à MySQL.
   - Fournit une méthode `execute(query, params)` pour exécuter des requêtes SQL.
   - **Singleton** : toutes les requêtes utilisent **la même instance de connexion**.

3. **Dans `main()`** :
   - On récupère une instance unique de `AsyncDBConnection`.
   - On exécute une requête `SELECT * FROM users`.
   - On ferme proprement la connexion.

---

## **2. Version avec Thread-Safety (Connexion Synchronous)**
Si on travaille en **mode synchrone**, voici une version thread-safe avec `mysql-connector-python` :

```python
import mysql.connector
import threading

class ThreadSafeSingletonMeta(type):
    """Métaclasse Singleton thread-safe pour gestion de connexion DB"""
    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:  # Protection contre les accès concurrents
            if cls not in cls._instances:
                cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class SyncDBConnection(metaclass=ThreadSafeSingletonMeta):
    """Gestionnaire de connexion DB Singleton pour mode synchrone"""
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()
        print("Connexion MySQL ouverte (Singleton)")

    def execute(self, query, params=None):
        """Exécute une requête SQL synchronisée"""
        self.cursor.execute(query, params or ())
        return self.cursor.fetchall()

    def close(self):
        """Ferme la connexion proprement"""
        self.cursor.close()
        self.conn.close()
        print("Connexion MySQL fermée (Singleton)")

# Utilisation
db = SyncDBConnection("localhost", "root", "password", "test_db")
result = db.execute("SELECT * FROM users")
print("Résultats de la requête :", result)
db.close()
```

---

## **📌 Comparatif des Approches**
| Méthode | Type | Cas d'utilisation | Avantages | Inconvénients |
|---------|------|------------------|-----------|--------------|
| **`AsyncDBConnection`** | Asynchrone | Apps modernes avec `asyncio` et `aiomysql` | Optimisé pour les I/O, scalable | Nécessite un event loop (`asyncio`) |
| **`SyncDBConnection`** | Synchrone | Scripts classiques, sans `asyncio` | Plus simple à intégrer | Bloque l'exécution des threads |
| **Thread-Safe Singleton** | Synchrone + Multi-thread | Accès concurrent à la DB | Protège l'accès aux données | Nécessite un `Lock` |

---

## **📌 Conclusion**
- **Si ton application est asynchrone (FastAPI, `asyncio`)** → Utilise `AsyncDBConnection` avec **`aiomysql`**.
- **Si ton code est synchrone (Flask, Django classique)** → Utilise `SyncDBConnection` avec **`mysql-connector`**.
- **Si ton programme est multi-threadé** → Ajoute un **verrou (`Lock`)** pour éviter les problèmes d’accès concurrent.