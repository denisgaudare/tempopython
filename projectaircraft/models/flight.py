from dataclasses import dataclass

from projectaircraft.models.base import NoInheritanceMeta


@dataclass(slots=True,repr=True)
class Flight(metaclass=NoInheritanceMeta):

    name: str
    capacity: int
    fuel: float
    airline: str
    year: int
    range_km: float
    status: str

