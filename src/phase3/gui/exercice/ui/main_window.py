from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from models.data_loader import load_flights
from models.flight_table_model import FlightTableModel
from widgets.flight_table_view import FlightTableView

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Flight Viewer")

        flights = load_flights("data/flights.csv")
        self.model = FlightTableModel(flights)
        self.table = FlightTableView()
        self.table.setModel(self.model)

        layout = QVBoxLayout()
        layout.addWidget(self.table)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
