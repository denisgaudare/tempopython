
import pandas as pd
import random
from datetime import datetime, timedelta

def add_noise(data):
    ln = len(data)
    ra = random.randint(0,ln*50)
    if ra<ln:
        data[ra] = random.choice([None,'',data[ra]])
    return data

def generate_flights_csv(output_path="flights.csv", n_flights=2000, seed=42):
    random.seed(100000)

    # Liste des aéroports de référence
    airport_codes = ['CDG', 'LHR', 'JFK', 'LAX', 'DXB', 'HND', 'SIN', 'FRA', 'AMS', 'MAD']
    start_date = datetime(2025, 3, 26)

    flights_data = []
    fields = ("flight_id","origin_airport","destination_airport",
            "departure_time","scheduled_arrival_time","arrival_time")

    for _ in range(n_flights):
        origin, destination = random.sample(airport_codes, 2)
        dep_time = start_date + timedelta(
            days=random.randint(0, 60),
            hours=random.randint(0, 23),
            minutes=random.randint(0, 59)
        )
        duration = timedelta(hours=random.randint(1, 12), minutes=random.randint(0, 59))
        arr_time = dep_time + duration
        sched_arr_time = arr_time - timedelta(minutes=random.randint(-30, 30))

        data = [f"FL{random.randint(1000, 9999)}",
                origin,destination,dep_time.isoformat(),
                sched_arr_time.isoformat(),arr_time.isoformat()
                ]

        data = add_noise(data)
        flights_data.append(dict(zip(fields, data)))

    flights_df = pd.DataFrame(flights_data)
    flights_df.to_csv(output_path, index=False)
    print(f"{n_flights} vols générés dans '{output_path}'")

# Exemple d'utilisation
if __name__ == "__main__":
    generate_flights_csv("flights.csv", n_flights=10000)
