
# 🧩 Dossier – Typage fort en Python

---

## 📌 Pourquoi typer son code Python ?

✅ Meilleure lisibilité et compréhension  
✅ Aide à la documentation automatique  
✅ Réduction des bugs  
✅ Support des IDE (complétion, erreurs)  
✅ Validation statique avec des outils comme `mypy`  
✅ Meilleure compatibilité avec les gros projets ou les APIs

---

## 📘 1. `typing` — Le module standard

Python permet d’annoter les types avec la **PEP 484** et les versions suivantes (PEP 585, etc.).

### ✍️ Syntaxes courantes

```python
def greet(name: str) -> str:
    return f"Hello, {name}"

def add(values: list[int]) -> int:
    return sum(values)

from typing import Optional, Union

def parse_number(text: str) -> Optional[float]:
    try:
        return float(text)
    except ValueError:
        return None

def handle(val: Union[int, str]) -> str:
    return str(val)
```

### 📚 Collections et structures avancées

```python
from typing import List, Dict, Tuple, Callable

Vector = List[float]
Config = Dict[str, Union[str, int]]

def operate(v: Vector) -> float:
    return sum(v)
```

### 🧬 Typing générique (paramétrage)

```python
from typing import TypeVar, Generic

T = TypeVar('T')

class Box(Generic[T]):
    def __init__(self, content: T):
        self.content = content
```

---

## 🔍 2. `mypy` — Vérificateur statique

### 📦 Installation
```bash
pip install mypy
```

### ▶️ Utilisation
```bash
mypy script.py
```

### 🧪 Exemple avec erreur
```python
def square(x: int) -> int:
    return x * x

square("3")  # mypy: Argument 1 to "square" has incompatible type "str"
```

### 🔧 Configuration : `mypy.ini` ou `pyproject.toml`
```ini
[mypy]
strict = True
ignore_missing_imports = True
```

---

## 🧠 3. `pydantic` — Typage + Validation des données

Pydantic est une bibliothèque qui combine **typing** et **validation runtime**.

### 📦 Installation
```bash
pip install pydantic
```

### ✅ Exemple basique

```python
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str

user = User(id=1, name="Alice", email="alice@example.com")
```

### ❌ Exemple avec validation

```python
User(id="abc", name="Bob", email="bob@example.com")
# → ValidationError: id is not an integer
```

### 💡 Bonus : validation avancée

```python
from pydantic import Field, EmailStr

class Person(BaseModel):
    name: str = Field(..., min_length=3)
    email: EmailStr
    age: int = Field(..., ge=0, le=130)
```

---

## 🔄 Comparaison

| Outil     | Typage | Vérification statique | Vérification runtime | Utilisation |
|-----------|--------|------------------------|------------------------|-------------|
| `typing`  | ✅     | ❌ (besoin de mypy)    | ❌                    | Standard    |
| `mypy`    | ✅     | ✅                     | ❌                    | Linter      |
| `pydantic`| ✅     | ✅ (optionnel)         | ✅                    | Data models |

---

## 🛠️ Bonnes pratiques

- Toujours typer les **arguments** et **valeurs de retour**.
- Favoriser `Optional[...]` et `Union[...]` aux types permissifs comme `Any`.
- Activer les options strictes de `mypy` pour plus de rigueur.
- Utiliser `pydantic` pour les entrées d’API, fichiers de config ou objets en provenance d’utilisateurs.

---

## 📁 Exemple complet

```python
from pydantic import BaseModel, EmailStr
from typing import Optional, List

class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    age: Optional[int] = None

def send_email(user: User) -> None:
    print(f"Sending email to {user.email}")

users: List[User] = [
    User(id=1, name="Alice", email="alice@example.com"),
    User(id=2, name="Bob", email="bob@example.com", age=30),
]

for u in users:
    send_email(u)
```

---

## 📎 Pour aller plus loin

- [PEP 484 – Type Hints](https://peps.python.org/pep-0484/)
- [mypy cheatsheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)
- [Pydantic v2 docs](https://docs.pydantic.dev/latest/)
- Alternatives : `dataclasses + dacite`, `attrs`
