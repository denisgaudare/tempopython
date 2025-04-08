# Projet complet **Pandas + NumPy**, 
# qui part du modèle de vols (`flights`) 

On va :
- Générer les données (comme précédemment),
- Charger dans un `DataFrame`,
- Appliquer un maximum de **concepts Pandas et NumPy** : types, filtres, groupby, pivot, interpolation, manipulation de dates, statistiques, etc.

---

## ✈️ Projet : Analyse et interpolation de données de vols avec Pandas & NumPy

### 🔧 Étape 1 : Génération des données

```python
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

airports = ['CDG', 'JFK', 'LHR', 'FRA', 'AMS', 'DXB', 'MAD', 'ORD', 'LAX', 'SIN']
airlines = ['AF', 'LH', 'BA', 'KL', 'EK', 'IB', 'UA', 'AA', 'SQ', 'DL']

def generate_flight_data(n=200):
    data = []
    now = datetime.now()
    for _ in range(n):
        airline = random.choice(airlines)
        flight_number = f"{airline}{random.randint(100, 9999)}"
        departure = random.choice(airports)
        arrival = random.choice([a for a in airports if a != departure])
        date = now + timedelta(days=random.randint(-10, 10))
        delay_minutes = np.random.choice([0, 10, 30, 60, np.nan], p=[0.6, 0.2, 0.1, 0.05, 0.05])
        duration = random.randint(90, 600)
        price = np.random.normal(loc=300, scale=75)
        data.append({
            "flight_number": flight_number,
            "airline": airline,
            "departure": departure,
            "arrival": arrival,
            "date": date.date(),
            "duration_min": duration,
            "delay_min": delay_minutes,
            "price_eur": round(price, 2)
        })
    return pd.DataFrame(data)

df = generate_flight_data()
```

---

### 🔍 Étape 2 : Exploration & nettoyage

```python
print(df.head())
print(df.dtypes)
print(df.isnull().sum())  # Détection des NaN
```

- Convertir `date` en datetime (si pas déjà) :
```python
df['date'] = pd.to_datetime(df['date'])
```

---

### 🧼 Étape 3 : Interpolation et traitement des valeurs manquantes

```python
# Impute les valeurs manquantes des retards par interpolation linéaire
df['delay_min_interp'] = df['delay_min'].interpolate()

# Si des NaN persistent au début/fin : on les remplace par la moyenne
df['delay_min_interp'].fillna(df['delay_min_interp'].mean(), inplace=True)
```

---

### 📊 Étape 4 : GroupBy, agrégation, pivot

```python
# Moyenne de prix et durée par compagnie
stats = df.groupby('airline')[['price_eur', 'duration_min']].agg(['mean', 'std', 'count'])
print(stats)

# Pivot table : prix moyen par date et compagnie
pivot = df.pivot_table(values='price_eur', index='date', columns='airline', aggfunc='mean')
print(pivot.tail())
```

---

### ⏱️ Étape 5 : Création de colonnes dérivées et logique NumPy

```python
# Catégoriser les vols par durée
df['duration_category'] = pd.cut(df['duration_min'], bins=[0, 180, 300, np.inf], labels=['court', 'moyen', 'long'])

# Détection des vols très chers (> 500€) avec NumPy
df['is_expensive'] = np.where(df['price_eur'] > 500, True, False)

# Retard "normalisé" par rapport à la durée
df['delay_ratio'] = df['delay_min_interp'] / df['duration_min']
```

---

### 📈 Étape 6 : Visualisation rapide

```python
import matplotlib.pyplot as plt

# Histogramme des prix
df['price_eur'].hist(bins=30)
plt.title("Distribution des prix")
plt.xlabel("Prix (€)")
plt.ylabel("Fréquence")
plt.show()

# Moyenne des retards par aéroport de départ
df.groupby("departure")["delay_min_interp"].mean().plot(kind="bar")
plt.title("Retard moyen par aéroport de départ")
plt.ylabel("Minutes")
plt.show()
```

---

### 🧠 Concepts abordés

| Concept                     | Utilisé dans                                  |
|----------------------------|-----------------------------------------------|
| `DataFrame`, `Series`      | Manipulation principale                       |
| Types datetime             | `pd.to_datetime`, filtres par date            |
| Valeurs manquantes         | `isnull()`, `interpolate()`, `fillna()`       |
| GroupBy / Aggregation      | `groupby().agg()`                             |
| Pivot tables               | `pivot_table()`                               |
| Binning / Categ.           | `pd.cut()`                                    |
| Conditions NumPy           | `np.where()`                                  |
| Graphiques                 | `matplotlib.pyplot`                           |
| Ratio, logique dérivée     | colonnes personnalisées                       |

---
