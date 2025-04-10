# --- 1. Génération de données factices volumineuses ---
import pandas as pd
import numpy as np
import os

# Paramètres de simulation
nb_files = 5
rows_per_file = 500_000
folder = "flights_data"
os.makedirs(folder, exist_ok=True)

# Génération de fichiers CSV
for i in range(nb_files):
    df = pd.DataFrame({
        "flight_id": range(i * rows_per_file, (i + 1) * rows_per_file),
        "origin": np.random.choice(["JFK", "LAX", "ORD", "ATL", "DFW"], size=rows_per_file),
        "destination": np.random.choice(["SFO", "MIA", "SEA", "BOS", "PHX"], size=rows_per_file),
        "delay_min": np.random.normal(loc=15, scale=10, size=rows_per_file).astype(int),
        "airline": np.random.choice(["Delta", "United", "American", "Southwest"], size=rows_per_file)
    })
    df.to_csv(f"{folder}/flights_{i}.csv", index=False)

# --- 2. Traitement avec Pandas ---
import time
import glob

csv_files = glob.glob(f"{folder}/flights_*.csv")

start = time.time()
df_all = pd.concat([pd.read_csv(f) for f in csv_files])
result_pandas = df_all.groupby("airline")["delay_min"].mean().reset_index()
duration_pandas = time.time() - start

print("\n--- Pandas ---")
print(result_pandas)
print(f"Durée : {duration_pandas:.2f}s")

# --- 3. Traitement avec DuckDB ---
import duckdb

start = time.time()
result_duckdb = duckdb.query(f'''
    SELECT airline, AVG(delay_min) AS avg_delay
    FROM read_csv_auto('{folder}/flights_*.csv')
    GROUP BY airline
    ORDER BY airline
''').to_df()
duration_duckdb = time.time() - start

print("\n--- DuckDB ---")
print(result_duckdb)
print(f"Durée : {duration_duckdb:.2f}s")
