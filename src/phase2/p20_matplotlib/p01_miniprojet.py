# ✅ Miniprojet Flights
import pandas as pd

from commontools.consoles import pause

airports = pd.read_csv("airports.csv")
flights = pd.read_csv("flights.csv", parse_dates=["date"])

## 📌 1. Visualisation simple : retards moyens par aéroport (bar chart)

import matplotlib.pyplot as plt

# Moyenne des retards à l’arrivée par aéroport de destination
avg_delay = flights.groupby("destination")["delay_min"].mean().sort_values(ascending=False)

plt.figure(figsize=(10, 5))
plt.bar(avg_delay.index, avg_delay.values)
plt.title("Retard moyen par aéroport de destination")
plt.xlabel("Aéroport (code IATA)")
plt.ylabel("Retard moyen (min)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("flight_avg.png")
pause()

## 📌 2. Scatter Plot : position géographique des aéroports

plt.figure(figsize=(12, 6))
plt.scatter(airports["longitude"], airports["latitude"], alpha=0.6)
plt.title("Position géographique des aéroports")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.grid(True)
plt.show()
pause()

## 📌 2. Scatter Plot +6: Avec un Worldmap

import cartopy.crs as ccrs
import cartopy.feature as cfeature

fig = plt.figure(figsize=(14, 7))
ax = plt.axes(projection=ccrs.PlateCarree())

# Ajouter une carte de fond avec détails
ax.stock_img()
ax.coastlines()
ax.add_feature(cfeature.BORDERS)

# Tracer les aéroports
ax.scatter(airports["longitude"], airports["latitude"], color='red', s=10, alpha=0.6, transform=ccrs.PlateCarree())

plt.title("Carte des aéroports avec Cartopy")
plt.show()
pause()

# 🌍 Peut être enrichi avec un fond de carte
# `Basemap` ou `Cartopy` si besoin.

## 📌 3. Évolution temporelle des retards (Line Plot)
# Moyenne des retards par jour
daily_delay = flights.groupby("date")["delay_min"].mean()

plt.figure(figsize=(10, 4))
plt.plot(daily_delay.index, daily_delay.values, linestyle='-', marker='o')
plt.title("Évolution des retards quotidiens")
plt.xlabel("Date")
plt.ylabel("Retard moyen (min)")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()
pause()

## 📌 4. Heatmap des retards par jour de la semaine et aéroport

import numpy as np

flights["day_of_week"] = flights["date"].dt.day_name()

pivot = flights.pivot_table(index="day_of_week", columns="destination", values="delay_min", aggfunc="mean")
pivot = pivot.reindex(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])

fig, ax = plt.subplots(figsize=(12, 5))
heatmap = ax.imshow(pivot.values, cmap="coolwarm", aspect="auto")

ax.set_xticks(np.arange(len(pivot.columns)))
ax.set_xticklabels(pivot.columns, rotation=45)
ax.set_yticks(np.arange(len(pivot.index)))
ax.set_yticklabels(pivot.index)

plt.title("Retards moyens par jour et destination")
plt.colorbar(heatmap, label="Retard (min)")
plt.tight_layout()
plt.show()
pause()

## 📌 5. Multiple Subplots : retards par compagnie et par jour
airlines = flights["airline"].unique()
fig, axs = plt.subplots(len(airlines), 1, figsize=(10, 2 * len(airlines)), sharex=True)

for i, airline in enumerate(airlines):
    sub = flights[flights["airline"] == airline]
    grouped = sub.groupby("date")["delay_min"].mean()
    axs[i].plot(grouped.index, grouped.values)
    axs[i].set_title(f"{airline}")
    axs[i].set_ylabel("Retard (min)")

plt.xlabel("Date")
plt.tight_layout()
plt.show()
pause()

## 📌 6. Visualisation géographique des routes les plus fréquentes
top_routes = flights.groupby(["origin", "destination"]).size().sort_values(ascending=False).head(10)
top_routes = top_routes.reset_index(name="count")

# Merge pour avoir lat/lon
routes = top_routes.merge(airports, left_on="origin", right_on="iata").rename(columns={"latitude": "lat_o", "longitude": "lon_o"})
routes = routes.merge(airports, left_on="destination", right_on="iata").rename(columns={"latitude": "lat_d", "longitude": "lon_d"})

plt.figure(figsize=(12, 6))
for _, row in routes.iterrows():
    plt.plot([row["lon_o"], row["lon_d"]], [row["lat_o"], row["lat_d"]], linewidth=row["count"]/5, alpha=0.6)

plt.title("Top 10 routes aériennes les plus fréquentes")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.grid(True)
plt.show()
pause()

# Nettoyage et conversion
flights = flights.dropna(subset=["scheduled_departure", "departure_delay", "distance"])
flights["scheduled_hour"] = pd.to_datetime(flights["scheduled_departure"]).dt.hour

# Échantillon pour ne pas surcharger le plot
sample = flights.sample(1000, random_state=42)

# Création du graph 3D
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

x = sample["scheduled_hour"]
y = sample["departure_delay"]
z = sample["distance"]

sc = ax.scatter(x, y, z, c=y, cmap='coolwarm', alpha=0.7)

ax.set_xlabel('Heure prévue de départ')
ax.set_ylabel('Retard au départ (min)')
ax.set_zlabel('Distance (km)')
ax.set_title('Départ vs Retard vs Distance')

fig.colorbar(sc, ax=ax, label='Retard (min)')

plt.show()
pause()