import pandas as pd
import glob

def process_flights_pandas(path="data/flights_*.csv"):
    files = glob.glob(path)
    df = pd.concat([pd.read_csv(f) for f in files])

    # Filtrer les vols retardés
    df = df[df["delay"] > 15]

    # Retard moyen par compagnie
    grouped = df.groupby("airline")["delay"].mean().reset_index()
    return grouped


