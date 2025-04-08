import pandas as pd
import random
import numpy as np
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()
Faker.seed(42)
random.seed(42)
np.random.seed(42)

NUM_AIRPORTS = 100
NUM_FLIGHTS = 10000
START_DATE = datetime(2024, 1, 1)
END_DATE = datetime(2024, 3, 31)
AIRLINES = ["Delta", "United", "American", "Southwest", "JetBlue", "Alaska", "Spirit"]

# --- Génération des aéroports ---
iata_codes = set()
while len(iata_codes) < NUM_AIRPORTS:
    code = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=3))
    iata_codes.add(code)

airports = []
for i, code in enumerate(sorted(iata_codes)):
    airports.append({
        "airport_id": i + 1,
        "name": fake.city() + " Airport",
        "city": fake.city(),
        "country": fake.country(),
        "iata": code,
        "latitude": round(random.uniform(-60, 70), 6),
        "longitude": round(random.uniform(-180, 180), 6)
    })
airports_df = pd.DataFrame(airports)

# --- Génération des vols ---
date_range = pd.date_range(START_DATE, END_DATE)
flights = []

for flight_id in range(1, NUM_FLIGHTS + 1):
    origin, destination = random.sample(list(iata_codes), 2)
    date = random.choice(date_range)
    airline = random.choice(AIRLINES)

    # Génération réaliste des retards (biaisés vers 0)
    delay = max(0, int(np.random.normal(loc=10, scale=20)))  # moyenne 10 min, parfois plus

    flights.append({
        "flight_id": flight_id,
        "origin": origin,
        "destination": destination,
        "date": date.strftime('%Y-%m-%d'),
        "airline": airline,
        "delay_min": delay
    })

flights_df = pd.DataFrame(flights)

# --- Sauvegarde ---
airports_df.to_csv("airports.csv", index=False)
flights_df.to_csv("flights.csv", index=False)

print("Fichiers générés : airports.csv ({} aéroports), flights.csv ({} vols)".format(len(airports_df), len(flights_df)))
