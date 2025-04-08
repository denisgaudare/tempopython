# Création du script Python complet
import pandas as pd
import matplotlib.pyplot as plt

from commontools.consoles import pause
from phase2.p10_concurrency.calculs import karney_distance

# Chargement des données
flights = pd.read_csv("flights.csv",
                      parse_dates=["departure_time", "scheduled_arrival_time", "arrival_time"])
airports = pd.read_csv("airports.csv")

# Nettoyage : vérification des données manquantes
print("Données manquantes dans flights:")
print(flights.isnull().sum())
print("\nDonnées manquantes dans airports:")
print(airports.isnull().sum())
pause()

# details des lignes nulles
null_columns=flights.columns[flights.isnull().any()]
print(flights[flights["flight_id"].isnull()][null_columns])
pause()

#all nulls
print(flights[flights.isnull().any(axis=1)][null_columns].head())
pause()

# Enrichissement : ajout des coordonnées des aéroports
flights = flights.merge(
    airports.add_prefix("origin_"),
    left_on="origin_airport",
    right_on="origin_airport_code",
    how="left"
)
flights = flights.merge(
    airports.add_prefix("dest_"),
    left_on="destination_airport",
    right_on="dest_airport_code",
    how="left"
)

flights.info()
pause()

# Transformation : calcul des retards en minutes
d = (flights["arrival_time"] - flights["scheduled_arrival_time"])
flights["delay_minutes"] = (flights["arrival_time"] - flights["scheduled_arrival_time"]).dt.total_seconds() / 60

# Calcul des distances entre aeroports
# appliquer une conversion pour ajouter une colonne
pause()
flights['distance'] = flights.apply(
    lambda row: karney_distance(row['origin_latitude'],
                    row['origin_longitude'],
                    row['dest_latitude'],
                    row['dest_longitude']),
    axis=1
)


# Agrégation : nombre de vols par jour
flights["departure_date"] = flights["departure_time"].dt.date
daily_flights = flights.groupby("departure_date").size()

# Affichage
print("\nNombre de vols par jour :")
print(daily_flights)
pause()

# Retard moyen par aéroport de destination
avg_delay = flights.groupby("destination_airport")["delay_minutes"].mean()
print("\nRetard moyen par aéroport de destination :")
print(avg_delay)

# Visualisation : histogramme du nombre de vols par heure
flights["hour"] = flights["departure_time"].dt.hour
flights["hour"].value_counts().sort_index().plot(kind="bar", figsize=(10, 5), title="Nombre de vols par heure")
plt.xlabel("Heure de départ")
plt.ylabel("Nombre de vols")
plt.tight_layout()
plt.savefig("vols_par_heure.png")
plt.show()


# save to json file
from json import loads, dump
result = flights.to_json(orient="split")
parsed = loads(result)
with open("flights_full.json","w") as jfile:
    dump(parsed, jfile, indent=4)

print("fin")