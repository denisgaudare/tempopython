
# ✍️ Exercices : Typage fort en Python

## 🧪 Exercice 1 — Typing de base

Ajoute les annotations de types à cette fonction :

```python
def format_name(first, last):
    return f"{last.upper()}, {first.capitalize()}"
```

---

## 🧪 Exercice 2 — Collections typées

Typage correct des paramètres et du retour :

```python
def total_price(items):
    return sum(items)
```
🧠 *`items` est une liste de `float` ou `int`.*

---

## 🧪 Exercice 3 — Optionnel & Union

Complète le typage :

```python
def parse_input(value):
    if value is None:
        return 0
    if isinstance(value, str):
        return int(value)
    return value
```

---

## 🧪 Exercice 4 — Génériques

Ajoute les types à cette classe :

```python
class Container:
    def __init__(self, content):
        self.content = content

    def get(self):
        return self.content
```

---

## 🧪 Exercice 5 — `pydantic` simple

Complète ce modèle :

```python
from pydantic import BaseModel

class Product(BaseModel):
    name: ...
    price: ...
    available: ...
```

Puis instancie un produit avec :

```python
Product(name="Keyboard", price=59.9, available=True)
```

---

## ✅ Corrigés

---

### ✅ Corrigé 1

```python
def format_name(first: str, last: str) -> str:
    return f"{last.upper()}, {first.capitalize()}"
```

---

### ✅ Corrigé 2

```python
from typing import List

def total_price(items: List[float]) -> float:
    return sum(items)
```

---

### ✅ Corrigé 3

```python
from typing import Union, Optional

def parse_input(value: Optional[Union[str, int]]) -> int:
    if value is None:
        return 0
    if isinstance(value, str):
        return int(value)
    return value
```

---

### ✅ Corrigé 4

```python
from typing import TypeVar, Generic

T = TypeVar('T')

class Container(Generic[T]):
    def __init__(self, content: T):
        self.content = content

    def get(self) -> T:
        return self.content
```

---

### ✅ Corrigé 5

```python
from pydantic import BaseModel

class Product(BaseModel):
    name: str
    price: float
    available: bool

product = Product(name="Keyboard", price=59.9, available=True)
```
