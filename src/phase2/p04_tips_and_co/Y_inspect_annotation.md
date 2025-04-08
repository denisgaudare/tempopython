Une **annotation en Python** est une **métadonnée associée à une variable, une fonction ou un paramètre**, souvent utilisée pour indiquer des **types**, mais qui peut en réalité contenir **n'importe quelle expression valide**.

### 🔹 Les annotations de fonction

Voici un exemple typique :

```python
def greet(name: str) -> str:
    return f"Hello, {name}"
```

- `name: str` → indique que `name` est censé être une chaîne de caractères
- `-> str` → indique que la fonction retourne une chaîne de caractères

⚠️ Les annotations **ne sont pas appliquées automatiquement** ! Elles sont **indicatives** et souvent utilisées par :
- les **outils de vérification statique** (ex: MyPy, Pyright),
- les **IDE** (auto-complétion, linting),
- des **librairies** comme `pydantic`, `fastapi`, etc.

---

### 🔹 Annotations de variables

```python
age: int = 30
name: str
```

- Ici aussi, c’est purement informatif : Python n’impose pas de contrainte.
- Tu peux même écrire :

```python
def f(x: "je suis un commentaire") -> "moi aussi":
    pass
```

---

### 🔹 Accès aux annotations

Tu peux récupérer les annotations d’une fonction via l’attribut `__annotations__` :

```python
def add(x: int, y: int) -> int:
    return x + y

print(add.__annotations__)
# {'x': <class 'int'>, 'y': <class 'int'>, 'return': <class 'int'>}
```

---

### 🔹 Exemple avec des types plus avancés

```python
from typing import List, Optional, Union

def process(items: List[int], flag: Optional[bool]) -> Union[int, None]:
    ...
```

---

### ✅ En résumé

| Élément           | Annotation         | Utilisation typique         |
|------------------|--------------------|-----------------------------|
| Paramètres        | `x: int`           | Documentation / type hinting |
| Valeur de retour  | `-> str`           | Documentation / outils type |
| Variable          | `x: float = 3.14`  | Aide IDE / outil statique    |
| Attribut classe   | `self.name: str`   | Typage structuré (dataclass) |


```
import contextlib
import inspect


@contextlib.contextmanager
def atest(a:int) -> str
    pass

print(inspect.get_annotations(atest))
```