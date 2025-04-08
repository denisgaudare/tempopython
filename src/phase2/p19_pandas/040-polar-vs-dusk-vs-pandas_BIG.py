"""
- Utiliser `timeit` pour mesurer les temps d’exécution
- Montrer `.lazy()` avec Polars pour chaîner les opérations
- Montrer qu’avec Dask, on peut traiter un fichier de 10Go sans planter
"""
import timeit

tr_file = "transactions_BIG.csv"

def phase_1():
    #📦 Préparation : installation
    #🧪 Exemple de BIG dataset

    # Pour Pandas
    import pandas as pd
    df_pd = pd.read_csv(tr_file)
    duree = timeit.timeit(lambda: [df_pd["montant"] > 100], number=100)
    print(duree)
    del df_pd

    # Pour Polars
    import polars as pl
    df_pl = pl.read_csv(tr_file)
    duree = timeit.timeit(lambda: df_pl.filter(pl.col("montant") > 100), number=100)
    print(duree)
    del df_pl

    # Pour Dask
    import dask.dataframe as dd
    df_dask = dd.read_csv(tr_file)
    duree = timeit.timeit(lambda: df_dask[df_dask["montant"] > 100].compute(), number=100)
    print(duree)
    del df_dask

def phase_2():
    import pandas as pd
    # ----------------------------------
    # parse = lambda d : pd.datetime.strptime(d, '%Y-%m-%d')
    df_pd = pd.read_csv(tr_file,
                        parse_dates=['date'],
                        date_format="%Y-%m-%d")
    df_pd["mois"] = df_pd["date"].dt.month
    df_pd["jour"] = df_pd["date"].dt.day
    df_pd.set_index('date', inplace=True)
    print(df_pd.divisions)
    resampled_pd = df_pd.resample('W').mean(numeric_only=True)
    print(resampled_pd.head())

def phase_3():
    import dask.dataframe as dd
    ddf = dd.read_csv(tr_file,
                      parse_dates=['date'],
                      date_format="%Y-%m-%d")
    ddf["mois"] = ddf["date"].dt.month
    ddf["jour"] = ddf["date"].dt.day
    ddf = ddf.set_index('date')
    print(ddf.divisions)
    resampled_dd = ddf.resample('W').mean(numeric_only=True).compute()
    print(resampled_dd.head())

phase_2()