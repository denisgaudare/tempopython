# ✅ Miniprojet Vide Flights 
## 🛫 Données de base

**Extraits types utilisés :**

```python
python generate_data.py
```

```python
import pandas as pd

airports = pd.read_csv("airports.csv")
flights = pd.read_csv("flights.csv", parse_dates=["date"])
```

---

## 📌 1. Visualisation simple : retards moyens par aéroport (bar chart)

```python
import matplotlib.pyplot as plt

# Moyenne des retards à l’arrivée par aéroport de destination
avg_delay = flights.groupby("destination")["delay_min"].mean().sort_values(ascending=False)

plt.figure(figsize=(10, 5))
plt.title("Retard moyen par aéroport de destination")
# TODO A VOUS DE COMPLETER
plt.show()
```

---

## 📌 2. Scatter Plot : position géographique des aéroports

```python
plt.figure(figsize=(12, 6))
plt.title("Position géographique des aéroports")
# TODO A VOUS DE COMPLETER
plt.show()
```

> 🌍 Peut être enrichi avec un fond de carte `Basemap` ou `Cartopy` si besoin.

---

## 📌 3. Évolution temporelle des retards (Line Plot)

```python
# Moyenne des retards par jour
daily_delay = # TODO A VOUS DE CALCULER

plt.figure(figsize=(10, 4))
# TODO A VOUS DE COMPLETER
plt.tight_layout()
plt.show()
```

---

## 📌 4. Heatmap des retards par jour de la semaine et aéroport

```python
import numpy as np

flights["day_of_week"] = flights["date"].dt.day_name()
# TODO CREER UNE HEATMAP DES RETARD PAR JOUR DE LA SEMAINE
plt.title("Retards moyens par jour et destination")
plt.colorbar(heatmap, label="Retard (min)")
plt.tight_layout()
plt.show()
```

---

## 📌 5. Multiple Subplots : retards par compagnie et par jour

```python
airlines = flights["airline"].unique()
fig, axs = plt.subplots(len(airlines), 1, figsize=(10, 2 * len(airlines)), sharex=True)

for i, airline in enumerate(airlines):
      # TODO CALCULER ET DESSINER PAR AIRLINE
 
plt.xlabel("Date")
plt.tight_layout()
plt.show()
```

---

## 📌 6. Visualisation géographique des routes les plus fréquentes

```python
top_routes = flights.groupby(["origin", "destination"]).size().sort_values(ascending=False).head(10)
top_routes = top_routes.reset_index(name="count")

# TODO Merge pour avoir lat/lon
 
plt.figure(figsize=(12, 6))
for _, row in routes.iterrows():
    # TODO : TRACER UNE LIGNE QUI REPRESENTE LA ROUTE

# TODO : Completer pour l'affichage
# par exemple les titres des axes & une grid
plt.show()
```
