import pandas as pd
from .flight import Flight
from .airport import Airport
from datetime import datetime
from typing import List

def load_flights(csv_path: str) -> List[Flight]:
    df = pd.read_csv(csv_path)
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    return [
        Flight(
            flight_id=row['flight_id'],
            airline=row['airline'],
            origin=row['origin'],
            destination=row['destination'],
            date=row['date'],
            delay=int(row['delay'])
        )
        for _, row in df.iterrows()
    ]

def load_airports(csv_path: str) -> List[Airport]:
    df = pd.read_csv(csv_path)
    return [
        Airport(
            airport_code=row['airport_code'],
            airport_name=row['airport_name'],
            latitude=float(row['latitude']),
            longitude=float(row['longitude'])
        )
        for _, row in df.iterrows()
    ]
