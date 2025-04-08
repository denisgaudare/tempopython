from prefect import flow, task

@task
def charger_donnees():
    import pandas as pd
    return pd.read_csv("flights.csv")

@task
def nettoyer(df):
    return df[df["duration_minutes"] > 0]

@task
def exporter(df):
    df.to_parquet("cleaned.parquet")

@flow
def pipeline_vols():
    df = charger_donnees()
    df_clean = nettoyer(df)
    exporter(df_clean)

if __name__ == "__main__":
    pipeline_vols()
