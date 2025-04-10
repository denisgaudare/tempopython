
# ✅ Corrigé des exercices Polars

> Tous les exercices supposent que le fichier `flights.csv` est bien structuré avec les colonnes :  
> `flight_id, airline, origin, destination, date, delay`

```python
import polars as pl
```

---

### 🔍 Exercice 1 – Filtrage de vols retardés

**Objectif** : Sélectionner tous les vols avec un retard > 60 minutes.

```python
df = pl.read_csv("flights.csv")

retards = df.filter(pl.col("delay") > 60)
print(retards.head())
```

---

### 🧮 Exercice 2 – Moyenne des retards par compagnie

**Objectif** : Calculer le retard moyen (`avg_delay`) pour chaque `airline`.

```python
retards_moyens = (
    df.groupby("airline")
      .agg(pl.mean("delay").alias("avg_delay"))
      .sort("avg_delay", descending=True)
)
print(retards_moyens)
```

---

### 🛫 Exercice 3 – Vols CDG → JFK après le 1er janvier 2024

**Objectif** : Filtrer les vols `CDG → JFK` après le 1er janvier 2024.

```python
df = df.with_columns(
    pl.col("date").str.strptime(pl.Date, fmt="%Y-%m-%d")
)

vols_selection = df.filter(
    (pl.col("origin") == "CDG") &
    (pl.col("destination") == "JFK") &
    (pl.col("date") > pl.Date("2024-01-01"))
)

print(vols_selection.head())
```

---

### 🔁 Exercice 4 – Fusionner avec une table compagnies

**Fichier externe** : `airlines.csv`
```csv
airline,country
Air France,France
Lufthansa,Allemagne
Delta,USA
...
```

**Solution** :

```python
df_airlines = pl.read_csv("airlines.csv")

df_joined = df.join(df_airlines, on="airline", how="left")
print(df_joined.head())
```

---

### 📦 Exercice 5 – Lecture / écriture Parquet

#### 1. Écriture des vols retardés (> 30 min)
```python
df_delays = df.filter(pl.col("delay") > 30)
df_delays.write_parquet("delayed_flights.parquet")
```

#### 2. Lecture depuis fichier Parquet
```python
df_parquet = pl.read_parquet("delayed_flights.parquet")
print(df_parquet.head())
```

---

### 🧠 Bonus – Lazy mode : top 5 compagnies les plus retardées

```python
lazy_df = pl.read_csv("flights.csv").lazy()

top_5 = (
    lazy_df
    .filter(pl.col("delay") > 15)
    .groupby("airline")
    .agg(pl.col("delay").mean().alias("avg_delay"))
    .sort("avg_delay", descending=True)
    .limit(5)
    .collect()
)

print(top_5)
```

---
