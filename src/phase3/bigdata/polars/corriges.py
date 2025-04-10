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

vols_selection = df.filter(
    (pl.col("origin") == "CDG") &
    (pl.col("destination") == "JFK") &
    (pl.col("date") > pl.Date("2024-01-01"))
)
print(vols_selection.head())
#4




#5