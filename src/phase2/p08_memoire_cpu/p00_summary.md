Comment Python gère la mémoire et comment en 
tirer parti pour améliorer le code est un 
excellent sujet, surtout pour des développeurs 
ayant déjà un peu d'expérience.

**Plan progressif** pour montrer la gestion 
mémoire en Python avec des **exemples concrets** 
et des **bonnes pratiques d’optimisation** :

---

## 🧠 1. Introduction à la gestion mémoire en Python

### Concepts de base
- **Allocation automatique** : Python gère la mémoire pour vous via un *garbage collector*.
- **Objets en mémoire** : tout est objet → chaque variable référence un objet en mémoire.
- **Références comptées** : Python utilise un *compteur de références* pour savoir si un objet est toujours utilisé.
- **Garbage collection cyclique** : pour détecter les cycles d’objets qui se référencent entre eux.

### Code exemple – compteur de références

```python
import sys

a = []
b = a
print(sys.getrefcount(a))  # souvent +1 car l’appel à getrefcount crée une référence temporaire
```

---

## 🕳 2. Fuites de mémoire et cycles

### Exemple de fuite mémoire involontaire
```python
class Node:
    def __init__(self):
        self.ref = self

a = Node()
del a  # objet non libéré car cycle de référence
```

➡️ Ce genre de cycle est détecté **périodiquement** par le *garbage collector*.

---

## ♻️ 3. Le module `gc` : contrôle du garbage collector

```python
import gc

gc.collect()  # forcer un passage du garbage collector
print(gc.get_count())  # nombre d’objets dans chaque génération
```

➡️ Utile pour détecter des fuites ou profiler.

---

## 🪶 4. Optimiser la mémoire : bonnes pratiques

### a. Préférer les **générateurs** aux listes
```python
def gen():
    for i in range(10**6):
        yield i

sum(gen())  # consommation mémoire minimale
```

➡️ Comparer avec : `sum([i for i in range(10**6)])`

### b. Utiliser `__slots__` dans les classes

```python
class Normal:
    def __init__(self):
        self.a = 1
        self.b = 2

class Slim:
    __slots__ = ('a', 'b')
    def __init__(self):
        self.a = 1
        self.b = 2

print(sys.getsizeof(Normal()))  # > Slim()
print(sys.getsizeof(Slim()))
```

➡️ `__slots__` évite la création d’un `__dict__` → gain mémoire significatif.

### c. Réutiliser les objets quand c’est possible (ex : buffer)

---

## 📦 5. Profiler la mémoire

### a. Avec `tracemalloc`

```python
import tracemalloc

tracemalloc.start()

# Code gourmand ici
big_list = [i for i in range(100000)]

snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')

for stat in top_stats[:5]:
    print(stat)
```

### b. Avec `memory_profiler`

```python
from memory_profiler import profile

@profile
def my_func():
    a = [1] * (10**6)
    b = [2] * (2 * 10**6)
    del b
    return a

my_func()
```

➡️ Lancer avec : `mprof run script.py` puis `mprof plot`

---

## 🛠️ 6. Bonnes pratiques générales

| Astuce | Pourquoi ? |
|--------|------------|
| Préférer les itérateurs/générateurs | Moins de mémoire allouée |
| Supprimer explicitement les objets (avec `del`) | Pour libérer plus tôt |
| Utiliser `__slots__` si les classes sont nombreuses | Économie de mémoire importante |
| Utiliser `array`, `numpy` au lieu de listes de nombres | Objets plus compacts |
| Ne pas garder de références inutiles | Évite de bloquer le GC |

---

Souhaites-tu un notebook d'exemples prêts à tester, ou une version orientée formation avec slides + démo ?