## Synthèse performances

## 1️⃣ Techniques Python pour optimiser performance

### a. **Générateurs et itérateurs**
Remplacent les listes en mémoire par des flux.

```python
def read_lines(file):
    with open(file) as f:
        for line in f:
            yield line
```

✅ Avantages :
- Évite de tout charger en RAM  

❌ Inconvénients :
- Pas de random access (une fois lue, la donnée est perdue)

---

### b. **Compréhensions avec conditions**
Évite des for-loops coûteuses

```python
squares = [x*x for x in range(1000) if x % 2 == 0]
```

✅ Avantages :
- Plus rapide que les `for`

❌ Limites :
- Moins lisible si trop complexe

---

### c. **Structures légères : `__slots__`**
Réduit l’empreinte mémoire des objets

```python
class Flight:
    __slots__ = ['id', 'origin', 'destination']
```

✅ Réduction mémoire jusqu’à -40%  
❌ Pas d’attribut dynamique possible

---

### d. **Fonctions natives vectorisées**
Utiliser `sum()`, `map()`, `zip()` au lieu de boucles

```python
res = sum(map(lambda x: x**2, range(1000)))
```

✅ Utilise des implémentations C plus rapides  
❌ Moins flexible, parfois illisible

---

## 2️⃣ Bibliothèques optimisées

### a. **NumPy / Pandas**
Calcul vectorisé en C, très rapide pour dataframes et matrices

```python
import numpy as np
a = np.arange(1e6)
b = a * 2  # très rapide
```

✅ Facteur x10 à x100 comparé aux boucles Python  
❌ Nécessite adaptation du code (pas de for classiques)

---

### b. **Polars**
DataFrame ultra-rapide, Rust + lazy evaluation

```python
import polars as pl
df = pl.read_csv("flights.csv").filter(pl.col("airline") == "AF")
```

✅ Plus rapide que Pandas, moins gourmand  
❌ Moins mature, API différente

---

### c. **Joblib / multiprocessing**
Parallélisation simple des tâches

```python
from joblib import Parallel, delayed
results = Parallel(n_jobs=4)(delayed(process)(i) for i in range(10))
```

✅ Gagne du temps sur CPU multicoeurs  
❌ Pas efficace pour I/O (préférer `asyncio`)

---

### d. **Dask / Vaex / Modin**
Permettent de paralléliser le traitement de `pandas` sur plusieurs cœurs (ou cluster)

```python
import dask.dataframe as dd
df = dd.read_csv("bigfile.csv")
```

✅ Travaille sur des jeux de données qui dépassent la RAM  
❌ Setup plus complexe, pas toujours 100% compatible Pandas

---

## 3️⃣ Interpréteurs et compilateurs alternatifs

### a. **PyPy**
Interpréteur Python avec JIT (Just-In-Time Compiler)

```bash
pypy script.py
```

✅ Accélère le code Python "pur" (boucles, calculs) jusqu’à x5  
❌ Moins compatible avec certaines libs (ex: NumPy)

---

### b. **Cython**
Compile du Python vers du C

```python
# fichier mymodule.pyx
def f(int x):
    return x * x
```

```bash
cythonize -i mymodule.pyx
```

✅ Très rapide pour les calculs intensifs  
❌ Nécessite compilation, parfois difficile à maintenir

---

### c. **Numba**
Compile à la volée du Python scientifique avec JIT

```python
from numba import jit

@jit
def compute(x):
    return x * x
```

✅ Très efficace pour les fonctions numériques pures  
❌ Moins bon sur les types dynamiques ou les structures complexes

---

## 🧠 Résumé global

| Méthode               | Temps     | Mémoire   | Difficulté | Remarques                             |
|-----------------------|-----------|-----------|------------|----------------------------------------|
| Générateurs           | ✅         | ✅         | 🟢 Facile   | Idéal pour I/O, fichiers                |
| NumPy/Pandas          | ✅✅       | ✅         | 🟡 Moyen    | Parfait pour calculs vectoriels        |
| Polars                | ✅✅✅     | ✅✅       | 🟡 Moyen    | Ultra rapide, base Rust                |
| PyPy                  | ✅✅       | =         | 🟢 Facile   | Aucun changement de code parfois       |
| Cython/Numba          | ✅✅✅     | ✅         | 🔴 Avancé   | À réserver pour les bottlenecks        |
| Dask/Modin/Vaex       | ✅         | ✅✅       | 🟡 Moyen    | Gère les très gros volumes             |
