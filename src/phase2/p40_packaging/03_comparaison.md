# Packaging 
## 📁 Arborescence commune du projet

```bash
hello_pkg/
├── hello_pkg/
│   └── __init__.py  # Contient la fonction
├── tests/
│   └── test_hello.py
├── README.md
├── requirements.txt
├── setup.py               # (1) setuptools classique
├── setup.cfg              # (optionnel pour setuptools)
├── pyproject.toml         # (2) nécessaire pour PEP 517/518
├── poetry.lock            # (3) généré par Poetry
```

---

## 📄 Fichier `hello_pkg/__init__.py`

```python
def say_hello(name: str) -> str:
    return f"Hello, {name}!"
```

---

## 📁 1. Packaging avec `setuptools` classique (avec `setup.py`)

### `setup.py`
```python
from setuptools import setup, find_packages

setup(
    name="hello_pkg",
    version="0.1.0",
    author="Ton Nom",
    description="Un exemple simple de package Python",
    packages=find_packages(),
    install_requires=[],
    python_requires=">=3.7",
)
```

Tu peux maintenant installer le package localement :

```bash
pip install .
```

---

## 📁 2. Packaging moderne avec `pyproject.toml` + `setuptools`

### `pyproject.toml`
```toml
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "hello_pkg"
version = "0.1.0"
description = "Un exemple simple de package Python"
authors = [
    { name="Ton Nom", email="ton.email@example.com" }
]
readme = "README.md"
requires-python = ">=3.7"
dependencies = []

[tool.setuptools.packages.find]
where = ["."]
```

### (Optionnel) `setup.cfg` (si tu veux tout passer dans le TOML, tu peux ignorer)

Puis :

```bash
pip install .
```

ou avec isolation :

```bash
python -m build
```

---

## 📁 3. Packaging avec `poetry`

### Commandes d'initialisation :
```bash
poetry init  # ou poetry new hello_pkg
```

### `pyproject.toml` généré par Poetry :
```toml
[tool.poetry]
name = "hello_pkg"
version = "0.1.0"
description = "Un exemple simple de package Python"
authors = ["Ton Nom <ton.email@example.com>"]
packages = [{ include = "hello_pkg" }]

[tool.poetry.dependencies]
python = ">=3.7"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

### Utilisation avec Poetry :
```bash
poetry install
poetry build
```

---

## ✅ Résumé

| Méthode           | Fichiers clés                      | Avantages                              |
|-------------------|------------------------------------|----------------------------------------|
| setuptools        | `setup.py`                         | Classique, compatible partout          |
| setuptools + toml | `pyproject.toml` + `setup.cfg`     | Moderne, standard PEP 517/518          |
| poetry            | `pyproject.toml` + `poetry.lock`   | Gestionnaire complet + simplicité      |
