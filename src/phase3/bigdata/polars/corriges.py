import datetime
import polars as pl

file = "../pandasvspolars/data/flights_2024_12.csv"
df = pl.read_csv(file)
#1
retards = df.filter(pl.col("delay") > 60)
print(retards.head())

#2
retards_moyens = (
    df.group_by("airline")
      .agg(pl.mean("delay").alias("avg_delay"))
      .sort("avg_delay", descending=True)
)
print(retards_moyens)


#3
df = df.with_columns(
    pl.col("date").str.strptime(pl.Date, format="%Y-%m-%d")
)

print(df.schema)

vols_selection = df.filter(
    (pl.col("origin") == "CDG") &
    (pl.col("destination") == "JFK") &
    (pl.col("date") > datetime.date(2024,1,1))
)
print(vols_selection.head())
#4



df_delays = df.filter(pl.col("delay") > 30)
df_delays.write_parquet("delayed_flights.parquet")

#repertoire
df.write_parquet("flights.parquet", partition_by="airline")
dfarrow = df.to_arrow()

import pandas as pd

df = pd.read_parquet("delayed_flights.parquet")
print(df.head())


print(dfarrow)


# Duo de choc
import duckdb


df = pl.read_parquet("flights.parquet")
result = df.to_pandas().pipe(duckdb.query,"SELECT Count(*) from df").fetchall()