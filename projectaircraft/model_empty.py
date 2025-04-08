import random
import time
from contextlib import contextmanager
from threading import Lock

class Airport:
    """
    Gestionnaire de contexte pour la gestion des pistes
    d'aéroport.
    """
    def __init__(self, runways=2):
        self.available_runways = runways

    # VA devenir un contexte manager avec decorateur
    def request_runway(self, flight_name):

        # ON verifie qu'il reste une piste
        # ON decremente le nombre de pistes de 1

        # Avion decolle

        # LA PISTE EST LIBEREE
        # ON incremente le nombre de pistes de 1


class FlightLogger:
    """Gestionnaire de contexte pour l'enregistrement des logs de vol."""

    def __init__(self, filename="flight_logs.log"):
        self.filename = filename

    def __enter__(self):
        # creation du fichier
        pass

    def log(self, message):
        # log du message vers le fichier
        pass


    def __exit__(self, exc_type, exc_value, traceback):
        """Ferme proprement le fichier de log."""
        pass


class Aircraft:
    """Simulation d'un avion avec context managers pour la gestion des ressources."""

    # ajouter les types
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
        # 1 on verifie le fuel
        # 2 on demande access a la piste (ce sera un context manager)
        #  log decollage, puis vol puis atterissage
