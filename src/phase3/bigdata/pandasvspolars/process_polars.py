import polars as pl
import glob

def process_flights_polars(path="data/flights_*.csv"):
    files = glob.glob(path)
    df = pl.concat([pl.read_csv(f) for f in files])

    # Traitement lazy = performance + optimisations
    result = (
        df.lazy()
        .filter(pl.col("delay") > 15)
        .group_by("airline")
        .agg(pl.col("delay").mean().alias("avg_delay"))
        .collect()
    )
    return result
