# 🧪 Exercices pratiques Polars – Niveau intermédiaire

## 📁 Données de base : `flights.csv`

Colonnes :
```
flight_id, airline, origin, destination, date, delay
```

---

### 🔍 Exercice 1 – Filtrage de vols retardés

**Objectif** : Sélectionner tous les vols avec un retard > 60 minutes.

```python
# Résultat attendu : DataFrame avec uniquement les vols retardés fortement
# Colonnes : flight_id, delay

import polars as pl
df = pl.read_csv("flights.csv")

retards = ...
```

💡 *Indice* :
```python
df.filter(pl.col("delay") > 60)
```

---

### 🧮 Exercice 2 – Moyenne des retards par compagnie

**Objectif** : Calculer le retard moyen (`avg_delay`) pour chaque `airline`, trié par ordre décroissant.

```python
delais = (
    df
    .groupby(...)
    .agg(...)
    .sort(...)
)
```

💡 *Utilise* `pl.mean("delay")`, `.agg()`, `.sort()`

---

### 🛫 Exercice 3 – Vols Paris → New York après 2024-01-01

**Objectif** : Extraire tous les vols `CDG → JFK` après le 1er janvier 2024.

```python
result = df.filter(
    ...
)
```

💡 *Indice* : il faut convertir `"date"` en format datetime avec `.str.strptime(pl.Date)`

---

### 🔁 Exercice 4 – Fusionner avec une table compagnies

**Données supplémentaires** : `airlines.csv`  
```
airline, country
```

**Objectif** : Joindre ce fichier à `flights.csv` pour enrichir les données avec le pays de chaque compagnie.

```python
df_airlines = pl.read_csv("airlines.csv")
df_joined = df.join(...)
```

💡 *Méthode* : `.join(df2, on="airline", how="left")`

---

### 📦 Exercice 5 – Lecture / écriture Parquet

**Objectif** :
1. Écrire les vols filtrés vers un fichier `delayed_flights.parquet`
2. Lire ce fichier avec Polars

```python
# 1.
delays = df.filter(pl.col("delay") > 30)
...

# 2.
df_parquet = ...
```

💡 *Méthodes* :
```python
df.write_parquet("file.parquet")
pl.read_parquet("file.parquet")
```

---

### 🧠 Bonus – Lazy mode : top 5 compagnies les plus retardées

```python
lazy_df = pl.read_csv("flights.csv").lazy()

result = (
    lazy_df
    .filter(pl.col("delay") > 15)
    .groupby("airline")
    .agg(pl.mean("delay").alias("avg_delay"))
    .sort("avg_delay", descending=True)
    .limit(5)
    .collect()
)
```

---
