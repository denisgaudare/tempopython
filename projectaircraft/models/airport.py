import threading
from collections import deque
from dataclasses import dataclass

from projectaircraft.models.base import NoInheritanceMeta


@dataclass(slots=True,repr=True)
class Airport(metaclass=NoInheritanceMeta):
    code: str            # ex: CDG
    name: str            # ex: Charles de Gaulle
    city: str            # ex: Paris
    country: str         # ex: France
    latitude: float
    longitude: float
    altitude: int        # en mètres

@dataclass
class Airport:
    code: str
    name: str
    city: str
    country: str
    runways: int = 2

    def __post_init__(self):
        self.landing_queue = deque()
        self.takeoff_queue = deque()
        self.lock = threading.Lock()