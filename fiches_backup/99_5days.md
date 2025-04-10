
## 🎯 Objectif de la présentation
Permettre à des développeurs Python expérimentés de :
- Monter en compétence sur des bibliothèques modernes et performantes.
- Approfondir leur compréhension du fonctionnement de Python.
- Savoir profiler, optimiser et structurer leur code pour des cas réels.

---

## 🗓️ Programme proposé (2 jours ou découpé en modules)

### 🔹 1. Intro + Rappels nécessaires (30 min)
- Différences CPython vs PyPy
- Comprendre le GIL (Global Interpreter Lock)
- Gestion mémoire en Python (référence, GC, cycles)

---

### 🔹 2. Python Performant
#### 🧠 Concepts
- Profiling avec `cProfile`, `line_profiler`, `memory_profiler`
- Optimisation avec `functools.lru_cache`, `numba`, `cython` (intro)
- Benchmarks : `timeit`, `perf`

#### 🛠️ Atelier
- Profiling d’un script lent → refactor + gain de perf

---

### 🔹 3. Manipulation de données avancée : Pandas vs Polars
- Concepts : lazy vs eager, memory mapping
- Benchmarks comparés
- Quand utiliser l’un ou l’autre ?
- Cas pratiques : agrégation, jointures, window functions

---

### 🔹 4. Asyncio & Concurrence en Python
- `async`, `await`, `event loop`
- Différences `threading`, `multiprocessing`, `asyncio`
- Exemple de web scraper concurrent

---

### 🔹 5. Architecture & Design Patterns Python
- Patterns utiles : Factory, Strategy, Decorator
- Modèles orientés événement : pub/sub avec `pydantic` + `fastapi`
- Typage fort avec `typing`, `mypy`, `pydantic`

---

### 🔹 6. Packaging & Déploiement moderne
- `pyproject.toml` (PEP 518), `poetry`, `setuptools`
- Structurer un projet (src layout, tests, versionning)
- Publishing sur PyPI / GitHub Release

---

### 🔹 7. Librairies utiles et méconnues
- `typer` : CLI moderne
- `rich` / `textual` : affichage riche en console
- `pydantic` : validation forte
- `hydra` / `omegaconf` : gestion de config
- `polars`, `numpy`, `dask` : pour le data

---

### 🔹 8. Code Quality & Tests
- Linters (`ruff`, `flake8`, `pylint`)
- Formatters (`black`, `isort`)
- Tests unitaires et property-based (`pytest`, `hypothesis`)
- Intégration continue (CI) avec `GitHub Actions`

---

### 🔹 9. Bonus au choix selon public
- Génération PDF avec `jinja2` + `weasyprint`
- Python + Web avec `FastAPI` ou `Streamlit`
- Python pour le traitement d’image : `pillow`, `opencv`
- Python + Cloud : intro à AWS Lambda, boto3

---
