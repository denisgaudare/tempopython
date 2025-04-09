import csv
import random

from projectaircraft import config

CODES = ["CDG", "JFK", "HND", "DXB", "SIN", "LHR", "FRA"]

# Matrice de base sans bruit
BASE_DISTANCES = {
    ("CDG", "JFK"): 5845, ("CDG", "HND"): 9713, ("CDG", "DXB"): 5245,
    ("CDG", "SIN"): 10732, ("CDG", "LHR"): 344,  ("CDG", "FRA"): 450,
    ("JFK", "HND"): 10872, ("JFK", "DXB"): 11000, ("JFK", "SIN"): 15340,
    ("JFK", "LHR"): 5567,  ("JFK", "FRA"): 6200,
    ("HND", "DXB"): 7935,  ("HND", "SIN"): 5310,  ("HND", "LHR"): 9564,
    ("HND", "FRA"): 9350,
    ("DXB", "SIN"): 5840,  ("DXB", "LHR"): 5500,  ("DXB", "FRA"): 4835,
    ("SIN", "LHR"): 10850, ("SIN", "FRA"): 10560,
    ("LHR", "FRA"): 640,
}

def apply_random_noise(km):
    variation = random.uniform(-0.03, 0.03)
    return round(km * (1 + variation), 1)

def generate_distance_file(filename):
    with open(filename, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["from", "to", "distance_km"])

        for code1 in CODES:
            for code2 in CODES:
                if code1 == code2:
                    dist = 0
                else:
                    base = BASE_DISTANCES.get((code1, code2)) or BASE_DISTANCES.get((code2, code1))
                    dist = apply_random_noise(base)
                writer.writerow([code1, code2, dist])

    print(f"✅ distances.csv généré avec variations aléatoires.")

# À appeler une seule fois pour générer le fichier :
generate_distance_file(config.DATA / "distances.csv")