La **mutabilité** est un concept fondamental en programmation, notamment en Python. Un objet est dit **mutable** s'il peut être modifié après sa création, et **immuable** s'il ne peut pas être modifié après sa création.

---

## 1. Mutabilité en Python : Types standards
En Python, certains types de données sont **mutables**, et d'autres sont **immuables** par défaut.

### Types **immuables** :
Ces objets ne peuvent pas être modifiés après leur création :
- `int`
- `float`
- `bool`
- `str`
- `tuple`
- `frozenset`
- `bytes`

#### Exemple :
```python
a = "hello"
a[0] = "H"  # Erreur, car les chaînes de caractères sont immuables
```

### Types **mutables** :
Ces objets peuvent être modifiés après leur création :
- `list`
- `dict`
- `set`
- `bytearray`

#### Exemple :
```python
lst = [1, 2, 3]
lst[0] = 99  # Modifie la liste
print(lst)  # [99, 2, 3]
```

---

## 2. Implémentation standard de la mutabilité en Python
Python implémente la mutabilité via la gestion des **références mémoire**.

- Un objet **immuable** a une valeur fixe en mémoire. Toute modification crée un nouvel objet.
- Un objet **mutable** permet de modifier son contenu sans changer sa référence mémoire.

#### Exemple de comportement :
```python
x = "hello"
y = x  # y référence la même chaîne de caractères
x += " world"  # x change de référence mémoire
print(x)  # "hello world"
print(y)  # "hello"

lst1 = [1, 2, 3]
lst2 = lst1  # lst2 référence la même liste
lst1.append(4)  # Modifie la liste en place
print(lst1)  # [1, 2, 3, 4]
print(lst2)  # [1, 2, 3, 4]  (lst2 est aussi modifié)
```

---

## 3. Rendre une classe **immuable**
Une classe peut être rendue **immuable** en :
1. Empêchant la modification des attributs après l'initialisation (`__setattr__`)
2. Utilisant `@property` pour exposer les valeurs sans possibilité de modification
3. Convertissant les attributs en types immuables (`tuple` au lieu de `list`, `frozenset` au lieu de `set`)

#### Exemple 1 : Bloquer les modifications avec `__setattr__`
```python
class ImmutableClass:
    def __init__(self, value):
        self.__dict__["value"] = value  # Initialisation permise
    
    def __setattr__(self, key, value):
        raise AttributeError("Impossible de modifier un attribut après la création")

obj = ImmutableClass(10)
print(obj.value)  # 10
obj.value = 20  # Erreur : Impossible de modifier
```

#### Exemple 2 : Utilisation de `@property`
```python
class ImmutableClass:
    def __init__(self, value):
        self._value = value  # Stockage interne
    
    @property
    def value(self):
        return self._value  # Lecture permise, mais pas d'écriture

obj = ImmutableClass(100)
print(obj.value)  # 100
obj.value = 200  # Erreur
```

#### Exemple 3 : Rendre une liste immuable avec `tuple`
```python
class ImmutableList:
    def __init__(self, items):
        self._items = tuple(items)  # Convertir la liste en tuple (immuable)

    @property
    def items(self):
        return self._items  # Fournir un accès en lecture

obj = ImmutableList([1, 2, 3])
print(obj.items)  # (1, 2, 3)
obj.items.append(4)  # Erreur : tuple immuable
```

---

## 4. Rendre une classe **mutable**
Une classe est **mutable** par défaut en Python, mais on peut la rendre plus flexible en autorisant la modification des attributs.

#### Exemple 1 : Classe mutable simple
```python
class MutableClass:
    def __init__(self, value):
        self.value = value  # L'attribut peut être modifié librement

obj = MutableClass(42)
print(obj.value)  # 42
obj.value = 100  # Modification autorisée
print(obj.value)  # 100
```

#### Exemple 2 : Liste mutable dans une classe
```python
class MutableList:
    def __init__(self, items):
        self.items = items  # Liste mutable

obj = MutableList([1, 2, 3])
obj.items.append(4)  # Modification autorisée
print(obj.items)  # [1, 2, 3, 4]
```

#### Exemple 3 : Ajouter des **méthodes de modification**
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def birthday(self):
        self.age += 1  # Modification autorisée

p = Person("Alice", 30)
p.birthday()
print(p.age)  # 31
```

---

## 5. Protéger une classe **semi-mutable**
Si on veut autoriser certaines modifications mais empêcher d'autres, on peut combiner les approches :

- **Autoriser certaines mises à jour**
- **Empêcher d’ajouter de nouveaux attributs** (`__slots__`)
- **Utiliser des méthodes dédiées pour modifier l’objet**

#### Exemple 1 : `__slots__` pour limiter les attributs modifiables
```python
class Restricted:
    __slots__ = ("name", "age")  # Seuls ces attributs sont autorisés

    def __init__(self, name, age):
        self.name = name
        self.age = age

obj = Restricted("Bob", 25)
obj.age = 26  # Modification permise
obj.address = "Paris"  # Erreur : Attribut non autorisé
```

#### Exemple 2 : Autoriser uniquement certaines modifications avec une méthode
```python
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age  # Protéger les attributs

    @property
    def name(self):
        return self._name  # Lecture seule

    @property
    def age(self):
        return self._age  # Lecture seule

    def set_age(self, new_age):
        if new_age > self._age:  # Contrôle d'accès
            self._age = new_age
        else:
            raise ValueError("Impossible de rajeunir !")

p = Person("Alice", 30)
p.set_age(31)  # OK
print(p.age)  # 31
p.set_age(29)  # Erreur
```

---

## Conclusion
- **Par défaut, Python rend les objets mutables (list, dict, set, etc.)**.
- **Certains types natifs sont immuables (`tuple`, `str`, `int`, etc.)**.
- **On peut rendre une classe immuable** en bloquant `__setattr__`, en utilisant `@property` ou en stockant des objets immuables.
- **On peut rendre une classe semi-mutable** en limitant la modification à des méthodes spécifiques ou en utilisant `__slots__`.

Avec ces approches, tu peux contrôler précisément le comportement de tes objets !