
# Structure du Projet
 
aircraft_project/
├── main.py
├── data/
│   └── flights.csv
├── models/
│   ├── base.py           # Classe de base avec metaclass
│   └── flight.py         # Modèle Flight
├── utils/
│   ├── decorators.py     # Décorateurs personnalisés
│   ├── context_managers.py  # Context managers
│   └── loader.py         # Chargement CSV



Conception Objet

class Flight(BaseModel):
    def __init__(self, name, capacity, fuel, airline, year, range_km, status):

class Fleet(BaseModel):
    def __init__(self, flights: List[Flight]):
        self.flights = flights

    def active_flights(self) -> List[Flight]:
    
    def average_capacity(self) -> float:

    def from_csv(cls, csv_file):
    
    def is_long_range(flight: Flight) -> bool:


context