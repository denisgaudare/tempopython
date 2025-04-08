import pandas as pd
from faker import Faker
from datetime import datetime, timedelta
import random

fake = Faker()

# Générer un petit dataset simulé de big_transactions
n_rows = 100_000
csv_path = "transactions_sample2.csv"

data = []

categories = ["Électronique", "Vêtements", "Maison", "Jeux", "Livres"]

start_date = datetime(2023, 1, 1)

for i in range(n_rows):
    data.append({
        "transaction_id": f"T{i+1:04d}",
        "client": fake.name(),
        "date": start_date + timedelta(days=random.randint(0, 180)),
        "categorie": random.choice(categories),
        "montant": round(random.uniform(10, 500), 2)
    })

df = pd.DataFrame(data)
df["date"] = pd.to_datetime(df["date"])

# Sauvegarder en CSV
df.to_csv(csv_path, index=False)