# **📌 Les Décateurs Standard et Externes en Python 🚀**

Les **décorateurs** permettent **d'ajouter dynamiquement des fonctionnalités aux fonctions et classes**. Python fournit plusieurs **décorateurs standard**, et des bibliothèques **externes populaires** apportent des fonctionnalités avancées.

---

## **🔹 1. Décorateurs standard en Python**
### 📌 **Pourquoi utiliser des décorateurs standard ?**
✅ **Intégrés nativement** → Pas besoin d'installation supplémentaire.  
✅ **Facilitent la programmation orientée objet** (ex: `@staticmethod`).  
✅ **Optimisent la gestion des ressources** (ex: `@property`).  

---

## **1.1 `@staticmethod` → Méthodes sans `self`**
📌 **Utilisé lorsqu’une méthode ne dépend d'aucune donnée de l'instance.**

### **Exemple**
```python
class Airport:
    @staticmethod
    def general_info():
        return "Tous les aéroports suivent les règles de l'OACI."

print(Airport.general_info())  # ✅ Fonctionne sans créer d'objet
```
✅ **Évite d’instancier une classe si ce n’est pas nécessaire.**  

---

## **1.2 `@classmethod` → Accéder à la classe directement**
📌 **Permet de modifier un attribut de classe au lieu de l'instance.**

### **Exemple**
```python
class Aircraft:
    fleet_size = 0  # Attribut de classe

    def __init__(self, name: str):
        self.name = name
        Aircraft.increment_fleet()

    @classmethod
    def increment_fleet(cls):
        cls.fleet_size += 1

plane1 = Aircraft("Boeing 737")
plane2 = Aircraft("Airbus A320")
print(Aircraft.fleet_size)  # ✅ 2
```
✅ **Permet d’agir sur tous les objets (`fleet_size`) sans les instancier.**  

---

## **1.3 `@property` → Convertir une méthode en attribut**
📌 **Permet d’accéder à une méthode comme si c’était un attribut.**

### **Exemple**
```python
class Aircraft:
    def __init__(self, fuel: float):
        self._fuel = fuel  # Convention: attribut privé

    @property
    def fuel_status(self) -> str:
        """Retourne un statut lisible du carburant."""
        return "🔴 Bas" if self._fuel < 50 else "🟢 OK"

plane = Aircraft(30)
print(plane.fuel_status)  # ✅ 🔴 Bas
# plane.fuel_status = 100  # ❌ Erreur, car readonly
```
✅ **Empêche la modification accidentelle d’un attribut sensible.**  

---

## **1.4 `@functools.lru_cache` → Mémorisation automatique**
📌 **Stocke les résultats des appels précédents pour améliorer la performance.**

### **Exemple**
```python
from functools import lru_cache
import time

@lru_cache(maxsize=100)
def slow_function(n):
    time.sleep(2)  # Simule un calcul lent
    return n * 2

print(slow_function(10))  # ✅ Prend 2s
print(slow_function(10))  # ✅ Instantané (mis en cache)
```
✅ **Accélère considérablement les calculs répétitifs.**  

---

## **1.5 `@functools.wraps` → Conserver les métadonnées des fonctions décorées**
📌 **Évite la perte du `__name__`, `__doc__` et d'autres informations lors de l’utilisation de décorateurs.**

### **Exemple**
```python
from functools import wraps

def log_execution(func):
    """Décorateur qui log l'exécution d'une fonction."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"📜 Exécution de `{func.__name__}`...")
        return func(*args, **kwargs)
    return wrapper

@log_execution
def process_data():
    """Traite les données."""
    print("📊 Données traitées.")

print(process_data.__name__)  # ✅ process_data (sans wraps, affiche `wrapper`)
```
✅ **Préserve la documentation et le nom d'origine de la fonction.**  

---

# **🔹 2. Bibliothèques externes de décorateurs populaires**
Les **bibliothèques PyPI** ajoutent des fonctionnalités avancées aux décorateurs.

---

## **2.1 `decorator` → Manipuler facilement les décorateurs**
📌 **Simplifie la création de décorateurs tout en conservant les métadonnées.**

### **Installation**
```bash
pip install decorator
```

### **Exemple**
```python
from decorator import decorator

@decorator
def log_execution(func, *args, **kwargs):
    print(f"📜 Exécution de `{func.__name__}`...")
    return func(*args, **kwargs)

@log_execution
def process_data():
    print("📊 Données traitées.")

process_data()  # ✅ Ajoute un log avant exécution
```
✅ **Moins de code à écrire comparé à `wraps()`.**  

---

## **2.2 `attrs` → Créer des classes immuables avec un décorateur**
📌 **Remplace `dataclasses` avec plus de flexibilité et performance.**

### **Installation**
```bash
pip install attrs
```

### **Exemple**
```python
import attr

@attr.s(frozen=True)  # Rend la classe immuable
class Aircraft:
    flight_name = attr.ib(type=str)
    capacity = attr.ib(type=int)

plane = Aircraft("AF101", 180)
# plane.capacity = 200  # ❌ Erreur : immuable
```
✅ **Meilleure gestion de l’immuabilité que `dataclasses`.**  

---

## **2.3 `pytest` → Décorateurs pour les tests unitaires**
📌 **Ajoute des fonctionnalités avancées pour tester des fonctions.**

### **Installation**
```bash
pip install pytest
```

### **Exemple**
```python
import pytest

@pytest.mark.slow
def test_large_computation():
    assert sum(range(1000000)) > 0
```
✅ **Marque les tests pour exécuter certaines catégories uniquement.**  

---

## **2.4 `loguru` → Simplifier le logging avec un décorateur**
📌 **Remplace le module `logging` avec une syntaxe plus intuitive.**

### **Installation**
```bash
pip install loguru
```

### **Exemple**
```python
from loguru import logger

@logger.catch
def divide(a, b):
    return a / b

divide(10, 0)  # ✅ Capture automatiquement l'erreur
```
✅ **Évite d'écrire des blocs `try/except` manuellement.**  

---

## **🔥 Conclusion**
| **Pourquoi utiliser ces décorateurs ?** ✅ |
|---------------------------------------------|
| **Réduit la duplication du code** 📉 |
| **Rend le code plus lisible et modulaire** 🎯 |
| **Ajoute des fonctionnalités avancées** 🚀 |
| **Simplifie la gestion des erreurs et logs** 🔥 |

| **Décorateur** | **Utilité** |
|---------------|------------|
| **`@staticmethod`** | Méthodes sans `self` |
| **`@classmethod`** | Accède à la classe directement |
| **`@property`** | Convertit une méthode en attribut |
| **`@functools.lru_cache`** | Cache les résultats d'une fonction |
| **`@functools.wraps`** | Préserve les métadonnées des fonctions décorées |
| **`decorator` (lib)** | Simplifie la création de décorateurs |
| **`attrs` (lib)** | Crée des classes immuables |
| **`pytest` (lib)** | Ajoute des fonctionnalités de test |
| **`loguru` (lib)** | Simplifie le logging avec un décorateur |

**🚀 Maîtriser les décorateurs standards et externes est essentiel pour un code Python propre, performant et modulaire !** 🔥