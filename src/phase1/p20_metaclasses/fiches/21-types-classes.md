En Python, le typage est dynamique mais peut être précisé à l'aide des **annotations de type** (introduites avec PEP 484). Quant aux classes, elles sont à la base de la programmation orientée objet (POO) en Python.

Voici un tour d'horizon du typage et des classes avec des exemples de code.

---

## 1. **Le Typage en Python**
Python est **dynamique** (on ne déclare pas les types explicitement), mais on peut **indiquer** les types avec des annotations pour améliorer la lisibilité et l'utilisation d'outils comme `mypy`.

### a) Annotations de type de base
```python
def addition(a: int, b: int) -> int:
    return a + b

print(addition(3, 5))  # 8
```

### b) Typage des listes et dictionnaires (avec `list`, `dict`)
```python
from typing import List, Dict

def somme(liste: List[int]) -> int:
    return sum(liste)

nombres: List[int] = [1, 2, 3, 4]
print(somme(nombres))  # 10

def mapping_noms_ages() -> Dict[str, int]:
    return {"Alice": 30, "Bob": 25}

print(mapping_noms_ages())  # {'Alice': 30, 'Bob': 25}
```

### c) `Union` et `Optional` (pour plusieurs types possibles)
```python
from typing import Union, Optional

def double(valeur: Union[int, float]) -> float:
    return valeur * 2

print(double(10))    # 20
print(double(10.5))  # 21.0

def message(nom: Optional[str] = None) -> str:
    return f"Bonjour {nom}" if nom else "Bonjour inconnu"

print(message())         # Bonjour inconnu
print(message("Alice"))  # Bonjour Alice
```

---

## 2. **Les Classes en Python**
Une classe permet de structurer des données et des comportements associés.

### a) Définition et instanciation
```python
class Personne:
    def __init__(self, nom: str, age: int):
        self.nom = nom
        self.age = age

    def se_presenter(self) -> str:
        return f"Je m'appelle {self.nom} et j'ai {self.age} ans."

# Instanciation
p1 = Personne("Alice", 30)
print(p1.se_presenter())  # Je m'appelle Alice et j'ai 30 ans.
```

### b) Typage des attributs avec `dataclasses`
Les **dataclasses** facilitent la création de classes avec des attributs typés.

```python
from dataclasses import dataclass

@dataclass
class Personne:
    nom: str
    age: int

p2 = Personne("Bob", 25)
print(p2)  # Personne(nom='Bob', age=25)
```

### c) Héritage et polymorphisme
```python
class Employe(Personne):
    def __init__(self, nom: str, age: int, salaire: float):
        super().__init__(nom, age)
        self.salaire = salaire

    def se_presenter(self) -> str:
        return f"{super().se_presenter()} Je gagne {self.salaire}€."

e1 = Employe("Charlie", 40, 50000)
print(e1.se_presenter())  # Je m'appelle Charlie et j'ai 40 ans. Je gagne 50000€.
```

### d) Classes Abstraites
```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def crier(self) -> str:
        pass

class Chien(Animal):
    def crier(self) -> str:
        return "Woof!"

c = Chien()
print(c.crier())  # Woof!
```

---

## 3. **Typing Avancé avec `Protocol`**
Avec `Protocol`, on peut définir des interfaces (similaire aux interfaces en Java).

```python
from typing import Protocol

class Criant(Protocol):
    def crier(self) -> str: pass

class Chat:
    def crier(self) -> str:
        return "Miaou!"

def faire_crier(animal: Criant) -> str:
    return animal.crier()

chat = Chat()
print(faire_crier(chat))  # Miaou!
```

---

## 4. **Utilisation de `TypedDict` (dictionnaires typés)**
```python
from typing import TypedDict

class PersonneDict(TypedDict):
    nom: str
    age: int

p: PersonneDict = {"nom": "Alice", "age": 30}
print(p["nom"])  # Alice
```

---

### **Conclusion**
- Python reste dynamique, mais le **typage statique avec annotations** améliore la lisibilité et permet des vérifications (`mypy`).
- Les **classes** sont essentielles en POO, et `dataclasses` simplifie leur utilisation.
- Les **protocoles et types avancés** (`Union`, `TypedDict`, `Protocol`) permettent de structurer du code robuste.

👉 Pour un projet sérieux, utiliser **mypy** :
```sh
pip install mypy
mypy mon_fichier.py
```



