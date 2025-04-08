# **📌 La Mutabilité en Python : Importance, Types et Transformation 🚀**  

La **mutabilité** est une notion clé en Python qui impacte **les performances, la conception logicielle et la gestion mémoire**. Certains types Python sont **mutables** (modifiable en place) et d’autres **immuables** (impossible à modifier après création).

---

## **🔹 1. Pourquoi la mutabilité est-elle importante ?**
| **Aspect** | **Impact de la mutabilité** |
|-----------|------------------------------|
| **Gestion mémoire** 🏋️ | Les types immuables sont souvent optimisés et réutilisés en mémoire (ex: `str`, `int`). |
| **Performance** 🚀 | Modifier un objet mutable évite la création de nouveaux objets, ce qui peut accélérer l'exécution. |
| **Sécurité** 🔒 | Les objets immuables sont plus sûrs pour la programmation parallèle (évite les modifications concurrentes). |
| **Conception logicielle** 🏗️ | Les objets immuables sont souvent préférés pour les **clés de dictionnaires** ou des structures de données fiables. |

---

## **🔹 2. Quels types sont mutables et immuables ?**
| **Type** | **Mutable ?** | **Exemple** |
|---------|------------|------------|
| `int`, `float`, `bool`, `complex` | ❌ Non mutable | `x = 42` (une nouvelle instance est créée si modifiée) |
| `str` | ❌ Non mutable | `"Hello"[0] = "A"` ❌ (Erreur) |
| `tuple` | ❌ Non mutable | `(1, 2, 3)[0] = 10` ❌ (Erreur) |
| `list` | ✅ Mutable | `l = [1, 2, 3]; l[0] = 10` ✅ |
| `dict` | ✅ Mutable | `d = {"a": 1}; d["a"] = 42` ✅ |
| `set` | ✅ Mutable | `s = {1, 2, 3}; s.add(4)` ✅ |

---

## **🔹 3. Impact de la mutabilité sur les performances**
### **3.1 Les types immuables sont réutilisés en mémoire**
```python
a = "hello"
b = "hello"
print(a is b)  # ✅ True (Réutilisation de l'objet en mémoire)
```
💡 **Optimisation via l’interning** : Python évite de dupliquer certains objets immuables.

---

### **3.2 Les objets mutables créent une référence commune**
```python
list1 = [1, 2, 3]
list2 = list1  # list2 pointe vers le même objet
list2.append(4)
print(list1)  # ✅ [1, 2, 3, 4] (Modifié à travers `list2`)
```
💡 **Piège !** Modifier une variable affecte **toutes les références pointant vers le même objet**.

✅ **Solution : Utiliser `.copy()` ou `deepcopy()` pour créer une nouvelle instance indépendante.**
```python
import copy
list2 = copy.deepcopy(list1)
```

---

## **🔹 4. Rendre une classe immuable en Python**
📌 **Transformer une classe mutable en immuable permet d’éviter des modifications accidentelles**.

### **4.1 Utiliser `@dataclass(frozen=True)`**
```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Aircraft:
    flight_name: str
    capacity: int

plane = Aircraft("AF101", 180)
# plane.capacity = 200  # ❌ AttributeError: can't assign to field
```
✅ **Les objets sont immuables** → Toute tentative de modification déclenche une erreur.

---

### **4.2 Définir `__slots__` et surcharger `__setattr__`**
📌 **Bloque l'ajout ou la modification d'attributs après création**.

```python
class ImmutableAircraft:
    __slots__ = ("flight_name", "capacity")

    def __init__(self, flight_name: str, capacity: int):
        self.flight_name = flight_name
        self.capacity = capacity

    def __setattr__(self, key, value):
        if hasattr(self, key):
            raise AttributeError(f"❌ `{key}` est immuable !")
        super().__setattr__(key, value)

plane = ImmutableAircraft("AF101", 180)
# plane.capacity = 200  # ❌ AttributeError: `capacity` est immuable !
```
✅ **Empêche la modification et la création de nouveaux attributs.**

---

## **🔹 5. Transformer une classe immuable en mutable**
📌 **Si on veut rendre une classe mutable, il faut éviter `frozen=True` et `__setattr__`.**

### **5.1 Convertir `@dataclass(frozen=True)` en `@dataclass` normal**
```python
from dataclasses import dataclass

@dataclass
class Aircraft:
    flight_name: str
    capacity: int

plane = Aircraft("AF101", 180)
plane.capacity = 200  # ✅ Possible car mutable
```

---

### **5.2 Autoriser les modifications d’attributs**
```python
class MutableAircraft:
    def __init__(self, flight_name: str, capacity: int):
        self.flight_name = flight_name
        self.capacity = capacity  # Peut être modifié librement

plane = MutableAircraft("AF101", 180)
plane.capacity = 200  # ✅ Possible
```
✅ **Autorise les modifications** après instanciation.

---

## **🔹 6. Quand utiliser des objets mutables ou immuables ?**
| **Cas** | **Type recommandé** | **Pourquoi ?** |
|---------|----------------|-------------|
| **Stocker des clés dans un `dict`** | `tuple`, `str`, `frozenset` (Immuable) | Les clés de dictionnaire doivent être **hashables**. |
| **Programmer en multithreading** | `tuple`, `frozenset`, `dataclass(frozen=True)` | Évite les **modifications concurrentes**. |
| **Créer des configurations constantes** | `NamedTuple`, `dataclass(frozen=True)` | Empêche **les modifications accidentelles**. |
| **Modifier dynamiquement une structure** | `list`, `dict`, `set` (Mutable) | Permet d'**ajouter, modifier ou supprimer des valeurs**. |

---

## **🔥 Conclusion**
| **Pourquoi la mutabilité est importante ?** ✅ |
|---------------------------------------------|
| **Impacte les performances** : Les objets immuables peuvent être réutilisés en mémoire. |
| **Affecte la sécurité** : Les objets mutables peuvent être modifiés de manière imprévisible. |
| **Améliore la lisibilité et l’optimisation** : `tuple`, `frozenset` sont préférés pour des données fixes. |
| **Essentiel en programmation concurrente** : Les objets immuables évitent les effets de bord. |

**🚀 Maîtriser la mutabilité est essentiel pour écrire un code Python robuste, efficace et sécurisé !** 🔥