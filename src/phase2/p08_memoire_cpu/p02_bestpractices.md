# ✅ Plusieurs exemples de code problématique** côté mémoire en Python, 
## Expliquer **ce qui pose problème**, 
## puis donner une **version corrigée**.

## ⚠️ Exemples de mauvais usages mémoire et solutions

### 🔁 **1. Listes volumineuses maintenues inutilement**

#### ❌ Problème :
```python
def process():
    data = [i for i in range(10_000_000)]  # occupe beaucoup de mémoire
    return sum(data)
```

➡️ La **liste est toute chargée en mémoire**, ce qui consomme plusieurs centaines de Mo.

#### ✅ Solution : utiliser un **générateur** (lazy loading)

```python
def process():
    return sum(i for i in range(10_000_000))  # range() + générateur
```

---

### 🔁 **2. Objets avec `__dict__` par défaut (classes)**

#### ❌ Problème :
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

➡️ Chaque objet possède un `__dict__`, qui prend plus de mémoire.

#### ✅ Solution : utiliser `__slots__`

```python
class Point:
    __slots__ = ('x', 'y')  # pas de __dict__
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

➡️ Gain important si tu as des **milliers d’objets**.

---

### 🔁 **3. Structures imbriquées non nécessaires**

#### ❌ Problème :
```python
data = [[i] for i in range(10_000)]
```

➡️ Chaque `i` est dans une liste → **beaucoup d’objets en mémoire**.

#### ✅ Solution :
```python
data = list(range(10_000))  # structure plate
```

---

### 🔁 **4. Références inutiles gardées en vie**

#### ❌ Problème :
```python
results = []
for _ in range(10):
    temp = [x for x in range(1000000)]  
    results.append(temp)  

# Résultat : 10 millions d’éléments restent en mémoire
```

➡️ Garde tout en mémoire, même si tu n’en as pas besoin ensuite.

#### ✅ Solution :
```python
for _ in range(10):
    temp = [x for x in range(1000000)]
    process(temp)  # traiter puis...
    del temp       # ...libérer explicitement
```

---

### 🔁 **5. Cycles de références entre objets**

#### ❌ Problème :
```python
class A:
    def __init__(self):
        self.b = B(self)

class B:
    def __init__(self, a):
        self.a = a

a = A()
del a
```

➡️ `A` et `B` se référencent mutuellement → **cycle** → pas libérés immédiatement.

#### ✅ Solution :
- Casser manuellement la référence
- Ou utiliser `weakref` :

```python
import weakref

class A:
    def __init__(self):
        self.b = B(self)

class B:
    def __init__(self, a):
        self.a = weakref.ref(a)
```

---

## 🧰 Outils internes et externes pour maîtriser la mémoire

---

### 🛠️ Modules intégrés (standard Python)

| Module | Utilité |
|--------|--------|
| `sys.getsizeof(obj)` | Taille mémoire approximative d’un objet |
| `gc` | Contrôle et debug du garbage collector |
| `tracemalloc` | Suivi de l’allocation mémoire dans le temps |
| `resource` (Linux/macOS) | Limites mémoire par processus |

#### Exemple avec `tracemalloc` :
```python
import tracemalloc

tracemalloc.start()

# Code à profiler
big_list = [i for i in range(100000)]

snapshot = tracemalloc.take_snapshot()
for stat in snapshot.statistics('lineno')[:5]:
    print(stat)
```

---

### 🛠️ Outils externes (install via pip)

| Outil | Description |
|-------|-------------|
| `memory_profiler` | Affiche ligne par ligne l’utilisation mémoire |
| `objgraph` | Visualise les objets et les références (très utile pour cycles) |
| `pympler` | Inspecte les objets vivants et leur taille |
| `guppy3` / `heapy` | Visualisation des objets en mémoire (mode interactif) |

#### `memory_profiler` exemple :
```python
from memory_profiler import profile

@profile
def my_func():
    a = [1] * 1000000
    return sum(a)

my_func()
```

➡️ Lancer avec : `python -m memory_profiler script.py`

---
