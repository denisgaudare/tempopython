"""
🎯 **Objectif**
Comparer les **fonctions et manipulations courantes** entre :
- 🐼 **Pandas** (référence historique)
- 🐻‍❄️ **Polars** (ultra rapide, lazy/eager)
- 🧱 **Dask** (parallélisé, out-of-core)
"""

#📦 Préparation : installation
# pip install pandas polars dask
tr_file = "transactions_sample.csv"
#🧪 Exemple de dataset commun (fichier CSV `transactions_sample.csv`)
# Pour Pandas

import pandas as pd
df_pd = pd.read_csv(tr_file, parse_dates=["date"])

# Pour Polars
import polars as pl
df_pl = pl.read_csv(tr_file, try_parse_dates=True)

# Pour Dask
import dask.dataframe as dd
df_dask = dd.read_csv(tr_file, parse_dates=["date"])

## 📋 Comparatif des opérations de base
# **Filtrer une valeur**
df_pd[df_pd["montant"] > 100]
df_pl.filter(pl.col("montant") > 100)
df_dask[df_dask["montant"] > 100].compute()

# **GroupBy somme**
df_pd.groupby("categorie")["montant"].sum()
#df_pl.groupby("categorie").agg("montant")
df_dask.groupby("categorie")["montant"].sum().compute()

# **Ajouter colonne calculée**
df_pd["tva"] = df_pd["montant"] * 0.2
df_pl = df_pl.with_columns((pl.col("montant") * 0.2).alias("tva"))
df_dask["tva"] = (df_dask["montant"]  * 0.2).compute()

# **Tri**
df_pd.sort_values("montant", ascending=False)
df_pl.sort("montant", descending=True)
df_dask.sort_values("montant", ascending=False).compute()

# **Dates (mois)**
df_pd["mois"] = df_pd["date"].dt.month
df_pl = df_pl.with_columns(pl.col("date").dt.month().alias("mois"))
df_dask["mois"] = df_dask["date"].dt.month

"""
## ⚡ Benchmarks (facultatif en démo)
- Sur gros fichiers CSV (1M lignes+), Polars est souvent 3-10x plus rapide que Pandas.
- Dask peut traiter des fichiers plus gros que la RAM, mais requiert `.compute()`.
"""
## 📎 Notes pédagogiques :
## 💡 Exemples avancés :
### Grouper et calculer moyenne par mois :
# **Pandas** **Polars** **Dask**
df_pd["mois"] = df_pd["date"].dt.month
df_pd.groupby("mois")["montant"].mean()

df_pl = df_pl.with_columns(pl.col("date").dt.month().alias("mois"))
df_pl.group_by("mois").agg(pl.mean("montant"))

df_dask["mois"] = df_pd["date"].dt.month
df_dask.groupby("mois")["montant"].mean().compute()
