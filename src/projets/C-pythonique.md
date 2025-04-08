

# **🔹 1. Bibliothèques standards pour un code robuste et élégant**
La bibliothèque standard de Python propose déjà **de nombreux outils** pour un **code propre, efficace et sécurisé**.

## **1.1 `dataclasses` → Alternative élégante aux classes classiques**
✅ Remplace les classes verbeuses par une approche plus propre et expressive.

### **Exemple**
```python
from dataclasses import dataclass

@dataclass
class Aircraft:
    flight_name: str
    capacity: int
    fuel: float = 100.0  # Valeur par défaut

plane = Aircraft("Flight 101", 180)
print(plane)  # Aircraft(flight_name='Flight 101', capacity=180, fuel=100.0)
```

📌 **Avantages** :
- Réduction du **code boilerplate**.
- Génère automatiquement `__init__`, `__repr__`, `__eq__`.

---

## **1.2 `contextlib` → Gestion avancée des context managers**
✅ Simplifie la gestion des ressources via des **context managers**.

### **Exemple : Un context manager pour mesurer le temps d'exécution**
```python
from contextlib import contextmanager
import time

@contextmanager
def timer():
    start = time.time()
    yield
    print(f"⏳ Temps écoulé : {time.time() - start:.2f}s")

with timer():
    time.sleep(2)  # Simule une opération longue
```

📌 **Avantages** :
- Gère automatiquement **l'ouverture/fermeture des ressources**.
- Évite d'oublier `finally` pour la libération des ressources.

---

## **1.3 `functools` → Optimisation et élégance**
✅ Fournit des outils avancés pour **optimiser et organiser le code**.

### **Exemple : Mémorisation des résultats (caching)**
```python
from functools import lru_cache

@lru_cache(maxsize=100)
def slow_function(n):
    time.sleep(2)  # Simule un calcul lent
    return n * 2

print(slow_function(10))  # Exécute normalement
print(slow_function(10))  # Récupéré en cache (instantané)
```

📌 **Avantages** :
- Accélère **les calculs répétitifs**.
- Facile à implémenter sans modifier le code existant.

---

## **1.4 `itertools` → Manipulation efficace des collections**
✅ Fournit des **outils puissants** pour les listes, tuples, et autres itérables.

### **Exemple : Création infinie d’identifiants**
```python
from itertools import count

id_generator = count(start=1)
print(next(id_generator))  # 1
print(next(id_generator))  # 2
print(next(id_generator))  # 3
```

📌 **Avantages** :
- **Évite les boucles inutiles**.
- Fournit **des combinaisons, permutations et itérations optimisées**.

---

# **🔹 2. Bibliothèques PyPI pour un code professionnel**
Les bibliothèques de **PyPI** permettent de rendre un code plus **puissant, sécurisé et maintenable**.

## **2.1 `pydantic` → Validation stricte des données**
✅ Génère des **modèles robustes** avec **vérification automatique des types**.

### **Exemple**
```python
from pydantic import BaseModel, conint

class FlightModel(BaseModel):
    flight_name: str
    passengers: conint(gt=0)  # Doit être > 0

flight = FlightModel(flight_name="Flight 101", passengers=150)
# flight = FlightModel(flight_name="Flight 101", passengers=-5)  # ⛔ Erreur
```

📌 **Avantages** :
- **Vérifie les types en temps réel**.
- Gère **JSON, bases de données et API REST**.

---

## **2.2 `rich` → Affichage élégant des logs et du debugging**
✅ Améliore **l'affichage des logs, erreurs et tableaux** en console.

### **Exemple**
```python
from rich.console import Console

console = Console()
console.print("[bold green]Succès ![/] L'avion a décollé.")
```

📌 **Avantages** :
- **Affichage coloré et interactif**.
- **Facilite le debugging et les logs**.

---

## **2.3 `typer` → Création de CLI élégantes**
✅ Permet de **créer des interfaces en ligne de commande** en **quelques lignes**.

### **Exemple**
```python
import typer

app = typer.Typer()

@app.command()
def greet(name: str):
    """Affiche un message de bienvenue."""
    print(f"👋 Bonjour, {name} !")

if __name__ == "__main__":
    app()
```
📌 **Avantages** :
- **Auto-génération de `--help`**.
- **Facilité d'intégration avec les scripts Python**.

---

## **2.4 `loguru` → Logging moderne et puissant**
✅ Remplace `logging` avec **moins de code et plus de flexibilité**.

### **Exemple**
```python
from loguru import logger

logger.add("app.log", rotation="1 MB")
logger.info("L'avion a décollé !")
```

📌 **Avantages** :
- **Formatage automatique des logs**.
- **Gère plusieurs fichiers de log** sans effort.

---

## **2.5 `attrs` → Alternative avancée aux `dataclasses`**
✅ Permet d'écrire **des classes propres et robustes**.

### **Exemple**
```python
import attr

@attr.s
class Aircraft:
    flight_name = attr.ib(type=str)
    capacity = attr.ib(type=int, default=180)

plane = Aircraft("Flight 101")
print(plane)
```

📌 **Avantages** :
- **Supporte l'héritage et la validation avancée**.
- **Plus flexible que `dataclasses`**.

---

# **🎯 Récapitulatif**
| **Catégorie**          | **Bibliothèque**  | **Utilisation principale** |
|----------------------|----------------|-------------------------|
| **Standard (préinstallé)** | `dataclasses` | Classes propres et concises |
|                        | `contextlib`  | Gestion avancée des ressources |
|                        | `functools`   | Caching et optimisation |
|                        | `itertools`   | Manipulation avancée des itérables |
| **PyPI (installation requise)** | `pydantic`   | Validation stricte des données |
|                        | `rich`        | Affichage élégant en console |
|                        | `typer`       | Création simple d'interfaces CLI |
|                        | `loguru`      | Logging puissant et moderne |
|                        | `attrs`       | Alternative avancée aux dataclasses |

---

# **🔥 Conclusion**
Un **code Python robuste et élégant** repose sur **une bonne utilisation de la bibliothèque standard** et des **outils avancés** de PyPI.  
✅ **Un expert Python doit maîtriser ces bibliothèques** pour produire un **code clair, optimisé et maintenable** ! 🚀