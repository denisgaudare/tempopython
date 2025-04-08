# ✅ Comparer `guppy3` et `tracemalloc`
## complémentaires pour l’analyse mémoire,mais ils ont des **philosophies et usages différents**. Voici ce que **`guppy3` apporte en plus** :

---

# 🧠 Ce que `guppy3` apporte par rapport à `tracemalloc`

## ✅ 1. **Vue orientée objets vivants**

| `guppy3` observe…       | …l’état actuel **des objets vivants** |
|--------------------------|----------------------------------------|
| ✅ Taille réelle (RAM)   | totale et par type                    |
| ✅ Nombre d'objets       | par type (`list`, `dict`, etc.)       |
| ✅ Graphe des références | qui référence quoi (→ fuite possible) |
| ✅ Représentation hiérarchique | structure de mémoire réelle       |

`tracemalloc`, lui, mesure **les allocations mémoire passées**, pas ce qui est **encore vivant**.

---

## ✅ 2. **Graphe d’objets (references & ownership)**

Tu peux visualiser par exemple :

```python
from guppy import hpy
h = hpy()
print(h.heap().bytype)  # regroupe les objets par type
```

Et même :

```python
print(h.heap().byrcs)  # groupé par « reference count set »
```

→ Très utile pour traquer les **cycles de référence** ou les **objets "orphelins"** qui ne sont pas libérés.

---

## ✅ 3. **Navigation interactive en live**

Tu peux inspecter un objet mémoire :

```python
heap = h.heap()
lists = heap.bytype['list']
print(lists[0])  # affiche un objet mémoire et ses liens
```

Tu peux même remonter la chaîne de références pour savoir **pourquoi un objet n’est pas libéré**.

---

## ✅ 4. **Point de référence (`setref()`) pour comparaison différée**

```python
h.setref()  # marque un état de référence
...
print(h.heap().diff())  # montre les objets créés après le setref
```

🔍 Très utile pour détecter les **fuites mémoire** sur une portion de code ou dans une boucle.

---

## ✅ 5. **Fonctionne avec CPython pur**

- Pas besoin d’instrumentation
- Fonctionne même sur du code tiers sans accès au code source

---

## 🔄 Résumé comparatif

| Fonction                    | `guppy3`                      | `tracemalloc`                   |
|----------------------------|-------------------------------|---------------------------------|
| 🧠 Vue des objets vivants  | ✅                             | ❌ (seulement historique)        |
| 📦 Par type d'objet        | ✅ (`bytype`, `byrcs`, etc.)   | ❌                              |
| 🔁 Graphe de références     | ✅                             | ❌                              |
| 🕵️‍♀️ Recherche de fuite    | ✅ en différentiel              | ✅ via snapshots comparés        |
| 📜 Stack trace             | ❌                             | ✅ (précis par ligne de code)    |
| 📈 Visualisation courbe    | à construire via `matplotlib` | non natif mais possible         |
| 🧪 Intégration low-level   | CPython natif                 | Instrumentation allocations     |

---

## 🔧 Recommandation

| Besoin                                      | Outil conseillé    |
|--------------------------------------------|--------------------|
| Analyse mémoire par ligne de code          | `tracemalloc`      |
| Comprendre **ce qui vit en mémoire**       | `guppy3`           |
| Traquer des objets non libérés             | `guppy3`           |
| Suivi global + graphique                   | `guppy3` + `matplotlib` |
| Suivi d’allocation précis dans le temps    | `tracemalloc`      |
| Usage simple en script de prod             | `tracemalloc`      |

---
