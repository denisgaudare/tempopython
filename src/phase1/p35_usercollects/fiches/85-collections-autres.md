
## **1. collections – Structures de données avancées**
Le module [`collections`](https://docs.python.org/3/library/collections.html) fournit plusieurs structures optimisées :

### ✅ **OrderedDict**
- **Description** : Un dictionnaire qui **conserve l'ordre** d'insertion des éléments (utile avant Python 3.7, où `dict` ne garantissait pas l'ordre).
- **Utilité** : Pratique pour les cas où l’ordre des clés est important.
  
```python
from collections import OrderedDict

ordered_dict = OrderedDict()
ordered_dict["a"] = 1
ordered_dict["b"] = 2
ordered_dict["c"] = 3

print(ordered_dict)  # OrderedDict([('a', 1), ('b', 2), ('c', 3)])
```

---

### ✅ **defaultdict**
- **Description** : Un `dict` qui permet de définir une valeur par défaut pour les clés inexistantes.
- **Utilité** : Évite les `KeyError` et facilite l'initialisation des valeurs.

```python
from collections import defaultdict

numbers = defaultdict(int)  # Par défaut, les valeurs sont 0
numbers["x"] += 1
print(numbers["x"])  # 1
print(numbers["y"])  # 0 (au lieu de KeyError)
```

---

### ✅ **deque**
- **Description** : Une liste optimisée pour **les ajouts/suppressions en début et fin** (`O(1)` au lieu de `O(n)` pour `list`).
- **Utilité** : Parfait pour implémenter une **file (FIFO)** ou une **pile (LIFO)**.

```python
from collections import deque

dq = deque()
dq.append(1)       # Ajout en fin
dq.appendleft(2)   # Ajout en début
dq.pop()           # Suppression en fin
dq.popleft()       # Suppression en début
```

---

### ✅ **Counter**
- **Description** : Un `dict` qui compte les occurrences des éléments.
- **Utilité** : Idéal pour les analyses statistiques, comptages rapides.

```python
from collections import Counter

letters = Counter("banana")
print(letters)  # Counter({'a': 3, 'n': 2, 'b': 1})
```

---

### ✅ **namedtuple**
- **Description** : Un `tuple` amélioré avec des **noms de champs**.
- **Utilité** : Permet un accès plus lisible aux éléments (alternative légère aux classes).

```python
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
print(p.x, p.y)  # 10 20
```

---

## **2. heapq – Gestion efficace des files de priorité**
Le module [`heapq`](https://docs.python.org/3/library/heapq.html) fournit une implémentation de **tas (heap)** sous forme de liste.

### ✅ **heap (tas)**
- **Description** : Une structure **triée dynamiquement** (min-heap ou max-heap).
- **Utilité** : Idéale pour récupérer rapidement **l'élément minimum (O(1))** et faire des tri partiels (`O(log n)` pour l’insertion et suppression).

```python
import heapq

heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)

print(heapq.heappop(heap))  # 1 (plus petit élément)
```

---

## **3. queue – Structures de file d'attente**
Le module [`queue`](https://docs.python.org/3/library/queue.html) fournit différentes **files d’attente synchronisées** :

### ✅ **Queue (FIFO)**
- **Utilité** : Utilisée pour des **tâches en attente** dans des applications multi-thread.

```python
from queue import Queue

q = Queue()
q.put(1)
q.put(2)
print(q.get())  # 1 (premier ajouté, premier sorti)
```

---

### ✅ **LifoQueue (LIFO)**
- **Utilité** : Implémente une **pile** (dernier ajouté, premier sorti).

```python
from queue import LifoQueue

stack = LifoQueue()
stack.put(1)
stack.put(2)
print(stack.get())  # 2 (dernier ajouté, premier sorti)
```

---

### ✅ **PriorityQueue**
- **Utilité** : Permet d’insérer des **éléments avec une priorité**, similaire à `heapq`.

```python
from queue import PriorityQueue

pq = PriorityQueue()
pq.put((2, "task2"))
pq.put((1, "task1"))  # Priorité 1 (le plus prioritaire)
print(pq.get())  # (1, 'task1')
```

---

## **4. array – Tableaux optimisés**
Le module [`array`](https://docs.python.org/3/library/array.html) fournit des **tableaux optimisés** pour stocker un grand nombre de nombres **du même type**.

- **Utilité** : Alternative plus efficace aux `list` pour manipuler des grandes quantités de données numériques.

```python
import array

arr = array.array("i", [1, 2, 3, 4])  # "i" pour des entiers
print(arr[1])  # 2
```

---

## **5. bisect – Recherche et insertion optimisées**
Le module [`bisect`](https://docs.python.org/3/library/bisect.html) permet des **recherches et insertions binaires** efficaces.

- **Utilité** : Utile pour **maintenir une liste triée** sans refaire de tri à chaque ajout.

```python
import bisect

numbers = [1, 3, 4, 10]
bisect.insort(numbers, 5)  # Insère 5 tout en gardant la liste triée
print(numbers)  # [1, 3, 4, 5, 10]
```

---

## **Résumé des structures et utilisations**
| Structure | Module | Utilité principale |
|-----------|--------|--------------------|
| **OrderedDict** | `collections` | Dictionnaire ordonné |
| **defaultdict** | `collections` | Dictionnaire avec valeurs par défaut |
| **deque** | `collections` | File ou pile efficace |
| **Counter** | `collections` | Comptage d'occurrences |
| **namedtuple** | `collections` | Tuple avec noms de champs |
| **heapq** | `heapq` | Gestion des files de priorité |
| **Queue** | `queue` | File d'attente synchronisée (FIFO) |
| **LifoQueue** | `queue` | Pile (LIFO) |
| **PriorityQueue** | `queue` | File de priorité |
| **array** | `array` | Tableau optimisé pour les nombres |
| **bisect** | `bisect` | Insertion et recherche binaire |
