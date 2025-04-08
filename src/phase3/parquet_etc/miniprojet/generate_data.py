import pandas as pd
import pyarrow as pa
import pyarrow.ipc as ipc
import os
from datetime import datetime, timedelta
import random
#import openpyxl

def generate_flights(num=1000):
    airports = ["JFK", "CDG", "LHR", "LAX", "FRA", "DXB"]
    airlines = ["Delta", "AirFrance", "Lufthansa", "Emirates", "United", "BritishAirways"]
    data = []

    for i in range(num):
        origin = random.choice(airports)
        dest = random.choice([a for a in airports if a != origin])
        duration = random.randint(60, 600)
        date = datetime(2024, 3, 1) + timedelta(days=random.randint(0, 6))
        data.append({
            "flight_id": f"FL{i:04d}",
            "origin": origin,
            "destination": dest,
            "airline": random.choice(airlines),
            "departure_time": date.strftime("%Y-%m-%d"),
            "duration_minutes": duration
        })

    return pd.DataFrame(data)

os.makedirs("data", exist_ok=True)
df = generate_flights(1000)
table = pa.Table.from_pandas(df)

df.to_parquet("data/flights.parquets",
              index=False,partition_cols=["airline"])
df.to_excel("data/flights.xlsx")

with ipc.new_file("data/flights.arrow", table.schema) as writer:
    writer.write(table)

print("✅ Données générées dans data/flights.???")
