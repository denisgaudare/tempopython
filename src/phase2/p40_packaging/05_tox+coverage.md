Super ! Voici un **mini projet Python complet** avec :

- `poetry` pour la gestion de projet & des dépendances  
- `pytest` pour les tests  
- `coverage` pour la couverture de code  

Tu pourras copier-coller ou cloner cette structure pour démarrer rapidement.

---

## 📁 Arborescence du projet

```
mon_mini_projet/
├── mon_mini_projet/
│   └── operations.py
├── tests/
│   └── test_operations.py
├── README.md
├── pyproject.toml
```

---

## 🧱 Étape 1 : Création du projet avec `poetry`

```bash
poetry new mon_mini_projet
cd mon_mini_projet
```

> Ça crée déjà la structure de base avec `tests/`, un fichier source, et `pyproject.toml`.

---

## 🧠 Étape 2 : Ajouter du code

### 🔧 `mon_mini_projet/operations.py`

```python
def addition(a: int, b: int) -> int:
    return a + b

def soustraction(a: int, b: int) -> int:
    return a - b
```

---

## 🧪 Étape 3 : Ajouter un test

### 📄 `tests/test_operations.py`

```python
from mon_mini_projet.operations import addition, soustraction

def test_addition():
    assert addition(2, 3) == 5

def test_soustraction():
    assert soustraction(5, 3) == 2
```

---

## ⚙️ Étape 4 : Ajouter `pytest` et `coverage`

```bash
poetry add --group dev pytest coverage
```

---

## ✅ Étape 5 : Exécuter les tests et la couverture

```bash
# Lancer les tests
poetry run pytest

# Lancer coverage
poetry run coverage run -m pytest

# Rapport terminal
poetry run coverage report

# Rapport HTML
poetry run coverage html
```

→ Ouvre ensuite `htmlcov/index.html` pour voir les fichiers et les lignes couvertes.

---

## 📝 Fichier `pyproject.toml` (résumé important)

```toml
[tool.poetry]
name = "mon-mini-projet"
version = "0.1.0"
description = "Petit projet avec poetry, pytest et coverage"
authors = ["Ton Nom"]

[tool.poetry.dependencies]
python = "^3.9"

[tool.poetry.dev-dependencies]
pytest = "^8.0"
coverage = "^7.4"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

---

## ➕ Bonus : Makefile (facultatif)

Si tu veux simplifier :

```makefile
test:
	poetry run pytest

coverage:
	poetry run coverage run -m pytest
	poetry run coverage report
	poetry run coverage html
```

---
