
---

## 🧠 Objectif de la session
> "Utiliser Pandas pour manipuler, transformer, agréger et analyser efficacement des données tabulaires."

---

## 🗂️ PLAN DE SESSION : Pandas pour développeurs Python

---

### 1. ⚙️ Introduction rapide
- Qu'est-ce qu'une `Series`, un `DataFrame` ?
- Pourquoi Pandas : surcouche de NumPy orientée données tabulaires

```python
import pandas as pd

data = pd.Series([10, 20, 30], index=["a", "b", "c"])
print(data["b"])  # 20
```

---

### 2. 📥 Chargement de données

- `read_csv`, `read_excel`, `read_json`, `read_sql`
- Astuces : `parse_dates`, `dtype`, `usecols`

```python
df = pd.read_csv("data.csv", parse_dates=["date","naissance"], usecols=["id", "date", "value"])
```
pratiques : spécifier les colonnes, les types, ne pas faire `read_csv` sur un fichier de 3 Go sans précaution.


---

### 3. 🔍 Exploration & filtrage

- `.head()`, `.info()`, `.describe()`
- Sélection : `.loc`, `.iloc`, masques booléens

```python
df[df["value"] > 100]
df.loc[df["date"] > "2023-01-01", ["id", "value"]]
```

---

### 4. 🔁 Transformation & nettoyage

- Fonctions utiles : `.fillna()`, `.dropna()`, `.astype()`, `.rename()`, `.apply()`
- Créer des colonnes calculées

```python
df["ratio"] = df["value"] / df["value"].sum()
df["label"] = df["value"].apply(lambda x: "High" if x > 100 else "Low")
```

> 💡 Comparaison `.apply()` vs vectorisation

---

### 5. 🧮 GroupBy & agrégation

- `.groupby()`, `.agg()`, `.transform()`
- Multi-index et hiérarchies

```python
df.groupby("label")["value"].agg(["mean", "sum"])
```

---

### 6. 🪄 Reshape & pivot

- `.pivot_table()`, `.melt()`, `.stack()`, `.unstack()`

```python
pivot = df.pivot_table(index="id", columns="label", values="value", aggfunc="sum")
```

---

### 7. 📊 Visualisation simple

- `.plot()` intégré
- Couplage avec `matplotlib`/`seaborn`

```python
df["value"].plot(kind="hist", bins=20)
```

---

### 8. 🧠 Tricks & bonnes pratiques Pandas

- `pd.to_datetime()`, `pd.cut()`, `pd.qcut()`
- Trier : `.sort_values()`, `.nlargest()`
- Chaînage de méthodes (`df.pipe()`)

---

### 9. ⚠️ Erreurs classiques

- Copie vs vue (`SettingWithCopyWarning`)
- Utiliser `.apply()` là où une op vectorisée suffit
- Mauvaise gestion des types (`object` vs `category`)

---

### 🔚 10. Mini-challenge live (15-20 min)

> Donne un petit dataset et une mission :
- Nettoyer les données
- Calculer des moyennes par groupe
- Générer un pivot
- Sortir un top 5

---

## 💡 Bonus si tu as plus de temps :
- Performance (vs Polars, Dask, NumPy pur)
- `df.query()` et `df.eval()` pour écrire plus clair
- Utiliser `categorical` pour mémoire/CPU
