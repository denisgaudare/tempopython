# Outils memoire 

## 🧠 1. **Big-O Calculator avec `big-O-calculator` (théorique)**

📌 Analyse (statique) de la **complexité algorithmique approximée**.

⚙️ Installation :
```bash
pip install bigO
```

✅ Exemple :
```python
import bigO

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

lib = bigO.BigO()
lib.test(bubble_sort, "random")  # Peut aussi faire "sorted", "inversed", etc.
```

📈 Résultat :
```
Best complexity: O(n)
Average complexity: O(n^2)
```

🧠 C’est un **outil d’approximation** utile pour détecter les algorithmes inefficaces.

---

## ⚙️ 2. **`scalene` – Profiler algorithmique multi-dimension**

📌 Mesure le **temps CPU, mémoire et temps d’attente I/O** ligne par ligne. Excellent pour détecter les goulets d'étranglement algorithmique.

⚙️ Installation :
```bash
pip install scalene
```

✅ Exemple :
```bash
scalene my_script.py
```

📈 Résultat :
- Détaille chaque ligne avec :
  - `% CPU`
  - `% I/O`
  - `% Memory`
  - Nombre de fois appelée

🧠 Scalene est **plus fin que cProfile** pour l'analyse algorithmique réelle (ex. si la lenteur vient du disque, pas de l’algo).

---

## 📊 3. **`pyinstrument` – Profiler d'exécution ultra lisible**

📌 Mesure l’appel des fonctions **dans l’ordre d’exécution réelle**, avec une hiérarchie claire.

⚙️ Installation :
```bash
pip install pyinstrument
```

✅ Exemple :
```python
from pyinstrument import Profiler

profiler = Profiler()
profiler.start()

# Code à profiler
my_function()

profiler.stop()
print(profiler.output_text(unicode=True, color=True))
```

📈 Affiche un **arbre d’exécution** avec le pourcentage de temps passé par fonction.

🧠 Idéal pour visualiser la structure algorithmique **réelle** de l’exécution.

---

## 📐 4. **`codetiming` – Mesure de blocs critiques personnalisés**

📌 Utilitaire simple pour mesurer des blocs spécifiques de code (utile pour comparer 2 approches algorithmiques).

⚙️ Installation :
```bash
pip install codetiming
```

✅ Exemple :
```python
from codetiming import Timer

with Timer(name="méthode_1", text="{name}: {seconds:.4f} sec"):
    methode_1()

with Timer(name="méthode_2", text="{name}: {seconds:.4f} sec"):
    methode_2()
```

🧠 Très utile pour **benchmarker deux implémentations** de la même tâche.

---

## 🧪 5. **`line_profiler` avec `kernprof` – Profilage algorithmique par ligne**

📌 Déjà cité mais ultra utile ici : mesure le **temps par ligne**, donc utile pour optimiser un algo ligne par ligne.

⚙️ Installation :
```bash
pip install line_profiler
```

✅ Exemple :
```python
@profile
def my_algo():
    ...
```

```bash
kernprof -l -v myscript.py
```

---

## 🧰 BONUS – Outils annexes pour l’analyse et l’optimisation :

| Outil                | Utilité principale                                       |
|---------------------|----------------------------------------------------------|
| `pyperf`             | Benchmark rigoureux (boucles multiples, statistiques)   |
| `asv` (airspeed velocity) | Benchmark automatique de versions d’un même code |
| `cProfile + SnakeViz`| Visualisation des appels coûteux dans le graphe         |
| `Numba` / `Cython`   | Pour optimiser le cœur algorithmique par compilation    |

---

## ✅ Recommandations combinées

| Objectif | Outils à combiner |
|---------|-------------------|
| Analyser un algorithme | `bigO`, `pyinstrument`, `line_profiler` |
| Optimiser CPU | `scalene`, `py-spy`, `cProfile`, `Timer` |
| Comparer deux versions | `codetiming`, `pyperf` |
| Détecter mauvaise structure | `pyinstrument`, `py-spy`, `asv` |

---

Souhaites-tu que je te génère un **projet comparatif** avec deux implémentations d’un même algo (ex: tri), testées avec `codetiming`, `bigO`, `scalene` et `pyinstrument` ?