# Création du script Python complet
import pandas as pd
import matplotlib.pyplot as plt
from distances import karney_distance

TODO = None

from commontools.consoles import pause

# Chargement des données (avec pandas)
flights = TODO
airports = TODO

# Nettoyage : vérification des données manquantes
print("Données manquantes dans flights:")
print(TODO)
print("Données manquantes dans airports:")
print(TODO)

pause()

# RECUPERER LES COLONNES NULLES
null_columns=TODO
print(TODO)

pause()

#all nulls : AFFICHER TOUS LES LIGNES NULLES
print(flights[flights.isnull().any(axis=1)][null_columns].head())
pause()

# Enrichissement : ajout des coordonnées des aéroports
# pour l'aeroport d'origine et celui de destination
flights = flights.merge(
    airports.add_prefix("origin_")
    ...TODO
)
flights = flights.merge(
    airports.add_prefix("dest_"),
    ...TODO
)

# ON fait le point sur les infos du Dataframe
flights.info()

# Transformation : calcul des retards en minutes
# Attention à diviser par 60
flights["delay_minutes"] = TODO

# Calcul des distances entre aeroports
# appliquer une conversion pour ajouter une colonne

flights['distance'] = flights.apply(
    lambda row: karney_distance(row['origin_latitude'],
                    row['origin_longitude'],
                    row['dest_latitude'],
                    row['dest_longitude']),
    axis=1
)

# Agrégation : nombre de vols par jour
flights["departure_date"] = TODO
daily_flights = TODO

# Affichage
print("Nombre de vols par jour :")
print(daily_flights)

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