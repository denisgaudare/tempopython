import os

import pandas as pd
import logging
import sys

from phase3.parquet_etc.parquet_pipeline.sqllitehandler import SQLiteHandler

# ---------- Configuration du Logger ----------
logger = logging.getLogger("FlightPipeline")
logger.setLevel(logging.DEBUG)

# Console handler (stderr)
console_handler = logging.StreamHandler(sys.stderr)
console_handler.setLevel(logging.ERROR)
formatter = logging.Formatter("[%(levelname)s] %(message)s")
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# SQLite handler for step tracking
db_handler = SQLiteHandler("data/pipeline_logs.db")
db_handler.setLevel(logging.INFO)
logger.addHandler(db_handler)

# ---------- Pipeline ----------
dtypes = {
    "flight_id": "string",
    "origin": "category",
    "destination": "category",
    "airline": "category",
    "duration_minutes": "int32"
}

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop_duplicates(subset="flight_id")
    df = df[(df["duration_minutes"] > 0) & (df["duration_minutes"] < 1000)]
    df = df[df["origin"] != df["destination"]]
    logger.info("Nettoyage terminé.")
    return df

def process_data(df: pd.DataFrame) -> pd.DataFrame:
    df["is_long_flight"] = df["duration_minutes"] > 300
    df["duration_hours"] = df["duration_minutes"] / 60
    summary = (
        df.groupby("airline", observed=False)
        .agg(

            avg_duration=("duration_minutes", "mean"),
            max_duration=("duration_minutes", "max"),
            nb_vols=("flight_id", "count")
        )
        .reset_index()
    )
    logger.info("Traitement terminé.")
    return df, summary

def export_results(df: pd.DataFrame, summary: pd.DataFrame):
    os.makedirs("output", exist_ok=True)
    df.to_parquet("output/flights_cleaned.parquet",
                  partition_cols=["destination"],
                  compression="snappy", index=False)
    summary.to_csv("output/summary_by_airline.csv", index=False)
    logger.info("Export terminé.")

def main():
    try:
        logger.info("Chargement du fichier...")
        df = pd.read_excel("data/flights.xlsx", dtype=dtypes, parse_dates=["departure_time"])

        logger.info("Démarrage du nettoyage...")
        df = clean_data(df)

        logger.info("Démarrage du traitement...")
        df, summary = process_data(df)

        logger.info("Démarrage de l'export...")
        export_results(df, summary)

        logger.info("Pipeline terminé avec succès.")
    except Exception as e:
        logger.error(f"Erreur pendant le pipeline : {e}")
        raise

if __name__ == "__main__":
    main()
