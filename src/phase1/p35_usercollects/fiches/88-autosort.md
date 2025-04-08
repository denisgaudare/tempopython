Si tu veux créer ta propre collection proche d'une `list`,
mais qui se **trie automatiquement** à chaque ajout, 
l'idéal est d'utiliser une classe personnalisée en 
héritant de `collections.UserList` ou en 
encapsulant une liste. 
Voici plusieurs façons de le faire.

---

## 1️⃣ **Implémentation basique avec `append()` et tri automatique**
On encapsule une liste et on trie automatiquement après chaque ajout.

```python
class SortedList:
    def __init__(self, iterable=None):
        """Initialise la liste et trie les éléments existants s'il y en a"""
        self._data = sorted(iterable) if iterable else []

    def append(self, value):
        """Ajoute un élément et trie automatiquement"""
        self._data.append(value)
        self._data.sort()  # Trie la liste après l'ajout

    def extend(self, iterable):
        """Ajoute plusieurs éléments et trie automatiquement"""
        self._data.extend(iterable)
        self._data.sort()

    def __getitem__(self, index):
        """Permet l'accès aux éléments comme une liste"""
        return self._data[index]

    def __len__(self):
        """Retourne la taille de la liste"""
        return len(self._data)

    def __repr__(self):
        """Affichage de la liste triée"""
        return repr(self._data)

# Exemple d'utilisation :
slist = SortedList([5, 2, 8])
print(slist)  # [2, 5, 8]
slist.append(3)
print(slist)  # [2, 3, 5, 8]
slist.extend([7, 1])
print(slist)  # [1, 2, 3, 5, 7, 8]
```

✅ **Avantages** : Simple et efficace.  
❌ **Inconvénient** : Trie la liste entière à chaque ajout, ce qui peut être lent.

---

## 2️⃣ **Optimisation avec une insertion binaire (`bisect.insort()`)**
Une meilleure approche est d'utiliser `bisect.insort()`, qui insère l'élément directement **au bon endroit**, évitant un tri complet.

```python
import bisect

class SortedList:
    def __init__(self, iterable=None):
        """Initialise la liste triée"""
        self._data = sorted(iterable) if iterable else []

    def append(self, value):
        """Ajoute un élément à sa position correcte sans trier toute la liste"""
        bisect.insort(self._data, value)

    def extend(self, iterable):
        """Ajoute plusieurs éléments de manière optimisée"""
        for value in iterable:
            bisect.insort(self._data, value)

    def __getitem__(self, index):
        return self._data[index]

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return repr(self._data)

# Exemple d'utilisation :
slist = SortedList([5, 2, 8])
print(slist)  # [2, 5, 8]
slist.append(3)
print(slist)  # [2, 3, 5, 8]
slist.extend([7, 1])
print(slist)  # [1, 2, 3, 5, 7, 8]
```

✅ **Avantages** :
- Plus efficace, surtout pour les grandes listes.
- Évite de trier entièrement la liste après chaque ajout.

❌ **Inconvénient** :
- Moins intuitif que `sort()`, mais plus performant.

---

## 3️⃣ **Hériter de `collections.UserList`**
Une approche plus élégante consiste à utiliser `UserList`, qui permet d'hériter directement du comportement d'une liste.

```python
from collections import UserList
import bisect

class SortedList(UserList):
    def append(self, value):
        """Insère l'élément à la bonne position"""
        bisect.insort(self.data, value)

    def extend(self, iterable):
        """Ajoute plusieurs éléments triés automatiquement"""
        for value in iterable:
            bisect.insort(self.data, value)

# Exemple d'utilisation :
slist = SortedList([5, 2, 8])
print(slist)  # [2, 5, 8]
slist.append(3)
print(slist)  # [2, 3, 5, 8]
slist.extend([7, 1])
print(slist)  # [1, 2, 3, 5, 7, 8]
```

✅ **Avantages** :
- Se comporte comme une vraie `list`.
- Permet d’hériter d'autres méthodes des listes Python (`pop()`, `remove()`, etc.).

---

## 4️⃣ **Utilisation d'un `heap` (tas binaire)**
Si tu veux une structure où **l'élément le plus petit est toujours accessible rapidement**, un `heap` (tas) est une solution.

```python
import heapq

class SortedHeap:
    def __init__(self, iterable=None):
        """Crée un tas min"""
        self._data = list(iterable) if iterable else []
        heapq.heapify(self._data)

    def append(self, value):
        """Ajoute un élément au tas"""
        heapq.heappush(self._data, value)

    def pop(self):
        """Retire et retourne le plus petit élément"""
        return heapq.heappop(self._data)

    def __repr__(self):
        """Affichage trié"""
        return repr(sorted(self._data))  # Affiche trié, mais stocke en heap

# Exemple d'utilisation :
heap = SortedHeap([5, 2, 8])
print(heap)  # [2, 5, 8]
heap.append(3)
print(heap)  # [2, 3, 5, 8]
heap.append(1)
print(heap.pop())  # 1 (plus petit élément retiré)
print(heap)  # [2, 3, 5, 8]
```

✅ **Avantages** :
- `heapq` est **très performant** pour gérer des éléments triés en temps réel.
- `pop()` est O(log n), plus rapide que `sort()`.

❌ **Inconvénient** :
- **L’ordre interne n’est pas trié** (`heapq` garde juste le plus petit élément accessible).

---

## 🔥 **Quelle solution choisir ?**
| Méthode | Facilité | Performance | Meilleur usage |
|---------|----------|------------|----------------|
| **Tri après chaque ajout (`sort()`)** | ✅ Facile | ❌ O(n log n) | Petites listes |
| **Insertion binaire (`bisect.insort()`)** | ✅ Simple | ✅ O(log n) | Grandes listes |
| **Héritage de `UserList`** | ✅ Plus naturel | ✅ O(log n) | Usage similaire aux listes Python |
| **`heapq` (tas binaire)** | ❌ Pas toujours intuitif | 🔥 O(log n) | File d’attente prioritaire |

Si tu veux **une vraie liste triée**, utilise `bisect.insort()`.  
Si tu veux **toujours récupérer le plus petit élément efficacement**, utilise `heapq`.
