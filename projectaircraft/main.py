import random
import time

from projectaircraft import config
from projectaircraft.controller.tower import ControlTower
from projectaircraft.models.airport import LocalAirport
from projectaircraft.models.fleet import Fleet
from projectaircraft.utils.context_managers import OpenFlightData


def main():
    cdg = LocalAirport(code="CDG", name="Charles de Gaulle", city="Paris", country="France")
    tower = ControlTower(cdg)

    with OpenFlightData(config.DATA / "flights.csv") as file:
        fleet = Fleet.from_csv(file)

    actives_only = lambda f : f.status == "active"
    flights = fleet.select_all(actives_only)

    flight1,flight2,flight3 = random.sample(flights,3)

    tower.request_takeoff(flight1)
    tower.request_landing(flight2)
    tower.request_landing(flight3)

    for _ in range(5):
        tower.check_status()
        time.sleep(5)
        tower.process_next_operation()
        time.sleep(5)

if __name__ == "__main__":
    main()