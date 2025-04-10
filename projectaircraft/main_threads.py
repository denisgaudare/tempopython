import random
import signal
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor

from projectaircraft import config
from projectaircraft.controller.tower import ControlTower
from projectaircraft.controller.worker import RunwayWorker
from projectaircraft.models.airport import LocalAirport
from projectaircraft.models.fleet import Fleet
from projectaircraft.utils.context_managers import OpenFlightData

def main():
    cdg = LocalAirport(code="CDG", name="Charles de Gaulle", city="Paris", country="France")
    tower = ControlTower(cdg)

    cdg.runways = 3

    # Tous les vols
    with OpenFlightData(config.DATA / "flights.csv") as file:
        fleet = Fleet.from_csv(file)

    # Lancer les threads de piste
    runways = [RunwayWorker(cdg, i+1) for i in range(cdg.runways)]

    for r in runways:
       r.start()

    actives_only = lambda f : f.status == "active"
    flights = fleet.select_all(actives_only)

    #Interrompre par CTRL+C propre
    def stops_all():
        for r in runways:
            r.stop()
    def handle_sigint(signum, frame):
        print("\n(Ctrl+C). Cleaning up before exit.")
        stops_all()
        sys.exit(0)
    signal.signal(signal.SIGINT, handle_sigint)

    while True:
        flight1,flight2,flight3 = random.sample(flights,3)

        tower.request_takeoff(flight1)
        tower.request_landing(flight2)
        tower.request_landing(flight3)

        #Laisser tourner un moment
        time.sleep(5)

    # Arrêter les threads proprement
    stops_all()

def main_pool():
    cdg = LocalAirport(code="CDG", name="Charles de Gaulle", city="Paris", country="France")
    tower = ControlTower(cdg)

    # Tous les vols
    with OpenFlightData(config.DATA / "flights.csv") as file:
        fleet = Fleet.from_csv(file)

    stop_event = threading.Event()

    with ThreadPoolExecutor(max_workers=cdg.runways) as executor:
        # Lancer les workers de piste
        for i in range(cdg.runways):
            #executor.submit(runway_worker, cdg, i + 1, stop_event)
            pass

    actives_only = lambda f : f.status == "active"
    flights = fleet.select_all(actives_only)

    def handle_sigint(signum, frame):
        print("\n(Ctrl+C). Cleaning up before exit.")
        # Signaler l'arrêt à tous les workers
        stop_event.set()
        sys.exit(0)
    signal.signal(signal.SIGINT, handle_sigint)

    while True:
        flight1,flight2,flight3 = random.sample(flights,3)

        tower.request_landing(flight2)
        tower.request_takeoff(flight1)
        tower.request_landing(flight3)

        #Laisser tourner un moment
        time.sleep(5)


    # Arrêter les threads proprement avec un event
    stop_event.set()

if __name__ == "__main__":
    main()