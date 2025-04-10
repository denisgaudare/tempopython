from dataclasses import dataclass

@dataclass
class Airport:
    airport_code: str
    airport_name: str
    latitude: float
    longitude: float
