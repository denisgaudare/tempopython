import csv
import random
from faker import Faker

# Initialisation de Faker
fake = Faker()

AIRPORT_CODES = ("CDG","JFK","HND","DXB","SIN","LHR","FRA")

# Génération de N avions
def generate_aircraft_data(n, filename="../data/flights.csv"):
    """
    Génère un fichier CSV avec des avions fi&ctifs.

    :param n: Nombre d'avions à générer
    :param filename: Nom du fichier de sortie (par défaut 'flights.csv')
    """
    # Définition des noms de colonnes
    fieldnames = ["flight_name", "capacity", "fuel", "airline", "manufacture_year", "range_km", "status","origin","destination"]

    # États possibles des avions
    status_choices = ["active", "maintenance", "retired"]

    # Ouverture du fichier CSV en mode écriture
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL)
        writer.writeheader()

        for _ in range(n):
            # Génération de données aléatoires
            flight_name = fake.bothify(text="FL#####")
            capacity = random.randint(100, 400)  # Capacité entre 100 et 400 passagers
            fuel = round(random.uniform(10, 100), 2)  # Niveau de carburant entre 10 et 100%
            airline = fake.company() + " Airlines"  # Nom de la compagnie
            manufacture_year = random.randint(1990, 2025)  # Année de fabrication entre 1990 et 2025
            range_km = random.randint(2000, 15000)  # Autonomie en kilomètres
            status = random.choice(status_choices)  # État de l'avion

            origin, destination = random.sample(AIRPORT_CODES, 2)

            # Écriture des données dans le fichier CSV
            writer.writerow({
                "flight_name": flight_name,
                "capacity": capacity,
                "fuel": fuel,
                "airline": airline,
                "manufacture_year": manufacture_year,
                "range_km": range_km,
                "status": status,
                "origin": origin,
                "destination": destination
            })

    print(f"Fichier CSV '{filename}' généré avec {n} avions.")


# Exemple d'utilisation
generate_aircraft_data(100000)  # Génère un fichier CSV avec 10 avions
