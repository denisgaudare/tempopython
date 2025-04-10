# **Formation Python Avancé et Perfectionnement**

## **Introduction**
Bienvenue dans cette formation avancée sur Python. Ce support couvre les concepts avancés du langage, avec des exemples pratiques et des exercices progressifs.

---

# **1. Bonnes Pratiques et Rappels Avancés**
## 1.1 Typage Statique et Annotation de Type
Python 3.9+ introduit des types avancés pour améliorer la lisibilité et la robustesse du code.

```python
from typing import List, Dict, Tuple

def somme(liste: List[int]) -> int:
    return sum(liste)
```

🔹 **Exercice :** Ajouter des annotations de types à une fonction qui traite des dictionnaires.

---

## **2. Programmation Orientée Objet (POO) Avancée**
### 2.1 Classes et Encapsulation
```python
class CompteBancaire:
    def __init__(self, solde: float):
        self.__solde = solde  # Attribut privé

    def deposer(self, montant: float):
        self.__solde += montant

    def afficher_solde(self):
        return self.__solde
```

🔹 **Exercice :** Implémenter une classe `CompteEpargne` avec un taux d'intérêt appliqué annuellement.

---

## **3. Gestion de la Mémoire et Optimisation**
### 3.1 Utilisation de `__slots__` pour réduire la consommation mémoire
```python
class Optimise:
    __slots__ = ['valeur']
    def __init__(self, valeur):
        self.valeur = valeur
```

🔹 **Exercice :** Comparer l'utilisation mémoire d'une classe avec et sans `__slots__`.

---

## **4. Concurrence et Parallélisme**
### 4.1 Threading vs Multiprocessing
```python
import threading
import multiprocessing
import time

def calcul():
    print("Calcul en cours...")
    time.sleep(2)
    print("Fin du calcul")

# Threading
thread = threading.Thread(target=calcul)
thread.start()
thread.join()

# Multiprocessing
process = multiprocessing.Process(target=calcul)
process.start()
process.join()
```

🔹 **Exercice :** Exécuter 4 tâches de calcul simultanément avec `multiprocessing.Pool()`.

---

## **5. Manipulation Avancée des Données**
### 5.1 Gestion de fichiers JSON et SQLite
```python
import json

# Lecture JSON
with open("data.json", "r") as file:
    data = json.load(file)
```

🔹 **Exercice :** Écrire un script qui stocke des données dans une base SQLite et les expose via une API Flask.

---

## **6. Programmation Fonctionnelle**
### 6.1 Utilisation de `map()`, `filter()` et `reduce()`
```python
from functools import reduce

nombres = [1, 2, 3, 4]
somme = reduce(lambda x, y: x + y, nombres)
print(somme)  # 10
```

🔹 **Exercice :** Utiliser `map()` et `filter()` pour transformer une liste de données.

---

## **7. Sécurité en Python**
### 7.1 Chiffrement des données avec `cryptography`
```python
from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)
message = cipher.encrypt(b"Message secret")
print(cipher.decrypt(message))
```

🔹 **Exercice :** Implémenter un système de stockage de mots de passe chiffrés.

---

## **8. Tests et Qualité du Code**
### 8.1 Tests unitaires avec `pytest`
```python
import pytest

def addition(a, b):
    return a + b

def test_addition():
    assert addition(2, 3) == 5
```

🔹 **Exercice :** Tester une fonction de validation d'e-mail.

---

## **9. Packaging et Déploiement**
### 9.1 Création d'un module Python
```python
# setup.py
from setuptools import setup

setup(
    name='mon_module',
    version='1.0',
    packages=['mon_module']
)
```

🔹 **Exercice :** Dockeriser une application Python et la déployer sur AWS Lambda.

---

## **10. Mini-Projet Final : API de Gestion des Utilisateurs**
Objectif : Construire une API avec `FastAPI` qui gère des utilisateurs en base de données SQLite.

```python
from fastapi import FastAPI
import sqlite3

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Bienvenue dans l'API utilisateur"}
```

🔹 **Exercice final :** Ajouter des endpoints pour CRUD (Create, Read, Update, Delete) d'utilisateurs.

---

# **Conclusion**
Cette formation vous a permis d'approfondir Python, de l'optimisation à la sécurisation des applications.

**🚀 Continuez à explorer et pratiquer !**

