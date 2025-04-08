import dask.dataframe as dd

# Chargement paresseux des fichiers CSV
df = dd.read_csv("/mnt/data/big_transactions/part_*.csv", parse_dates=["date"])

# Exemple : filtrer et agréger sans charger tout en mémoire
result = (
    df[df["montant"] > 500]
    .groupby("categorie")["montant"]
    .agg(["mean", "count"])
)

# Lancement du calcul distribué
print(result.compute())
