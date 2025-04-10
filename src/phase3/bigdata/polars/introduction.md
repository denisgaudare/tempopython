# 🦾 **Introduction à Polars**  
*Une alternative moderne à Pandas, boostée par Rust*

---

## 📚 1. Pourquoi Polars ?  

### ⚙️ Limitations de Pandas :
- Monothread (soumis au GIL)
- Consommation mémoire importante
- Performance parfois décevante sur gros volumes
- Pas de lazy evaluation

### 🚀 Polars, c’est :
- Écrit en **Rust** → ultra-performant
- **Multithread** par défaut
- Évaluation **lazy** possible (comme Spark)
- API Python inspirée de Pandas + SQL-like
- Compatibilité avec Arrow / Parquet

---

## 🧰 2. Installation

```bash
pip install polars
```

Optionnel :
```bash
pip install pyarrow
```

---

## 🔤 3. Syntaxe de base vs Pandas

### 📄 Création de DataFrame

```python
import polars as pl

df = pl.DataFrame({
    "name": ["Alice", "Bob"],
    "age": [25, 32],
})
```

### 🔎 Sélection de colonnes

```python
df["age"]           # Serie
df.select("name")   # DataFrame
df.select(["age", "name"])
```

### 📊 Filtres

```python
df.filter(pl.col("age") > 30)
```

### 🔁 GroupBy

```python
df.groupby("name").agg(pl.col("age").mean())
```

---

## 🧠 4. Lazy vs Eager

### ⚡ Eager (par défaut)
Comme Pandas : chaque opération exécute immédiatement.

```python
df = pl.read_csv("flights.csv")
df.filter(pl.col("delay") > 15).select("airline")
```

### 💤 Lazy (optimisé avant exécution)

```python
lazy_df = pl.read_csv("flights.csv").lazy()
result = (
    lazy_df
    .filter(pl.col("delay") > 15)
    .groupby("airline")
    .agg(pl.mean("delay"))
    .sort("delay", descending=True)
    .collect()  # ⚠️ ne calcule qu'ici
)
```

Avantages :
- Optimisations automatiques : projection pushdown, filtre pushdown, etc.
- Exécution en un seul plan de calcul

---

## ⚡ 5. Comparatif de perfs (vs Pandas)

| Opération         | Pandas (1M rows) | Polars eager | Polars lazy |
|-------------------|------------------|--------------|-------------|
| CSV load          | ~1.2s            | ~0.4s        | ~0.4s       |
| GroupBy + Mean    | ~0.7s            | ~0.2s        | ~0.05s      |
| Filter + Sort     | ~0.5s            | ~0.1s        | ~0.03s      |
| RAM utilisée      | élevée           | basse        | basse       |

---

## 🧬 6. Comparaison API Pandas vs Polars

| Action                   | Pandas                             | Polars                               |
|--------------------------|------------------------------------|--------------------------------------|
| Sélection conditionnelle | `df[df["x"] > 0]`                  | `df.filter(pl.col("x") > 0)`         |
| GroupBy + agg            | `df.groupby("x")["y"].mean()`      | `df.groupby("x").agg(pl.mean("y"))`  |
| Renommage                | `df.rename(columns={"a": "b"})`    | `df.rename({"a": "b"})`              |
| Fusion (merge)           | `df.merge(df2, on="id")`           | `df.join(df2, on="id")`              |

---

## 📦 7. Polars & fichiers

- `pl.read_csv("file.csv")`
- `pl.read_parquet("data.parquet")`
- `df.write_csv("out.csv")`
- `df.write_parquet("out.parquet")`

Prise en charge native de :
- CSV / TSV
- Parquet
- IPC / Arrow

---

## 🧪 8. Interopérabilité

- Polars peut convertir vers Pandas : `df.to_pandas()`
- Ou depuis Pandas : `pl.from_pandas(df)`
- Compatible avec NumPy via `.to_numpy()`, `pl.Series("x", np_array)`

---

## 🧠 9. Cas d’usage idéaux

- Traitement de **très gros fichiers**
- Pipelines **data engineering**
- Scripts **multithread** sans effort
- Remplacer Spark localement pour jobs de transformation
- Traitement de logs, NDJSON, données tabulaires lourdes

---

## 📌 10. En résumé

| Tu veux...                                        | Utilise...     |
|--------------------------------------------------|----------------|
| Intégration facile avec SciPy, Matplotlib, etc.  | Pandas         |
| Performance + faible RAM + multi-thread          | Polars         |
| Pipelines scalables avec transformations         | Polars (lazy)  |
| Manipulation interactive en notebook             | Pandas ou Polars (eager) |

---
