import pandas as pd

# Chargement d’un DataFrame exemple
df = pd.read_csv("flights.csv", parse_dates=["departure_time"])

# PYARROW

# Écriture avec pyarrow + compression + colonnes sélectionnées
df.to_parquet(
    "flights.parquet",
    engine="pyarrow",
    compression="snappy",        # ou "gzip", "brotli", etc.
    columns=["flight_id", "origin", "destination", "departure_time"]
)



# Lecture uniquement de certaines colonnes
df_parquet = pd.read_parquet(
    "flights.parquet",
    engine="pyarrow", #engine="fastparquet", 
    columns=["flight_id", "departure_time"]
)

# Exemple de traitement : afficher les vols de plus de 5h
df_long = df[df["duration_minutes"] > 300]
print(df_long)


# Combiné multithread, multiprocess

import pandas as pd
import glob
from concurrent.futures import ThreadPoolExecutor

# Tous les fichiers Parquet à lire
files = glob.glob("data/flights_*.parquet")

# Fonction de lecture de fichier individuel
def read_parquet_file(file_path):
    return pd.read_parquet(file_path, engine="fastparquet")

# Lecture parallèle
with ThreadPoolExecutor(max_workers=4) as executor:
    dfs = list(executor.map(read_parquet_file, files))

# Fusion des résultats
df_combined = pd.concat(dfs, ignore_index=True)

print(df_combined.head())



from concurrent.futures import ProcessPoolExecutor

def process_file(file_path):
    df = pd.read_parquet(file_path, engine="fastparquet")
    # Exemple : ne garder que les vols > 5h
    return df[df["duration_minutes"] > 300]

with ProcessPoolExecutor(max_workers=4) as executor:
    dfs = list(executor.map(process_file, files))

df_filtered = pd.concat(dfs, ignore_index=True)

