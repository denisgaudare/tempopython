import csv
import json

from projectaircraft import config
from projectaircraft.models.flight import Flight
from projectaircraft.models.airport import Airport
from projectaircraft.utils.context_managers import OpenFlightData, Timer


def load_flights(csv_file):
    flights = []
    reader = csv.DictReader(csv_file)
    for row in reader:
        flight = Flight(
            row['flight_name'],
            int(row['capacity']),
            float(row['fuel']),
            row['airline'],
            int(row['manufacture_year']),
            float(row['range_km']),
            row['status'],
            row['origin'],
            row['destination']
        )
        flights.append(flight)
    return flights

def load_airports(json_file):
    data = json.load(json_file)
    airports = []
    for item in data:
        airport = Airport(
            code=item["code"],
            name=item["name"],
            city=item["city"],
            country=item["country"],
            latitude=float(item["latitude"]),
            longitude=float(item["longitude"]),
            altitude=int(item["altitude"])
        )
        airports.append(airport)

    return airports

if __name__ == "__main__":
    with Timer():
        with OpenFlightData(config.DATA / "flights.csv") as file:
            flights = load_flights(file)
            for f in flights[:5]:
                print(f)

        with OpenFlightData(config.DATA / "airports.old") as file:
            airports = load_airports(file)
            for a in airports[:5]:
                print(a)