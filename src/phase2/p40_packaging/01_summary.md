**Packager un projet Python** 

## 🧱 1. Structure minimale d’un projet Python packagé

```
mon_projet/
├── src/
│   └── mon_projet/
│       └── __init__.py
├── tests/
│   └── test_mon_projet.py
├── README.md
├── LICENSE
├── pyproject.toml       # Format standard moderne
├── setup.cfg            # Configuration declarative (setuptools)
├── setup.py             # Souvent vide ou minimal aujourd’hui
├── MANIFEST.in          # (optionnel) Pour inclure fichiers non-Python
```

---

## ⚙️ 2. Le `setup.cfg` (setuptools)

`setup.cfg` est un fichier **déclaratif** 
qui remplace progressivement le code Python dans `setup.py`.

### Exemple simple :

```ini
[metadata]
name = mon-projet
version = 0.1.0
description = Mon super projet Python
author = Ton Nom
license = MIT
long_description = file: README.md
long_description_content_type = text/markdown

[options]
packages = find:
package_dir =
    = src
install_requires =
    numpy
    pandas

[options.packages.find]
where = src
```

---

## 📦 3. Le `pyproject.toml` : le nouveau standard

Introduit par [PEP 518](https://peps.python.org/pep-0518/), c’est le **fichier standard** moderne pour configurer tous les outils (build, test, format, etc.).

### Exemple avec `setuptools` :

```toml
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"
```

Ce fichier est **obligatoire** pour certains outils modernes (comme `pip` en mode isolé, `poetry`, `flit`, etc.).

---

## 🛠 4. Alternatives modernes à `setuptools`

### ✅ `flit`
- Léger, simple, rapide.
- Ne supporte que les **packages purs** (pas d’extension C).
- Configuration **uniquement dans `pyproject.toml`**.

```toml
[build-system]
requires = ["flit_core >=3.2,<4"]
build-backend = "flit_core.buildapi"

[project]
name = "mon-projet"
version = "0.1.0"
dependencies = ["numpy", "pandas"]
```

→ Installation : `pip install flit`  
→ Build : `flit build`

---

### ✅ `poetry`
- Gestionnaire complet (dépendances + packaging + virtualenvs)
- Très utilisé dans les projets modernes.
- Tout est dans `pyproject.toml`.

→ Installation : `pip install poetry`  
→ Initialisation : `poetry init`  
→ Build : `poetry build`

---

### ⚠️ `pipenv`
- Combine `Pipfile` + virtualenv.
- Moins orienté packaging, plus pour la gestion d’envs.
- Délaissé par certains au profit de `poetry`.

---

## 📤 5. Construire et publier son paquet

```bash
# Construire
python -m build  # nécessite: pip install build

# Publier sur PyPI
python -m twine upload dist/*
```

---

## 🧪 6. Tests locaux

```bash
pip install -e .  # install en editable mode pour dev
```

---

## 📌 Resumé

| Outil       | Packaging | Dépendances | Virtualenv | Popularité |
|-------------|-----------|-------------|------------|------------|
| setuptools  | ✅        | ❌          | ❌         | ⭐⭐⭐⭐      |
| flit        | ✅        | ⚠️          | ❌         | ⭐⭐⭐       |
| poetry      | ✅        | ✅          | ✅         | ⭐⭐⭐⭐⭐     |
| pipenv      | ❌        | ✅          | ✅         | ⭐⭐        |

---
