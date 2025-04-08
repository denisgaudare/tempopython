from dataclasses import dataclass

@dataclass
class Flight:
    __slots__ = ['name', 'capacity', 'fuel', 'airline', 'year', 'range_km', 'status']

    name: str
    capacity: int
    fuel: float
    airline: str
    year: int
    range_km: float
    status: str

class FlighSecret():
    __slots__ = ["varpublic"]
    def __init__(self):
        self.varpublic = "PUBLIC"

