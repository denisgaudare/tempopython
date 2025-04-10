import csv
import random
import os
from datetime import datetime, timedelta

# Configuration
rows_per_file = 200_000
output_dir = "data"
year = 2024
months = range(1, 13)  # Génère Janvier à Decembre

# Données simulées
airlines = ["Air France", "Lufthansa", "Delta", "KLM", "British Airways", "Emirates"]
airports = ["CDG", "JFK", "LHR", "FRA", "AMS", "DXB", "ATL", "LAX", "SIN", "NRT"]

os.makedirs(output_dir, exist_ok=True)

for month in months:
    filename = f"{output_dir}/flights_{year}_{month:02d}.csv"
    with open(filename, mode="w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["flight_id", "airline", "origin", "destination", "date", "delay"])

        for i in range(rows_per_file):
            flight_id = f"{month:02d}FL{i:06d}"
            airline = random.choice(airlines)
            origin, destination = random.sample(airports, 2)
            day = random.randint(1, 28)  # évite les problèmes de fin de mois
            date = datetime(year, month, day).strftime("%Y-%m-%d")
            delay = max(0, int(random.gauss(mu=10, sigma=20)))
            writer.writerow([flight_id, airline, origin, destination, date, delay])

    print(f"✅ Fichier généré : {filename}")
