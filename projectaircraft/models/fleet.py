from projectaircraft.models.flight import Flight


class BaseModel:
    pass

class Fleet(BaseModel):
    def __init__(self, flights: list[Flight]):
        self.flights = flights

    def long_flights(self) -> list[Flight]:
        return [f for f in self.flights if Fleet.is_long_range(f)]

    def active_flights(self) -> list[Flight]:
        return [ f for f in self.flights if f.status == "Actif" ]

    def average_capacity(self) -> float:
        return sum(f.capacity for f in self.flights) / len(self.flights)

    def group_by_airline(airline:str):
        pass


    @classmethod
    def from_csv(cls, csv_file):
        from projectaircraft.utils.loader import load_flights
        flights = load_flights(csv_file)
        # return une instance de Fleet
        return cls(flights)

    def to_csv(cls, csv_file):
        pass


    @staticmethod # !!!
    def is_long_range(flight:Flight) -> bool:
        return flight.range_km > 3000
