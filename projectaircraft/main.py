from projectaircraft.models.fleet import Fleet
from projectaircraft.utils.context_managers import OpenFlightData, Timer

with Timer():
    with OpenFlightData("data/flights.csv") as f:
        fleet = Fleet.from_csv(f)
        print(f"{fleet.average_capacity():1.2f}")
        for f in fleet.long_flights():
            print(f)
