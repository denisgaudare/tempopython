from dataclasses import dataclass
from datetime import datetime

@dataclass
class Flight:
    flight_id: str
    airline: str
    origin: str
    destination: str
    date: datetime
    delay: int  # delay in minutes
