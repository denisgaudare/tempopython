import polars as pl

df = pl.read_ipc("data/flights.arrow")

print("✈️ Vols par aéroport d’origine :")
print(df.groupby("origin").count())

print("\n📊 Durée moyenne des vols par compagnie :")
print(df.groupby("airline").agg(pl.col("duration_minutes").mean().alias("avg_duration")))

print("\n🕔 Vols de plus de 5 heures :")
print(df.filter(pl.col("duration_minutes") > 300).select(["flight_id", "origin", "destination", "duration_minutes"]))

print("\n📅 Moyenne de vols par jour :")
print(df.groupby("departure_time").count().sort("departure_time"))
