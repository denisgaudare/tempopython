### ✅ **Implémentation d'une liste triée avec `UserList`**
L'utilisation de `collections.UserList` permet d'hériter du comportement d'une liste standard tout en **ajoutant des contraintes** spécifiques, comme un tri automatique après chaque insertion.
---

### 1️⃣ **Implémentation de base**
On va surcharger `append()` et `extend()` pour s'assurer que les éléments sont toujours triés.

```python
from collections import UserList
import bisect

class SortedList(UserList):
    def append(self, value):
        """Insère un élément à la bonne position automatiquement"""
        bisect.insort(self.data, value)

    def extend(self, iterable):
        """Ajoute plusieurs éléments triés automatiquement"""
        for value in iterable:
            bisect.insort(self.data, value)

# Exemple d'utilisation
slist = SortedList([5, 2, 8])
print(slist)  # [2, 5, 8]
slist.append(3)
print(slist)  # [2, 3, 5, 8]
slist.extend([7, 1, 6])
print(slist)  # [1, 2, 3, 5, 6, 7, 8]
```

✅ **Avantages** :
- Se comporte comme une **liste classique**, donc on peut utiliser `len()`, `[]`, `pop()`, etc.
- Trie automatiquement **sans refaire un tri complet** (`O(log n)` au lieu de `O(n log n)`).

---

### 2️⃣ **Ajout de méthodes supplémentaires**
On peut ajouter des méthodes comme :
- **Suppression d'un élément (`remove()`)**
- **Accès au plus petit élément (`min()`)**
- **Accès au plus grand élément (`max()`)**
- **Récupération et suppression du plus petit (`pop_min()`)**

```python
class SortedList(UserList):
    def append(self, value):
        """Insère un élément à la bonne position automatiquement"""
        bisect.insort(self.data, value)

    def extend(self, iterable):
        """Ajoute plusieurs éléments triés automatiquement"""
        for value in iterable:
            bisect.insort(self.data, value)

    def min(self):
        """Retourne le plus petit élément"""
        if not self.data:
            raise ValueError("Liste vide")
        return self.data[0]

    def max(self):
        """Retourne le plus grand élément"""
        if not self.data:
            raise ValueError("Liste vide")
        return self.data[-1]

    def pop_min(self):
        """Retire et retourne le plus petit élément"""
        if not self.data:
            raise IndexError("Liste vide")
        return self.data.pop(0)

# Exemple d'utilisation
slist = SortedList([5, 2, 8])
print(slist)  # [2, 5, 8]
slist.append(3)
print(slist)  # [2, 3, 5, 8]
print(slist.min())  # 2
print(slist.max())  # 8
print(slist.pop_min())  # 2
print(slist)  # [3, 5, 8]
```

---

### 3️⃣ **Rendre la liste **semi-immutable** (interdire `insert()` et `__setitem__`)**
Si tu veux que les utilisateurs **ne puissent pas insérer aux mauvais endroits** ou modifier un élément directement (ex: `slist[0] = 99`), on peut bloquer ces actions.

```python
class SortedList(UserList):
    def append(self, value):
        bisect.insort(self.data, value)

    def extend(self, iterable):
        for value in iterable:
            bisect.insort(self.data, value)

    def __setitem__(self, index, value):
        """Empêche la modification directe d'un élément"""
        raise TypeError("Modification d'un élément interdit, utilisez append()")

    def insert(self, index, value):
        """Empêche l'insertion à un index arbitraire"""
        raise TypeError("Insertion par index interdit, utilisez append()")

# Exemple
slist = SortedList([3, 1, 4])
print(slist)  # [1, 3, 4]
slist.append(2)
print(slist)  # [1, 2, 3, 4]

# Tentative de modification interdite
slist[0] = 99  # Erreur : TypeError
slist.insert(1, 5)  # Erreur : TypeError
```

---

### 4️⃣ **Comparaison des performances avec `list` classique**
Regardons la performance d’ajout de **10 000 éléments aléatoires** dans une `SortedList` et une `list` classique.

```python
import random
import time

# Test avec SortedList
slist = SortedList()
start = time.time()
for _ in range(10000):
    slist.append(random.randint(0, 100000))
end = time.time()
print(f"Temps avec SortedList : {end - start:.5f} secondes")

# Test avec list classique + sort()
lst = []
start = time.time()
for _ in range(10000):
    lst.append(random.randint(0, 100000))
lst.sort()  # Tri après ajout
end = time.time()
print(f"Temps avec list + sort() : {end - start:.5f} secondes")
```

🔍 **Résultats typiques :**
- `SortedList` (avec `bisect.insort()`) est souvent **plus rapide** que `list` + `sort()`, car elle insère les éléments directement **au bon endroit** (`O(log n)`).
- Pour **petites listes**, la différence est négligeable.
- Pour **grandes listes**, `SortedList` est beaucoup plus efficace.

---

## 🎯 **Conclusion**
| Méthode | Facilité | Performance | Meilleur usage |
|---------|----------|------------|----------------|
| **`list` + `sort()`** | ✅ Très simple | ❌ `O(n log n)` après chaque ajout | Si on trie rarement |
| **`bisect.insort()` (`SortedList`)** | ✅ Facile | ✅ `O(log n)` pour chaque ajout | Quand on ajoute souvent |
| **`heapq` (tas binaire)** | ❌ Moins lisible | 🔥 `O(log n)` | Si on veut récupérer le plus petit élément rapidement |

🔥 **Si tu veux une liste triée automatiquement, 
`SortedList` avec `UserList` et `bisect.insort()` 
est la meilleure approche !**