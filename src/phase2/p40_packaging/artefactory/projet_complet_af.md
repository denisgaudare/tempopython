# Exemple complet Artefactory

---

## ✅ Exemple avec `setuptools`

### `setup.py`

```python
from setuptools import setup, find_packages

setup(
    name="hello_pkg",
    version="0.1.0",
    description="Un exemple simple de package Python",
    author="Ton Nom",
    packages=find_packages(),
    install_requires=[],
    python_requires=">=3.7",
)
```

### `pyproject.toml` (nécessaire pour `build`)

```toml
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"
```

### `~/.pypirc`

```ini
[distutils]
index-servers =
    artifactory

[artifactory]
repository = https://your-company.jfrog.io/artifactory/api/pypi/python-local/
username = TON_UTILISATEUR
password = TON_MOT_DE_PASSE_OU_TOKEN
```

### Commandes à exécuter

```bash
python -m build
twine upload -r artifactory dist/*
```

---

## ✅ Exemple avec `poetry`

### `pyproject.toml`

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

[[tool.poetry.source]]
name = "artifactory"
url = "https://your-company.jfrog.io/artifactory/api/pypi/python-local/"
```

### Authentification (à faire une seule fois)

```bash
poetry config http-basic.artifactory TON_UTILISATEUR TON_MOT_DE_PASSE_OU_TOKEN
```

### Commandes

```bash
poetry build
poetry publish --repository artifactory
```

---

## ✅ Structure du projet

```
hello_pkg/
├── hello_pkg/
│   └── __init__.py       # Contient say_hello()
├── pyproject.toml
├── setup.py              # (si setuptools)
├── dist/                 # Créé après build
```

---

## 📌 Bonus : `hello_pkg/__init__.py`

```python
def say_hello(name: str) -> str:
    return f"Hello, {name}!"
```
