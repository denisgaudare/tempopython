import datetime
import json
import os
import random

from faker import Faker

base_dir = "physijson_complete/data"
os.makedirs(base_dir, exist_ok=True)

# Génération d'un fichier NDJSON factice
faker = Faker()
domains = ["optics", "mechanics", "quantum", "thermo"]
formulas = {
    "optics": "E = h * f",
    "mechanics": "F = m * a",
    "quantum": "ΔE = h * ν",
    "thermo": "Q = m * c * ΔT"
}

ndjson_data = []
for i in range(200):
    domain = random.choice(domains)
    formula = formulas[domain]
    freq = random.uniform(1e14, 1e15)
    results = [
        {
            "x": freq,
            "y": freq * 6.626e-34,
            "error": random.uniform(1e-22, 1e-20)
        }
    ]
    record = {
        "id": f"exp{(i+1):03}",
        "domain": domain,
        "formula": formula,
        "parameters": {"f": [freq]},
        "results": results,
        "metadata": {
            "author": faker.name(),
            "timestamp": datetime.datetime.now().isoformat()
        }
    }
    ndjson_data.append(record)

ndjson_path = os.path.join(base_dir, "experiments.ndjson")
with open(ndjson_path, "w") as f:
    for line in ndjson_data:
        f.write(json.dumps(line) + "\n")
