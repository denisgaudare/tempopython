
# 🧠 `joblib` : Présentation complète

---

## 📌 Qu’est-ce que `joblib` ?

> `joblib` est une bibliothèque Python pour :
- ⚡ **exécuter des fonctions en parallèle** (sur plusieurs cœurs)
- 💾 **sérialiser (sauvegarder) des objets lourds**
- 🧠 Optimiser des calculs coûteux avec du **memoization** (cache)

Très utilisée dans les domaines **data science**, **machine learning**, **calcul scientifique**, etc.

📦 Installation :
```bash
pip install joblib
```

---

## 🚀 1. Exécution parallèle

### ✅ Exemple simple : traitement d'une liste en parallèle

```python
from joblib import Parallel, delayed
import time

def slow_square(n):
    time.sleep(1)
    return n * n

results = Parallel(n_jobs=4)(delayed(slow_square)(i) for i in range(8))
print(results)
```

### 🔍 Explication :
- `n_jobs=4` : nombre de **processus** utilisés (🧠 pas threads)
- `delayed(f)(x)` : transforme `f(x)` pour un appel différé
- En parallèle → beaucoup plus rapide que une boucle classique

---

### ✅ Variante avec fonction lambda

```python
Parallel(n_jobs=2)(delayed(lambda x: x**2)(i) for i in range(5))
```

---

## 🧠 2. Mémoization / Caching

### ✅ Exemple : mise en cache d'une fonction coûteuse

```python
from joblib import Memory
import time

memory = Memory(location=".joblib_cache", verbose=1)

@memory.cache
def slow_fn(x):
    time.sleep(2)
    return x ** 2

print(slow_fn(10))  # lent
print(slow_fn(10))  # instantané : chargé depuis cache
```

- `Memory` permet de **sauvegarder automatiquement le résultat d’une fonction**
- Très utile en **expérimentation / notebook** pour éviter de relancer tout

---

## 💾 3. Sauvegarde/chargement d’objets Python

> Alternative optimisée à `pickle`, surtout pour **objets NumPy lourds**

```python
from joblib import dump, load
import numpy as np

data = {"a": np.random.rand(1000, 1000)}
dump(data, "data.joblib")

# Plus tard...
data2 = load("data.joblib")
```

- Plus rapide que `pickle` pour tableaux NumPy
- Compatible avec scikit-learn (modèles ML, transformers, etc.)

---

## 📦 4. Cas d’usage concrets

| Besoin                             | Solution `joblib`                              |
|------------------------------------|-------------------------------------------------|
| Paralléliser une boucle de calculs | `Parallel` + `delayed`                         |
| Éviter de relancer des calculs     | `@memory.cache`                                |
| Sauvegarder des modèles ML         | `dump(model, 'model.joblib')`                 |
| Gagner du temps avec de gros tableaux | `dump/load` plus rapide que `pickle`        |

---

## 🧠 joblib vs alternatives

| Fonction                 | joblib       | pickle     | multiprocessing | dask       |
|--------------------------|--------------|------------|------------------|------------|
| Sauvegarde objets        | ✅ rapide    | ✅          | ❌               | ❌         |
| Parallélisme CPU-bound   | ✅ (process) | ❌          | ✅               | ✅         |
| Cache de fonction        | ✅           | ❌          | ❌               | ✅         |
| Utilisation avancée      | Moyenne      | Très basique | Complexe         | Avancée    |

---

## ⚠️ Limitations

- `n_jobs=-1` = **utilise tous les cœurs** ➤ attention à la RAM ⚠️
- Ne marche pas avec des fonctions **non sérialisables** (ex. lambdas imbriquées, objets non picklables)
- Pas conçu pour le **parallélisme distribué** (cluster → voir Dask ou Ray)

---

## 📚 Références

- Doc officielle : https://joblib.readthedocs.io/
- Utilisé massivement dans : `scikit-learn`, `statsmodels`, `skopt`, etc.

---
