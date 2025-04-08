Comparer **Pandas**, **Polars** et **Dask** est très pertinent, surtout pour des devs expérimentés. Voici :

---

## 🎯 **Objectif**
Comparer les **fonctions et manipulations courantes** entre :
- 🐼 **Pandas** (référence historique)
- 🐻‍❄️ **Polars** (ultra rapide, lazy/eager)
- 🧱 **Dask** (parallélisé, out-of-core)

---

## 📦 Préparation : installation

```bash
pip install pandas polars dask
```

---

## 🧪 Exemple de dataset commun (fichier CSV `transactions_sample.csv`)

```python
# Pour Pandas
import pandas as pd
df_pd = pd.read_csv("transactions_sample.csv", parse_dates=["date"])

# Pour Polars
import polars as pl
df_pl = pl.read_csv("transactions_sample.csv", try_parse_dates=True)

# Pour Dask
import dask.dataframe as dd
df_dask = dd.read_csv("transactions_sample.csv", parse_dates=["date"])
```

---

## 📋 Comparatif des opérations de base

| Opération | Pandas | Polars | Dask |
|----------|--------|--------|------|
| **Afficher 5 lignes** | `df.head()` | `df.head()` | `df.head()` |
| **Filtrer une valeur** | `df[df["montant"] > 100]` | `df.filter(pl.col("montant") > 100)` | `df[df["montant"] > 100].compute()` |
| **GroupBy somme** | `df.groupby("categorie")["montant"].sum()` | `df.groupby("categorie").agg(pl.sum("montant"))` | `df.groupby("categorie")["montant"].sum().compute()` |
| **Ajouter colonne calculée** | `df["tva"] = df["montant"] * 0.2` | `df = df.with_columns((pl.col("montant") * 0.2).alias("tva"))` | `df["tva"] = df["montant"] * 0.2` *(puis `.compute()`)* |
| **Tri** | `df.sort_values("montant", ascending=False)` | `df.sort("montant", descending=True)` | `df.sort_values("montant", ascending=False).compute()` |
| **Dates (mois)** | `df["mois"] = df["date"].dt.month` | `df = df.with_columns(pl.col("date").dt.month().alias("mois"))` | `df["mois"] = df["date"].dt.month` |

---

## ⚡ Benchmarks (facultatif en démo)
- Sur gros fichiers CSV (1M lignes+), Polars est souvent 3-10x plus rapide que Pandas.
- Dask peut traiter des fichiers plus gros que la RAM, mais requiert `.compute()`.

---

## 📎 Notes pédagogiques :

| | Pandas | Polars | Dask |
|--|--------|--------|------|
| Langage | API classique | API inspirée Rust | API Pandas-like |
| Mode | eager uniquement | eager ou lazy | lazy (par défaut) |
| Parallélisme | non (mono-thread) | oui, auto (multi-thread) | oui, scalable |
| RAM | en mémoire | très efficace | support out-of-core |

---

## 💡 Exemples avancés :

### Grouper et calculer moyenne par mois :

**Pandas**
```python
df["mois"] = df["date"].dt.month
df.groupby("mois")["montant"].mean()
```

**Polars**
```python
df = df.with_columns(pl.col("date").dt.month().alias("mois"))
df.groupby("mois").agg(pl.mean("montant"))
```

**Dask**
```python
df["mois"] = df["date"].dt.month
df.groupby("mois")["montant"].mean().compute()
```

---

## 🧠 À montrer en démo :
- Utiliser `timeit` pour mesurer les temps d’exécution
- Montrer `.lazy()` avec Polars pour chaîner les opérations
- Montrer qu’avec Dask, on peut traiter un fichier de 10Go sans planter