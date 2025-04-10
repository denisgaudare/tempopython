from PySide6.QtCore import QAbstractTableModel, Qt, QModelIndex
from models.flight import Flight

class FlightTableModel(QAbstractTableModel):
    def __init__(self, flights: list[Flight]):
        super().__init__()
        self.flights = flights
        self.headers = ["ID", "Airline", "Origin", "Destination", "Date", "Delay (min)"]

    def rowCount(self, parent=QModelIndex()) -> int:
        return len(self.flights)

    def columnCount(self, parent=QModelIndex()) -> int:
        return len(self.headers)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid() or role != Qt.DisplayRole:
            return None

        flight = self.flights[index.row()]
        column = index.column()

        if column == 0: return flight.flight_id
        if column == 1: return flight.airline
        if column == 2: return flight.origin
        if column == 3: return flight.destination
        if column == 4: return flight.date.strftime("%Y-%m-%d")
        if column == 5: return flight.delay

        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role != Qt.DisplayRole:
            return None
        if orientation == Qt.Horizontal:
            return self.headers[section]
        return section + 1
