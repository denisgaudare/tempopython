### 🔹 **Bibliothèques Standard Python utilisant les Décorateurs**
#### 1. **functools** (Standard Library)
   - **Décorateurs fournis** : `@lru_cache`, `@wraps`, `@cache`, `@partial`, etc.
   - **Usage** :
     ```python
     from functools import lru_cache

     @lru_cache(maxsize=128)
     def expensive_function(n):
         print("Computing...")
         return n * n

     print(expensive_function(10))  # Calcul
     print(expensive_function(10))  # Cache
     ```
   - **Utilité** : Optimisation des performances, évite les calculs inutiles.

#### 2. **dataclasses** (Standard Library)
   - **Décorateurs fournis** : `@dataclass`
   - **Usage** :
     ```python
     from dataclasses import dataclass

     @dataclass
     class Point:
         x: int
         y: int

     p = Point(3, 4)
     print(p)  # Point(x=3, y=4)
     ```
   - **Utilité** : Génère automatiquement `__init__`, `__repr__`, etc.

#### 3. **contextlib** (Standard Library)
   - **Décorateurs fournis** : `@contextmanager`
   - **Usage** :
     ```python
     from contextlib import contextmanager

     @contextmanager
     def my_resource():
         print("Acquiring resource")
         yield
         print("Releasing resource")

     with my_resource():
         print("Using resource")
     ```
   - **Utilité** : Créer des context managers sans définir une classe.

---

### 🔹 **Bibliothèques Externes utilisant les Décorateurs**
#### 4. **Click** (CLI)
   - **Décorateurs fournis** : `@click.command`, `@click.option`
   - **Usage** :
     ```python
     import click

     @click.command()
     @click.option("--name", default="World", help="Your name")
     def greet(name):
         click.echo(f"Hello, {name}!")

     if __name__ == "__main__":
         greet()
     ```
   - **Utilité** : Créer des interfaces CLI sans gérer manuellement `argparse`.

#### 5. **Flask** (Web Framework)
   - **Décorateurs fournis** : `@app.route`, `@app.before_request`
   - **Usage** :
     ```python
     from flask import Flask

     app = Flask(__name__)

     @app.route("/")
     def home():
         return "Hello, World!"

     if __name__ == "__main__":
         app.run()
     ```
   - **Utilité** : Définit des routes HTTP sans écrire un serveur HTTP de zéro.

#### 6. **FastAPI** (Web APIs)
   - **Décorateurs fournis** : `@app.get`, `@app.post`
   - **Usage** :
     ```python
     from fastapi import FastAPI

     app = FastAPI()

     @app.get("/")
     async def root():
         return {"message": "Hello, World"}

     if __name__ == "__main__":
         import uvicorn
         uvicorn.run(app, host="0.0.0.0", port=8000)
     ```
   - **Utilité** : Créer des API RESTful rapidement avec de la validation automatique.

#### 7. **Pydantic** (Validation des données)
   - **Décorateurs fournis** : `@validator`
   - **Usage** :
     ```python
     from pydantic import BaseModel, validator

     class User(BaseModel):
         name: str
         age: int

         @validator("age")
         def check_age(cls, value):
             if value < 18:
                 raise ValueError("Age must be at least 18")
             return value

     user = User(name="Alice", age=20)
     print(user)
     ```
   - **Utilité** : Validation et typage automatique des entrées.

#### 8. **Numba** (Optimisation JIT)
   - **Décorateurs fournis** : `@jit`
   - **Usage** :
     ```python
     from numba import jit
     import numpy as np

     @jit(nopython=True)
     def compute(arr):
         return np.sum(arr)

     arr = np.arange(1000000)
     print(compute(arr))  # Optimisé en JIT
     ```
   - **Utilité** : Accélérer les calculs numériques avec une compilation Just-In-Time (JIT).

---

### 📌 **Résumé**
| Bibliothèque | Décorateurs Importants | Utilité |
|-------------|----------------------|---------|
| `functools` | `@lru_cache`, `@wraps`, `@cache` | Optimisation, décorateurs personnalisés |
| `dataclasses` | `@dataclass` | Génération automatique de classes |
| `contextlib` | `@contextmanager` | Gestion de ressources |
| **Click** | `@click.command`, `@click.option` | Création CLI |
| **Flask** | `@app.route`, `@app.before_request` | Web API et serveur HTTP |
| **FastAPI** | `@app.get`, `@app.post` | API REST ultra-rapide |
| **Pydantic** | `@validator` | Validation des données |
| **Numba** | `@jit` | Optimisation des calculs |
