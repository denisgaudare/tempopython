Parfait ! Voici un **exemple complet de projet Python packagé avec `poetry`**, pas à pas, avec un fichier source, une structure claire, et une configuration via `pyproject.toml`.

---

## 🎯 Objectif

Créer un projet Python nommé `mon_projet` avec une fonction simple et un test, tout en utilisant `poetry` pour la gestion du packaging et des dépendances.

---

## 🧱 1. Structure du projet

```
mon_projet/
├── mon_projet/
│   └── __init__.py
├── tests/
│   └── test_main.py
├── README.md
├── pyproject.toml       # Géré par poetry
```

---

## 🚀 2. Initialisation avec `poetry`

```bash
mkdir mon_projet
cd mon_projet
poetry init --name mon_projet --author "Ton Nom" --license MIT --python ">=3.9" --dependency pytest
```

> Accepte les options proposées, ou édite le fichier manuellement ensuite.

---

## 🧑‍💻 3. Code source

**`mon_projet/__init__.py`**

```python
def bonjour(nom: str) -> str:
    return f"Bonjour, {nom} !"
```

---

## 🧪 4. Fichier de test

**`tests/test_main.py`**

```python
from mon_projet import bonjour

def test_bonjour():
    assert bonjour("Alice") == "Bonjour, Alice !"
```

---

## 📝 5. Fichier `pyproject.toml` généré

Poetry a généré ceci (extrait pertinent) :

```toml
[tool.poetry]
name = "mon_projet"
version = "0.1.0"
description = ""
authors = ["Ton Nom"]
license = "MIT"
readme = "README.md"
packages = [{ include = "mon_projet" }]

[tool.poetry.dependencies]
python = ">=3.9"

[tool.poetry.dev-dependencies]
pytest = "^8.0"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

---

## 📦 6. Installation pour dev et tests

```bash
poetry install        # installe les dépendances
poetry shell          # active l'environnement virtuel
pytest                # exécute les tests
```

---

## 📤 7. Build et publication

```bash
poetry build          # crée dist/ avec .tar.gz et .whl
poetry publish        # publie sur PyPI (si configuré)
```

Pour publier :
```bash
poetry config pypi-token.pypi ton_token
poetry publish --build
```

---
