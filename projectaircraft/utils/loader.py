import csv

from projectaircraft.models.flight import Flight


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
            row['status']
        )
        flights.append(flight)
    return flights