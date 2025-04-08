**Packaging Python** utilisant plusieurs outils populaires : `setuptools`, `setup.cfg`, `pyproject.toml`, et `poetry`, accompagné d’une **comparaison** de ces outils.

---

## 📦 Objectif du projet : `mypkg`

Un petit package Python nommé `mypkg` avec un module simple et un point d'entrée CLI.

Structure :

```
mypkg/
├── mypkg/
│   └── __init__.py
│   └── cli.py
├── tests/
│   └── test_cli.py
├── README.md
├── LICENSE
├── setup.py         (optionnel)
├── setup.cfg        (setuptools config)
├── pyproject.toml   (standard modern)
├── poetry.lock      (si poetry)
└── MANIFEST.in
```

---

## 🧪 Contenu minimal du package

### `mypkg/__init__.py`

```python
__version__ = "0.1.0"
```

### `mypkg/cli.py`

```python
def main():
    print("Hello from mypkg!")
```

### `tests/test_cli.py`

```python
from mypkg.cli import main

def test_main(capfd):
    main()
    out, _ = capfd.readouterr()
    assert "Hello from mypkg" in out
```

---

## ⚙️ 1. Avec `setuptools` (ancienne méthode avec `setup.py`)

### `setup.py`

```python
from setuptools import setup, find_packages

setup(
    name="mypkg",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": ["mypkg=mypkg.cli:main"]
    },
)
```

Commande :
```bash
python setup.py sdist bdist_wheel
```

---

## ⚙️ 2. Avec `setup.cfg` (configuration déclarative)

### `setup.cfg`

```ini
[metadata]
name = mypkg
version = 0.1.0
description = A simple CLI package
author = Your Name

[options]
packages = find:
install_requires =

[options.entry_points]
console_scripts =
    mypkg = mypkg.cli:main
```

### `setup.py` (optionnel mais recommandé pour compatibilité)

```python
from setuptools import setup
setup()
```

---

## ⚙️ 3. Avec `pyproject.toml` (standard PEP 518/PEP 621)

### `pyproject.toml` (avec `setuptools`)

```toml
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "mypkg"
version = "0.1.0"
description = "A simple CLI package"
authors = [{ name = "Your Name", email = "you@example.com" }]
dependencies = []

[project.scripts]
mypkg = "mypkg.cli:main"
```

Commande :
```bash
pip install build
python -m build
```

---

## ⚙️ 4. Avec `Poetry`

```bash
poetry init
# ou directement :
poetry new mypkg
```

### `pyproject.toml` (généré par poetry)

```toml
[tool.poetry]
name = "mypkg"
version = "0.1.0"
description = "A simple CLI package"
authors = ["Your Name <you@example.com>"]

[tool.poetry.dependencies]
python = "^3.8"

[tool.poetry.scripts]
mypkg = "mypkg.cli:main"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

Commandes :

```bash
poetry install
poetry build
poetry publish
```

---

## 📊 Comparaison des outils de packaging

| Critère                  | `setuptools + setup.py`         | `setup.cfg`                   | `pyproject.toml` (PEP 621)      | `Poetry`                            |
|--------------------------|----------------------------------|-------------------------------|----------------------------------|--------------------------------------|
| **Modernité**            | Ancien, toujours supporté        | Moderne, déclaratif           | Moderne (standard PEP)           | Très moderne, opinionné              |
| **Simplicité**           | Très simple, script Python       | Plus propre que `setup.py`    | Lisible, modulaire               | Très lisible mais structuré          |
| **Gestion des deps**     | Manuel ou avec pip               | Manuel                        | Possible avec `requirements.txt` | Géré automatiquement (`poetry.lock`) |
| **Scripts CLI**          | Via `entry_points`               | Idem                          | Idem                             | Plus simple avec `[tool.poetry.scripts]` |
| **Isolation d’environnement** | Externe (`virtualenv`, `venv`) | Idem                          | Idem                             | Intégré (`poetry shell`, `poetry env`) |
| **Popularité**           | Très utilisée, standard historique | Adoptée de plus en plus       | Recommandée officiellement       | En croissance rapide                 |
| **Interopérabilité**     | Moyenne                          | Bonne                         | Excellente (standard)            | Moyenne (poetry-centric)             |
| **Courbe d’apprentissage** | Facile                         | Facile                        | Moyenne                          | Légèrement plus complexe             |

---

## 🧰 Autres outils possibles

- **Flit** : Packaging minimaliste avec `pyproject.toml` uniquement.
- **Hatch** : Moderne, orienté projets complexes.
- **PDM** : Gestionnaire moderne basé sur `pyproject.toml`.

---
