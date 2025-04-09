Python propose plusieurs **outils intégrés (préinstallés)** et des **bibliothèques standard** pour le **monitoring statique, dynamique, technique et fonctionnel**. Voici un aperçu des outils disponibles et comment les utiliser avec des exemples concrets.

---

# **1. Monitoring Statique (Analyse du code sans exécution)**
Le **monitoring statique** permet d'analyser le code **sans l'exécuter** pour détecter des erreurs, améliorer les performances et assurer la conformité aux bonnes pratiques.

## **1.1 `py_compile` (Vérification de syntaxe)**
Python dispose du module **py_compile** pour vérifier si un script est syntaxiquement valide.

### 🔹 **Exemple : Compiler un script pour vérifier les erreurs**
```python
import py_compile

py_compile.compile("script.py")  # Vérifie si script.py contient des erreurs de syntaxe
```
💡 **Usage** : Détecte les erreurs syntaxiques sans exécuter le code.

---

## **1.2 `ast` (Abstract Syntax Tree)**
Le module **ast** permet d'analyser un code Python sous forme d'arbre syntaxique.

### 🔹 **Exemple : Vérifier si un script contient une boucle `while`**
```python
import ast

code = """
while True:
    print("Boucle infinie")
"""

tree = ast.parse(code)
has_while = any(isinstance(node, ast.While) for node in ast.walk(tree))
print("Le code contient une boucle while :", has_while)
```
💡 **Usage** : Audit de code, refactoring, analyse de style.

---

## **1.3 `tokenize` (Analyse de tokens)**
Le module **tokenize** analyse un script ligne par ligne en identifiant ses composants.

### 🔹 **Exemple : Identifier tous les noms de variables**
```python
import tokenize
from io import BytesIO

code = b"x = 10\ny = 20\nprint(x + y)"
tokens = tokenize.tokenize(BytesIO(code).readline)

for token in tokens:
    print(token)
```
💡 **Usage** : Audit de code, génération de documentation, détection de noms non conformes.

---

# **2. Monitoring Dynamique (Analyse pendant l'exécution)**
Le **monitoring dynamique** permet d'analyser le comportement du programme pendant son exécution.

## **2.1 `trace` (Suivi de l'exécution ligne par ligne)**
Le module **trace** permet de suivre l'exécution d'un script.

### 🔹 **Exemple : Exécuter un script avec suivi de l'exécution**
```python
import trace

tracer = trace.Trace(trace=True, count=False)
tracer.run('print("Hello World")')
```
💡 **Usage** : Debugging avancé, identification des lignes exécutées.

---

## **2.2 `cProfile` (Profilage de performance)**
Le module **cProfile** permet d’analyser **les performances** du code.

### 🔹 **Exemple : Profilage d’une fonction**
```python
import cProfile

def test():
    total = sum(range(10000))
    print(total)

cProfile.run('test()')
```
💡 **Usage** : Détection des goulots d’étranglement dans le code.

---

## **2.3 `sys` (Suivi de la mémoire et des ressources)**
Le module **sys** permet d’obtenir des informations sur l’état du programme.

### 🔹 **Exemple : Afficher la mémoire occupée par un objet**
```python
import sys

x = [1] * 1000
print("Taille en mémoire :", sys.getsizeof(x), "octets")
```
💡 **Usage** : Analyse de l'utilisation mémoire, détection de fuites mémoire.

---

# **3. Monitoring Technique (Suivi des ressources et des logs)**
Le **monitoring technique** vise à surveiller l'utilisation des **ressources système**.

## **3.1 `logging` (Gestion des logs)**
Le module **logging** permet de gérer des journaux d'événements.

### 🔹 **Exemple : Écrire un log dans un fichier**
```python
import logging

logging.basicConfig(filename="app.log", level=logging.INFO)
logging.info("Ceci est un message d'information")
```
💡 **Usage** : Suivi des erreurs, audits d'exécution.

---

## **3.2 `resource` (Surveillance de la consommation CPU et mémoire)**
Le module **resource** (Linux/macOS uniquement) permet d'obtenir la consommation mémoire et CPU.

### 🔹 **Exemple : Mesurer le temps CPU utilisé par le script**
```python
import resource

usage = resource.getrusage(resource.RUSAGE_SELF)
print("Temps CPU utilisé :", usage.ru_utime, "secondes")
```
💡 **Usage** : Suivi des performances et détection de surconsommation de ressources.

---

## **3.3 `psutil` (Surveillance des ressources système)**
Le module **psutil** permet de récupérer des informations sur l'usage CPU et mémoire (besoin d'installation).

### 🔹 **Exemple : Afficher l’utilisation CPU et mémoire**
```python
import psutil

print("Utilisation CPU :", psutil.cpu_percent(), "%")
print("Mémoire disponible :", psutil.virtual_memory().available / 1024 / 1024, "MB")
```
💡 **Usage** : Surveillance des serveurs et applications.

---

# **4. Monitoring Fonctionnel (Tests et validation)**
Le **monitoring fonctionnel** permet d’assurer que l’application fonctionne comme prévu.

## **4.1 `unittest` (Tests unitaires)**
Le module **unittest** permet d'écrire et d'exécuter des tests.

### 🔹 **Exemple : Tester une fonction**
```python
import unittest

def add(a, b):
    return a + b

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

if __name__ == "__main__":
    unittest.main()
```
💡 **Usage** : Tester la validité du code automatiquement.

---

## **4.2 `doctest` (Tests intégrés dans la documentation)**
Le module **doctest** exécute des tests à partir de la documentation.

### 🔹 **Exemple : Ajouter un test dans un commentaire**
```python
def square(x):
    """
    Retourne le carré de x.

    >>> square(3)
    9
    >>> square(0)
    0
    """
    return x * x

import doctest
doctest.testmod()
```
💡 **Usage** : Assurer la cohérence entre la documentation et l’implémentation.

---

## **4.3 `timeit` (Mesure du temps d’exécution d’une fonction)**
Le module **timeit** permet de chronométrer l’exécution d’un code.

### 🔹 **Exemple : Mesurer le temps d'exécution d'une fonction**
```python
import timeit

def test():
    return sum(range(1000))

print(timeit.timeit("test()", globals=globals(), number=10000))
```
💡 **Usage** : Comparer différentes implémentations d’un algorithme.

---

# **📌 Récapitulatif des outils Python pour le monitoring**
| **Catégorie**  | **Outil** | **Utilité** |
|--------------|-----------|------------|
| **Statique** | `py_compile` | Vérifier la syntaxe |
|              | `ast` | Analyser la structure du code |
|              | `tokenize` | Identifier les éléments du code |
| **Dynamique** | `trace` | Suivre l'exécution du code |
|              | `cProfile` | Profiler les performances |
|              | `sys` | Suivre la mémoire utilisée |
| **Technique** | `logging` | Gérer les logs |
|              | `resource` | Mesurer l'utilisation CPU/mémoire |
|              | `psutil` | Surveiller les ressources système |
| **Fonctionnel** | `unittest` | Exécuter des tests unitaires |
|              | `doctest` | Tester directement depuis la doc |
|              | `timeit` | Mesurer le temps d'exécution |

---