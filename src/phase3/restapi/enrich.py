import pandas as pd
from fetch_weather import get_weather

flights = pd.read_csv("data/flights.csv")
flights["departure_date"] = pd.to_datetime(flights["departure_time"]).dt.date

def enrich_flight(row):
    weather = get_weather(row["departure_airport"], str(row["departure_date"]))
    return pd.Series(weather)

weather_data = flights.apply(enrich_flight, axis=1)
enriched = pd.concat([flights, weather_data], axis=1)
enriched.to_csv("../../data/flights_enriched.csv", index=False)
