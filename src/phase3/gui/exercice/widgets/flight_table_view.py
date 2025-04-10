from PySide6.QtWidgets import QTableView

class FlightTableView(QTableView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAlternatingRowColors(True)
        self.setSelectionBehavior(QTableView.SelectRows)
        self.setSortingEnabled(True)
        self.setMinimumSize(800, 400)
