from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QSplitter

from phase3.gui.exercice.actions.filter_logic import filter_flights
from phase3.gui.exercice.actions.map_logic import generate_map_html
from phase3.gui.exercice.models.data_loader import load_flights, load_airports
from phase3.gui.exercice.models.flight_table_model import FlightTableModel
from phase3.gui.exercice.widgets.flight_filter_widget import FlightFilterWidget
from phase3.gui.exercice.widgets.flight_table_view import FlightTableView
from phase3.gui.exercice.widgets.map_view import MapView


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Flight Viewer")

        self.all_flights = load_flights("data/flights.csv")
        airports = load_airports("data/airports.csv")
        airport_codes = [a.airport_code for a in airports]

        mymap = generate_map_html(airports)
        map_view = MapView(str(mymap))

        self.model = FlightTableModel(self.all_flights)
        self.table = FlightTableView()
        self.table.setModel(self.model)

        self.filter_widget = FlightFilterWidget(airport_codes)
        self.filter_widget.apply_btn.clicked.connect(self.apply_filter)

        # Interface principale
        left_layout = QVBoxLayout()
        left_layout.addWidget(self.filter_widget)
        left_layout.addWidget(self.table)
        left = QWidget()
        left.setLayout(left_layout)

        splitter = QSplitter()
        splitter.addWidget(left)
        splitter.addWidget(map_view)

        self.setCentralWidget(splitter)

    def apply_filter(self):
        filters = self.filter_widget.get_filters()
        filtered_flights = filter_flights(self.all_flights, filters)
        self.model.flights = filtered_flights
        self.model.layoutChanged.emit()