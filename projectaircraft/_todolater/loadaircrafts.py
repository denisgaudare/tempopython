import csv

class Aircraft:
    def __init__(self, flight_name: str, capacity: int, fuel: float = 100.0):
        """
        Initialise un avion avec un nom de vol, une capacité et un niveau de carburant.
        """
        self.flight_name = flight_name
        self.capacity = capacity
        self.fuel = fuel

    def __str__(self):
        """Retourne une description de l'avion."""
        return f"Avion {self.flight_name} - Capacité: {self.capacity} passagers - Carburant: {self.fuel:.2f}%"


def load_aircrafts_from_csv(filename="flights.csv"):
    """
    Lit un fichier CSV et crée un dictionnaire d'objets Aircraft.

    :param filename: Nom du fichier CSV
    :return: Dictionnaire {flight_name: Aircraft}
    """
    aircrafts = {}

    with open(filename, mode="r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            # Création d'un objet Aircraft à partir des données CSV
            flight_name = row["flight_name"]
            capacity = int(row["capacity"])
            fuel = float(row["fuel"])

            aircraft = Aircraft(flight_name, capacity, fuel)
            aircrafts[flight_name] = aircraft  # Ajout à la collection

    return aircrafts


# Exemple d'utilisation
aircrafts_dict = load_aircrafts_from_csv()

# Affichage des avions chargés
for flight_name, aircraft in aircrafts_dict.items():
    print(aircraft)
