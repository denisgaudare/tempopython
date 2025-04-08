Très bonne question ! Voici un panorama clair des **outils disponibles pour les tests unitaires** en Python — aussi bien ceux **intégrés à la stdlib** que les **librairies externes** populaires.

---

## 🧪 1. Outils de test unitaire **intégrés** à Python

### ✅ `unittest`
- Inclus dans la standard library.
- Inspiré de JUnit (Java).
- Style orienté objet avec des classes de tests.

```python
import unittest

class TestMath(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(1 + 1, 2)
```

→ Exécution :
```bash
python -m unittest discover
```

---

## 🚀 2. Librairies de test **externes** (plus modernes et puissantes)

### 🔥 `pytest` (le plus utilisé)
- Ultra flexible.
- Détection automatique des tests.
- Fixtures puissantes.
- Syntaxe naturelle (pas besoin d’hériter de classes).

```python
def test_addition():
    assert 1 + 1 == 2
```

→ Exécution :
```bash
pytest
```

**Bonus** : très riche écosystème de plugins (coverage, mocks, reporting, async tests…).

---

### 🧰 `hypothesis`
- Pour les **tests basés sur la propriété** (fuzz testing).
- Génère automatiquement des cas de test valides (ex. : chaînes, entiers, etc.).

```python
from hypothesis import given
import hypothesis.strategies as st

@given(st.integers(), st.integers())
def test_addition_commutative(a, b):
    assert a + b == b + a
```

---

### 🪄 `tox`
- Automatisation des tests dans plusieurs versions de Python / environnements virtuels.
- Utile pour valider la compatibilité d’un package.

```ini
# tox.ini
[tox]
envlist = py39, py310

[testenv]
deps = pytest
commands = pytest
```

→ Exécution :
```bash
tox
```

---

### 🧪 `coverage`
- Mesure la **couverture de code**.
- S’intègre bien avec `pytest`.

```bash
coverage run -m pytest
coverage report
coverage html  # Génère un rapport HTML
```

---

## 🧰 3. Pour les mocks et patchs

### 🔁 `unittest.mock` (standard library)
- Pour simuler des objets externes (ex. appels réseau, fichiers, DB).

```python
from unittest.mock import Mock

def salut(service):
    return service.get_name()

def test_salut():
    mock = Mock()
    mock.get_name.return_value = "Alice"
    assert salut(mock) == "Alice"
```

### 🔁 `pytest-mock` (plugin pour pytest)
- Fournit un fixture `mocker` pratique :

```python
def test_patch(mocker):
    fake = mocker.patch("module.externe.fonction", return_value=42)
    assert fake() == 42
```

---

## 🧑‍🔧 4. Compléments utiles

| Outil           | Rôle principal                    |
|------------------|------------------------------------|
| `pytest`         | Exécution des tests, assertions    |
| `coverage`       | Rapport de couverture              |
| `hypothesis`     | Tests basés sur la propriété       |
| `tox`            | Tests multi-envs                   |
| `unittest.mock`  | Mocks intégrés                     |
| `pytest-mock`    | Intégration des mocks avec pytest  |
| `pytest-asyncio` | Pour tester du code async          |

---

## 📦 Intégration avec `poetry`

```toml
[tool.poetry.dev-dependencies]
pytest = "^8.0"
pytest-mock = "^3.12"
coverage = "^7.4"
hypothesis = "^6.100"
tox = "^4.14"
```

---
