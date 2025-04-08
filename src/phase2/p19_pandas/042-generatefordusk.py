import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime, timedelta
import random

fake = Faker()

# Nombre de lignes à générer (modifiable)
n_rows = 100  # changez à 1_000_000 pour un gros fichier

# Catégories pour les produits
categories = ["Électronique", "Vêtements", "Maison", "Jeux", "Livres"]

# Génération des données
data = []

start_date = datetime(2023, 1, 1)

for i in range(n_rows):
    data.append({
        "transaction_id": f"T{i+1:08d}",
        "client": fake.name(),
        "date": start_date + timedelta(days=random.randint(0, 365)),
        "categorie": random.choice(categories),
        "montant": round(random.uniform(10, 1000), 2)
    })

# Convertir en DataFrame Pandas
df = pd.DataFrame(data)

# Enregistrer en CSV pour Dask
csv_path = "/mnt/data/transactions_dask_ready.csv"
df.to_csv(csv_path, index=False)

csv_path
