import dask.dataframe as dd

# Chargement du fichier
df = dd.read_csv("transactions_dask_ready.csv", parse_dates=["date"])

# Filtrer les big_transactions > 500€
high_value = df[df["montant"] > 500]

# Moyenne par catégorie
mean_by_cat = df.groupby("categorie")["montant"].mean()

# Exécuter les calculs
print(high_value.head())
print(mean_by_cat.compute())
