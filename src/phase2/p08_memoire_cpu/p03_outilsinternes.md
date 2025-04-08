# ✅ Outils internes à Python ≥ 3.12** (ou disponibles en standard avec la distribution) qui t’aident à **analyser, profiler et optimiser la mémoire** et les performances de ton code :

## 🧠 **1. `sys` – Outils mémoire basiques**

```python
import sys

obj = [1, 2, 3]
print(sys.getsizeof(obj))  # taille en octets
```

> `sys.getsizeof()` permet de voir la taille en mémoire d’un objet, **hors références imbriquées**.

---

## 📊 **2. `tracemalloc` – Profiler mémoire intégré**

```python
import tracemalloc

tracemalloc.start()

# Code à profiler...
big_list = [x for x in range(10_000_000)]

current, peak = tracemalloc.get_traced_memory()
print(f"Actuel: {current / 1e6:.2f} Mo ; Pic: {peak / 1e6:.2f} Mo")

tracemalloc.stop()
```

> Trace la consommation mémoire **ligne par ligne**, très utile pour voir où la mémoire augmente.

✅ Depuis **Python 3.12**, tu peux aussi obtenir **l’historique détaillé** des allocations avec `Snapshot.statistics()`.

---

## 🐍 **3. `sys.monitoring` (nouveau en 3.12)**

```python
import sys.monitoring
```

> Nouvel outil en Python 3.12 pour **observer dynamiquement** l’exécution de code (hooks sur fonction, ligne, appel, etc.)

🔧 Très utile pour écrire des outils de profilage personnalisés ou des **audits dynamiques de performance.**

---

## 🐢 **4. `profile` et `cProfile` – Profilage CPU**

```bash
python -m cProfile -s time script.py
```

> Profilers intégrés pour **mesurer le temps d’exécution** de chaque fonction. `cProfile` est plus rapide car en C.

Tu peux aussi l’utiliser en code :
```python
import cProfile

def main():
    ...

cProfile.run('main()')
```

Pour une meilleure lisibilité :
```bash
pip install snakeviz
snakeviz output.prof  # interface web
```

---

## 📌 **5. `functools.cache_info` + `@cache` ou `@lru_cache`**

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

fib(100)
print(fib.cache_info())
```

> Cache les résultats de fonctions coûteuses en CPU mais légères en RAM. À monitorer pour éviter de **surcharger la mémoire**.

---

## 🔥 **6. `gc` – Contrôle du Garbage Collector**

```python
import gc

gc.set_debug(gc.DEBUG_STATS)
gc.collect()
```

> Permet d’**analyser les cycles de mémoire** et les objets non collectés. Très utile si tu suspectes une **fuite mémoire.**

---

## 🧩 BONUS : outils du standard mais pas "intégrés" par défaut

| Outil               | Installation | Utilité principale                       |
|--------------------|--------------|-------------------------------------------|
| `memory_profiler`  | `pip install memory-profiler` | Profiling mémoire ligne par ligne |
| `py-spy`           | binaire externe | Profiler ultra-rapide, non intrusif |
| `objgraph`         | `pip install objgraph` | Visualisation de structures mémoire |
| `Pympler`          | `pip install pympler` | Analyse mémoire avancée (objets vivants) |

---

Tu veux que je te crée un **template de projet Python avec `tracemalloc`, `cProfile` et logs intégrés** pour profiler proprement ton code ?