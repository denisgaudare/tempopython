### 🧠 Concepts à comprendre

#### 1. **Typage dynamique et duck typing**
- Python n’a pas de types explicites (sauf annotations).
- Comprendre que le typage se fait à l'exécution, et que l'important est ce que l'objet **fait**, pas ce qu'il **est** (`if hasattr(obj, 'read'):` plutôt que `obj is StreamReader`).

#### 2. **Tout est objet**
- Même les fonctions, modules et types de base sont des objets.
- Les objets peuvent être passés, stockés, modifiés.

#### 3. **Indentation significative**
- Pas d’accolades : l’indentation **fait partie** de la syntaxe.

#### 4. **Pas de structures statiques comme `class static void Main()`**
- Le code peut s’exécuter directement (top-level), avec éventuellement `if __name__ == '__main__':`.

---

### 🧱 Vocabulaire Python spécifique

| Concept C#              | Équivalent Python            |
|------------------------|-----------------------------|
| Namespace              | Module                      |
| Property               | `@property`                 |
| Interface              | Duck typing ou `abc.ABC`    |
| using / IDisposable    | `with` et `contextlib`      |
| Exception filter       | `try/except` (pas de filtre spécifique, mais on peut `except SomeException as e:`) |
| Nullable               | `None`                      |
| foreach                | `for item in iterable:`     |
| Lambda                 | `lambda` (mais limité à une expression) |
| Dictionary             | `dict`                      |
| List<T>                | `list`                      |

---

### 🧰 Modules standard indispensables pour du scripting

| Besoin courant                  | Module Python              |
|--------------------------------|----------------------------|
| Manipuler fichiers             | `os`, `pathlib`, `shutil`  |
| Argument en ligne de commande  | `argparse`, `sys.argv`     |
| Lire/écrire du JSON            | `json`                     |
| Temps et date                  | `datetime`, `time`         |
| Télécharger ou appeler API     | `requests` (non stdlib, mais incontournable) |
| Expressions régulières         | `re`                       |
| Travailler avec des fichiers CSV | `csv`, `pandas` (optionnel) |
| Créer des fichiers temporaires | `tempfile`                 |
| Logging                        | `logging`                  |
| Compression (zip, tar, gzip)   | `zipfile`, `tarfile`, `gzip` |
| Sérialisation légère           | `pickle`                   |
| Script long / schedulé         | `time.sleep`, `schedule` (non stdlib) |

---

### 🔁 Syntaxe à adopter

- **List comprehensions**  
  ```python
  squares = [x * x for x in range(10)]
  ```

- **Unpacking**  
  ```python
  a, b = b, a
  ```

- **F-strings**  
  ```python
  name = "Alice"
  print(f"Hello {name}")
  ```

- **Fonctions anonymes avec `lambda`**  
  ```python
  sorted(data, key=lambda x: x[1])
  ```

- **Fonctions de haut niveau : `map`, `filter`, `any`, `all`, `zip`, `enumerate`**  
  ```python
  for i, val in enumerate(mylist):
      print(i, val)
  ```

---

### 🧼 Bonnes pratiques

- Suivre le **PEP 8** (style guide)
- Utiliser des **docstrings** (`"""Description"""`)
- Penser "pythonic" : éviter les structures trop formelles (comme les classes inutiles)
- Préférer `pathlib.Path` à `os.path`
- Utiliser `venv` pour isoler les environnements

---

### ➕ Bonus pour les développeurs avancés

- `itertools` et `functools`
- Générateurs (`yield`) et fonctions paresseuses
- Décorateurs
- Comprendre les différences entre `is`, `==`, `in`
- Typage avec `typing` (`List[int]`, `Optional[str]`, etc.)

---

## 🧠 Concepts avancés à maîtriser

### 1. **Générateurs et paresse**
- Utiliser `yield`, `generator expressions`, `itertools` pour traiter de grandes quantités de données sans tout charger en mémoire.
  ```python
  def read_lines(filepath):
      with open(filepath) as f:
          for line in f:
              yield line
  ```

### 2. **Compréhension fine de la gestion mémoire**
- Le ramasse-miettes (`gc`) fonctionne par **comptage de références** + détection des cycles.
- Attention aux **références circulaires** ou objets capturés par des closures ou des callbacks.

### 3. **Mutabilité vs immutabilité**
- `list`, `dict`, `set` sont mutables, `tuple`, `frozenset` ne le sont pas.
- Comprendre les implications pour la **copie** (`copy`, `deepcopy`) et la **sécurité fonctionnelle**.

### 4. **Objets légers et slots**
- Pour optimiser les objets souvent instanciés : `__slots__` réduit la mémoire.
  ```python
  class Point:
      __slots__ = ('x', 'y')
  ```

---

## 🚦 Qualité de code

### 1. **Linters et formatteurs**
- `flake8`, `pylint`, `mypy`, `black`, `isort` : pour automatiser qualité, lisibilité et typage statique.

### 2. **Typage statique avec `typing`**
- Même si non obligatoire, très utile pour détection d’erreurs + documentation :
  ```python
  def get_name(user: dict[str, str]) -> str:
      return user['name']
  ```

### 3. **Tests unitaires**
- `unittest`, `pytest`, `doctest` : essentiels pour des scripts fiables et testables.
- Utiliser des fixtures, mocks (`unittest.mock`) pour isoler les dépendances.

### 4. **Structure modulaire**
- Organiser les scripts avec des fonctions, puis des modules, puis éventuellement un petit package.
- Exemple typique :
  ```
  myscript/
    ├── __main__.py
    ├── core.py
    ├── utils.py
    └── config.yaml
  ```

---

## 🔍 Analyse de performance

### 1. **Mesure temps d'exécution**
- Avec `time`, `timeit`, `cProfile`, `line_profiler`
  ```python
  import timeit
  print(timeit.timeit("x = sum(range(100))", number=1000))
  ```

### 2. **Profiling mémoire**
- `tracemalloc`, `memory_profiler`, `objgraph`
  ```python
  import tracemalloc
  tracemalloc.start()
  ```

### 3. **Optimisation CPU**
- Eviter les boucles explicites → préférer les opérations vectorisées (via `numpy`, `pandas`)
- Utiliser `multiprocessing`, `concurrent.futures`, `asyncio` selon le cas :
  - **CPU-bound** → `multiprocessing`
  - **IO-bound** → `asyncio` ou `ThreadPoolExecutor`

---

## 🛠️ Patterns utiles et idiomatiques

- **`if __name__ == "__main__":`** pour rendre le script réutilisable
- **Context managers personnalisés** via `contextlib`
- **Logging configurable** via `logging.config`
- **Memoization** via `functools.lru_cache`

---

## 📦 Bonnes pratiques de packaging & exécution

- Structurer le script pour pouvoir l’**importer sans exécuter** tout (`main`)
- Ajouter un `requirements.txt` ou `pyproject.toml`
- Utiliser `argparse` pour faire des CLI robustes
- Intégrer un `Makefile` ou un outil comme `invoke` pour automatiser (`make run`, `make lint`, etc.)

---

## 📘 Ressources recommandées

- Livre : **"Effective Python" (Brett Slatkin)**
- Site : [https://realpython.com](https://realpython.com)
- Outils : `rich`, `typer`, `click`, `pydantic`, `attrs`

