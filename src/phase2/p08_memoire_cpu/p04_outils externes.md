# ✅ Panorama des meilleurs outils externes pour l’optimisation mémoire et CPU en Python**, avec pour chaque outil :

- 📌 But
- ⚙️ Installation
- ✅ Exemple exhaustif et expliqué
- 🧠 Cas d’usage typiques

---

## 🧪 1. `memory_profiler` – **Profiling mémoire ligne par ligne**

📌 **Analyse de la mémoire utilisée à chaque ligne d'une fonction.**

⚙️ Installation :
```bash
pip install memory-profiler
```

✅ Exemple :
```python
from memory_profiler import profile

@profile
def create_large_list():
    a = [i for i in range(1_000_000)]
    b = [str(i) for i in a]
    return b

create_large_list()
```

💡 Lancer avec :
```bash
python -m memory_profiler script.py
```

📈 Résultat :
```
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     4     20.1 MiB     20.1 MiB           1   a = [i for i in range(1_000_000)]
     5     50.5 MiB     30.4 MiB           1   b = [str(i) for i in a]
```

🧠 Idéal pour repérer les **lignes très coûteuses** en mémoire.

---

## 🧠 2. `tracemalloc` + `Pympler` – **Traque fine des objets en RAM**

📌 `Pympler` complète `tracemalloc` pour savoir **quels types d’objets occupent la mémoire**.

⚙️ Installation :
```bash
pip install pympler
```

✅ Exemple :
```python
from pympler import muppy, summary

def do_work():
    a = [i for i in range(1000000)]
    b = {'x': a}
    return b

do_work()

all_objects = muppy.get_objects()
sum_stats = summary.summarize(all_objects)
summary.print_(sum_stats)
```

📈 Résultat :
```
TYPE       |   COUNT |   TOTAL SIZE
----------------------------------
list       |   1000010 | 38.1 MiB
dict       |     1000 | 0.5 MiB
```

🧠 Excellent pour repérer les **types d’objets "gourmands"** (dict, list, etc.) dans un contexte large.

---

## 🔎 3. `objgraph` – **Visualiser les graphes d’objets en RAM**

📌 Suivre les **références entre objets** et repérer les fuites mémoire (cycles, non collectés, etc.)

⚙️ Installation :
```bash
pip install objgraph graphviz
```

✅ Exemple :
```python
import objgraph

class A:
    pass

a = A()
b = A()
a.ref = b
b.ref = a  # Référence circulaire

objgraph.show_backrefs([a], filename='ref_graph.png')
```

📈 Produit un **graphique image** (`ref_graph.png`) des objets et leurs références.

🧠 Idéal pour débusquer les **cycles de références** ou les objets qui ne sont pas libérés.

---

## 🕵️ 4. `py-spy` – **Profiler CPU sans modifier le code**

📌 Profiler ultra-rapide, sans instrumentation, même sur un script en cours d'exécution !

⚙️ Installation :
```bash
pip install py-spy
```
ou binaire direct : https://github.com/benfred/py-spy

✅ Exemple (depuis terminal) :
```bash
py-spy top --pid $(pgrep -f script.py)
```

✅ Enregistrement :
```bash
py-spy record -o profile.svg -- python script.py
```

📈 Résultat : un **flamegraph interactif** pour analyser les appels les plus coûteux.

🧠 Outil de référence pour comprendre **les ralentissements CPU** sans toucher au code source.

---

## 🌐 5. `line_profiler` – **Profilage du temps d’exécution ligne par ligne**

📌 Pour mesurer précisément **le temps** passé à chaque ligne d’une fonction.

⚙️ Installation :
```bash
pip install line_profiler
```

✅ Exemple :
```python
@profile
def slow_function():
    total = 0
    for i in range(1_000_000):
        total += i
    return total
```

💡 Lancer avec :
```bash
kernprof -l -v script.py
```

📈 Résultat :
```
Timer unit: 1e-06 s
Total time: 0.500 s
Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     2         1            0      0.0      0.0  def slow_function():
     3         1            1      1.0      0.2      total = 0
     4   1000000       499999      0.5     99.9      total += i
```

🧠 Permet de zoomer sur les **lignes exactes qui ralentissent** un traitement.

---

## 📉 Synthèse des outils

| Outil           | Ce qu'il analyse          | Interface         | Avantage clé                        |
|----------------|---------------------------|-------------------|-------------------------------------|
| `memory_profiler` | Mémoire ligne par ligne   | CLI / texte        | Simple, rapide                      |
| `pympler`       | Type d’objets mémoire      | Console            | Vue d’ensemble                      |
| `objgraph`      | Graphes mémoire            | Image `.png`       | Détection de fuites                 |
| `py-spy`        | Temps CPU global           | Terminal / SVG     | Aucun besoin de modifier le code    |
| `line_profiler` | Temps ligne par ligne      | CLI                | Hyper-précis                        |
| `tracemalloc`   | Allocation mémoire native  | Console            | Inclus en standard                  |

---
