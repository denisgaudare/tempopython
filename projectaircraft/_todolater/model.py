import random
import time
from contextlib import contextmanager

from projectaircraft.utils.metaclasses import NoInheritanceMeta


class Airport:
    """
    Gestionnaire de contexte pour la gestion des pistes
    d'aéroport.
    """

    def __init__(self, runways=2):
        self.available_runways = runways

    @contextmanager
    def request_runway(self, flight_name):
        """Gestion de l'accès aux pistes."""
        if self.available_runways == 0:
            print(f"⏳ {flight_name} attend une piste...")

        self.available_runways -= 1
        print(f"🛫 {flight_name} a obtenu une piste pour décoller/atterrir.")

        try:
            yield  # Exécution de la phase de vol
        finally:

            self.available_runways += 1
            print(f"🛬 {flight_name} a libéré une piste.")

class FlightLogger(metaclass=NoInheritanceMeta):
    """Gestionnaire de contexte pour l'enregistrement des logs de vol."""

    def __init__(self, filename="flight_logs.txt"):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, "a")  # Ouverture en mode ajout
        return self

    def log(self, message):
        """Écrit un message dans le log."""
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        self.file.write(f"[{timestamp}] {message}\n")
        print(f"📜 LOG: {message}")

    def __exit__(self, exc_type, exc_value, traceback):
        """Ferme proprement le fichier de log."""
        self.file.close()


class Aircraft:
    """Simulation d'un avion avec context managers pour la gestion des ressources."""

    def __init__(self, flight_name, airport):
        self.flight_name = flight_name
        self.airport = airport

    @contextmanager
    def manage_fuel(self):
        """Gestion du carburant et de la maintenance."""
        fuel = random.randint(50, 100)  # Carburant en pourcentage
        maintenance_check = random.choice([True, False])
        print(f"⛽ {self.flight_name} a {fuel}% de carburant avant le vol.")

        if fuel < 60:
            print(f"⚠️ {self.flight_name} a besoin de ravitaillement !")
        if maintenance_check:
            print(f"🔧 {self.flight_name} doit passer un contrôle technique avant le vol.")

        try:
            yield
        finally:
            print(f"🛑 {self.flight_name} vérifie son carburant après l'atterrissage.")

    def fly(self):
        """Simulation d'un cycle de vol."""
        with self.airport.request_runway(self.flight_name):
            with FlightLogger() as logger:
                with self.manage_fuel():
                    logger.log(f"{self.flight_name} a décollé.")
                    time.sleep(random.randint(2, 5))  # Simulation du vol
                    logger.log(f"{self.flight_name} est en vol.")
                    time.sleep(random.randint(2, 5))  # Simulation du vol
                    logger.log(f"{self.flight_name} a atterri.")

if __name__=="__main__":
    # Création des avions
    airport = Airport(3)
    aircrafts = [
        Aircraft("Flight 101", airport),
        Aircraft("Flight 202", airport),
        Aircraft("Flight 303", airport),
        Aircraft("Flight 404", airport)
    ]

    for ac in aircrafts:
        ac.fly()