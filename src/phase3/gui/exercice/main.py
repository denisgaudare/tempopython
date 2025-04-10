import sys

from models.data_loader import load_flights, load_airports
from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow

def main_v0():
    flights = load_flights("data/flights.csv")
    airports = load_airports("data/airports.csv")

    print("Loaded flights:", len(flights))
    print("Loaded airports:", len(airports))

def main():


    if __name__ == "__main__":
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec())

if __name__ == "__main__":
    main()
