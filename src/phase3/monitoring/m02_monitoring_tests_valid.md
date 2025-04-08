Voici une **configuration de base** pour un projet Python avec :

✅ `pytest` pour les tests  
📊 `coverage` pour mesurer la couverture  
📋 `logging` pour surveiller l’exécution du code

---

## 🗂️ **Arborescence recommandée du projet**

```
mon_projet/
│
├── mon_module/
│   ├── __init__.py
│   └── operations.py
│
├── tests/
│   ├── __init__.py
│   └── test_operations.py
│
├── requirements.txt
└── pytest.ini
```

---

## 🧰 **1. Fichier `operations.py` (exemple simple)**

```python
# mon_module/operations.py

import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def add(a, b):
    logger.info(f"Addition de {a} + {b}")
    return a + b

def divide(a, b):
    logger.info(f"Division de {a} / {b}")
    if b == 0:
        logger.error("Division par zéro")
        raise ValueError("Division by zero")
    return a / b
```

---

## 🧪 **2. Test avec `pytest`**

```python
# tests/test_operations.py

from mon_module.operations import add, divide
import pytest

def test_add():
    assert add(2, 3) == 5

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)
```

---

## 📦 **3. Fichier `requirements.txt`**

```
pytest
coverage
```

Installe tout avec :
```bash
pip install -r requirements.txt
```

---

## ⚙️ **4. Fichier `pytest.ini` (facultatif)**

```ini
# pytest.ini
[pytest]
minversion = 6.0
addopts = -ra -q
testpaths = tests
```

---

## 🧪 **5. Lancer les tests et la couverture**

```bash
# Exécute les tests avec pytest
pytest

# Mesure la couverture
coverage run -m pytest

# Affiche le rapport dans le terminal
coverage report -m

# Génère un rapport HTML consultable
coverage html
```

➡️ Un dossier `htmlcov/` est créé, ouvre `htmlcov/index.html` dans ton navigateur.

---

## 📋 **Exemple de log lors du test**

Grâce au `logging`, quand tu lances les tests tu verras :
```
INFO:mon_module.operations:Addition de 2 + 3
INFO:mon_module.operations:Division de 10 / 2
INFO:mon_module.operations:Division de 5 / 0
ERROR:mon_module.operations:Division par zéro
```

---

Souhaites-tu aussi une version avec `pre-commit` pour automatiser les tests et le linting avant chaque commit ?