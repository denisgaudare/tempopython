**Polars + Arrow** : c’est **ultra rapide**, très bien adapté aux gros volumes, et super élégant à utiliser.

**mini-projet complet** basé sur le thème aviation (comme ton projet Aircrd), utilisant :

- 🔢 **Un jeu de données simulé** (flights)
- 📦 **Le format Arrow IPC** (`.arrow`)
- ⚡ **La librairie Polars** pour lecture, traitement, filtrage et agrégation
---
## ✅ Objectif du mini-projet

Créer un pipeline :

1. Générer un DataFrame de vols
2. Sauvegarder au format **Arrow IPC**
3. Recharger les données avec **Polars**
4. Faire des traitements :
   - vols par aéroport
   - durée moyenne par compagnie
   - filtres sur les vols longs

---

## 📁 Structure du projet

```
arrow_aircraft_project/
├── generate_data.py        # Génère les données et les écrit au format Arrow
├── process_data.py         # Lit les fichiers .arrow et les analyse avec Polars
└── data/
    └── flights.arrow       # Données Arrow
```

---

## 📦 1. Installation des dépendances

```bash
pip install polars pyarrow
```

---

## 🛠️ 2. generate_data.py — Génération des données + export en Arrow

```python
import pandas as pd
import pyarrow as pa
import pyarrow.ipc as ipc
import os
from datetime import datetime, timedelta
import random

# Génère des vols fictifs
def generate_flights(num=1000):
    airports = ["JFK", "CDG", "LHR", "LAX", "FRA", "DXB"]
    airlines = ["Delta", "Air France", "Lufthansa", "Emirates", "United", "British Airways"]
    
    data = []
    for i in range(num):
        origin = random.choice(airports)
        dest = random.choice([a for a in airports if a != origin])
        duration = random.randint(60, 600)
        date = datetime(2024, 3, 1) + timedelta(days=random.randint(0, 6))
        
        data.append({
            "flight_id": f"FL{i:04d}",
            "origin": origin,
            "destination": dest,
            "airline": random.choice(airlines),
            "departure_time": date.strftime("%Y-%m-%d"),
            "duration_minutes": duration
        })
    
    return pd.DataFrame(data)

# Crée le dossier data/
os.makedirs("data", exist_ok=True)

# Génère les données
df = generate_flights(1000)

# Conversion en Arrow Table
table = pa.Table.from_pandas(df)

# Sauvegarde en .arrow (IPC file)
with ipc.new_file("data/flights.arrow", table.schema) as writer:
    writer.write(table)

print("✅ Données générées et sauvegardées dans data/flights.arrow")
```

---

## 📊 3. process_data.py — Traitement des données avec **Polars**

```python
import polars as pl

# Lecture du fichier Arrow IPC
df = pl.read_ipc("data/flights.arrow")

# 1. Vols par aéroport d’origine
print("✈️ Vols par aéroport d’origine :")
print(df.groupby("origin").count())

# 2. Durée moyenne par compagnie
print("\n📊 Durée moyenne des vols par compagnie :")
print(df.groupby("airline").agg(pl.col("duration_minutes").mean().alias("avg_duration")))

# 3. Vols de plus de 5 heures (> 300 minutes)
print("\n🕔 Vols de plus de 5 heures :")
print(df.filter(pl.col("duration_minutes") > 300).select(["flight_id", "origin", "destination", "duration_minutes"]))

# 4. Moyenne par jour
print("\n📅 Moyenne de vols par jour :")
print(df.groupby("departure_time").count().sort("departure_time"))
```
---
## 🧪 Résultat attendu

```
✈️ Vols par aéroport d’origine :
shape: (6, 2)
┌────────┬───────┐
│ origin │ count │
├────────┼───────┤
│ JFK    │ 168   │
│ CDG    │ 154   │
...

📊 Durée moyenne des vols par compagnie :
shape: (6, 2)
┌────────────────────┬────────────┐
│ airline            │ avg_duration │
├────────────────────┼────────────┤
│ Delta              │ 325.7      │
│ Lufthansa          │ 278.3      │
...

🕔 Vols de plus de 5 heures :
shape: (X, 4)
┌──────────┬────────┬────────────┬────────────────┐
│ flight_id│ origin │ destination│ duration_minutes│
├──────────┼────────┼────────────┼────────────────┤
│ FL0001   │ JFK    │ DXB        │ 460            │
...

📅 Moyenne de vols par jour :
┌──────────────┬───────┐
│ departure_time │ count │
├──────────────┼───────┤
│ 2024-03-01    │ 140   │
│ 2024-03-02    │ 138   │
...
```

---

## 🧠 Pourquoi ce projet est cool

- ✅ Touche à **Arrow** (format ultra-performant pour l’interopérabilité)
- ✅ Utilise **Polars** pour des traitements super rapides
- ✅ Simule un vrai cas d’usage métier (vols par jour, analyse de compagnie)
- ✅ Extensible facilement (partitionnement, enrichissement avec `airports.csv`, etc.)
---
