# ✅ Libs externes vs standard en Python

## Sélection de **librairies externes** 
## améliorant les **librairies standard** de Python, classées par thème.

## 📁 1. Fichiers & chemins

- **Standard** : `os`, `pathlib`
- **Externe** : [`pyfilesystem2`](https://www.pyfilesystem.org/)

**✅ Avantage** : abstraction du système de fichiers (ZIP, FTP, cloud…)

```python
from fs import open_fs

fs = open_fs('mem://')
fs.writetext('hello.txt', 'Bonjour !')
print(fs.readtext('hello.txt'))  # → Bonjour !
```

---

## 🌐 2. Requêtes HTTP

- **Standard** : `urllib.request`
- **Externe** : [`requests`](https://docs.python-requests.org/)

**✅ Avantage** : API simple, support complet HTTP/HTTPS, gestion des erreurs

```python
import requests

resp = requests.get('https://api.github.com')
print(resp.status_code, resp.json())
```

## 📄 3. JSON & données

- **Standard** : `json`, `csv`, `configparser`
- **Externe** : [`pydantic`](https://docs.pydantic.dev/), [`ruamel.yaml`](https://pypi.org/project/ruamel.yaml/)

**✅ Avantage** : validation automatique, typage strict, conversions implicites

```python
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str

u = User(id='42', name='Alice')  # Conversion auto str → int
print(u.dict())  # {'id': 42, 'name': 'Alice'}
```

---

## 📊 4. Maths, calcul, statistiques

- **Standard** : `math`, `statistics`
- **Externe** : [`numpy`](https://numpy.org/), [`scipy`](https://scipy.org/)

**✅ Avantage** : calcul vectoriel performant, matrices, fonctions mathématiques avancées

```python
import numpy as np

a = np.array([1, 2, 3])
print(a * 10)  # [10 20 30]
```

---

## 📚 5. Structures de données avancées

- **Standard** : `collections`, `heapq`
- **Externe** : [`sortedcontainers`](https://github.com/grantjenks/python-sortedcontainers)

**✅ Avantage** : listes triées avec insertion rapide

```python
from sortedcontainers import SortedList

s = SortedList([5, 1, 3])
s.add(2)
print(s)  # SortedList([1, 2, 3, 5])
```

---

## 🧪 6. Tests

- **Standard** : `unittest`
- **Externe** : [`pytest`](https://docs.pytest.org/)

**✅ Avantage** : syntaxe plus naturelle, fixtures puissantes, écosystème riche

```python
def inc(x): return x + 1

def test_inc():
    assert inc(3) == 4
```

---

## ⏱ 7. Concurrence & async

- **Standard** : `threading`, `asyncio`
- **Externe** : [`trio`](https://trio.readthedocs.io/), [`anyio`](https://anyio.readthedocs.io/)

**✅ Avantage** : modèle de concurrence plus sûr et ergonomique

```python
import trio

async def hello():
    print("Hello...")
    await trio.sleep(1)
    print("...world!")

trio.run(hello)
```

---

## 🧰 8. Scripts & CLI

- **Standard** : `argparse`
- **Externe** : [`typer`](https://typer.tiangolo.com/) (ou [`click`](https://click.palletsprojects.com/))

**✅ Avantage** : génération automatique de CLI à partir de fonctions typées

```python
import typer

def hello(name: str):
    print(f"Hello {name}!")

typer.run(hello)
```

---

## 🎨 9. Interface graphique (GUI)

- **Standard** : `tkinter`
- **Externe** : [`PySide6`](https://doc.qt.io/qtforpython/), [`DearPyGui`](https://github.com/hoffstadt/DearPyGui)

**✅ Avantage** : interface moderne, multiplateforme, plus puissante

```python
from PySide6.QtWidgets import QApplication, QLabel

app = QApplication([])
label = QLabel("Hello Qt!")
label.show()
app.exec()
```

---

## 📦 10. Sérialisation

- **Standard** : `pickle`
- **Externe** : [`dill`](https://pypi.org/project/dill/), [`joblib`](https://joblib.readthedocs.io/)

**✅ Avantage** : supporte la sérialisation de fonctions, lambdas, objets plus complexes

```python
import dill

def square(x): return x * x

with open('func.pkl', 'wb') as f:
    dill.dump(square, f)
```

---
