import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime, timedelta
import random
import os

fake = Faker()
n_rows_per_file = 100_000  # taille d'une partition
n_files = 10  # total = 1 million de lignes
categories = ["Électronique", "Vêtements", "Maison", "Jeux", "Livres"]
start_date = datetime(2023, 1, 1)

output_dir = "/mnt/data/big_transactions/"
os.makedirs(output_dir, exist_ok=True)

for file_index in range(n_files):
    data = []
    for i in range(n_rows_per_file):
        data.append({
            "transaction_id": f"T{file_index}_{i:07d}",
            "client": fake.name(),
            "date": start_date + timedelta(days=random.randint(0, 365)),
            "categorie": random.choice(categories),
            "montant": round(random.uniform(10, 1000), 2)
        })

    df = pd.DataFrame(data)
    df.to_csv(f"{output_dir}/part_{file_index:02d}.csv", index=False)
