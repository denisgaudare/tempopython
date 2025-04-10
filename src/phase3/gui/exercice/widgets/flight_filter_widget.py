from PySide6.QtWidgets import QWidget, QFormLayout, QComboBox, QSpinBox, QPushButton

class FlightFilterWidget(QWidget):
    def __init__(self, airport_codes: list[str]):
        super().__init__()
        layout = QFormLayout()

        self.origin_cb = QComboBox()
        self.origin_cb.addItem("Any")
        self.origin_cb.addItems(sorted(airport_codes))

        self.destination_cb = QComboBox()
        self.destination_cb.addItem("Any")
        self.destination_cb.addItems(sorted(airport_codes))

        self.delay_spin = QSpinBox()
        self.delay_spin.setMinimum(0)
        self.delay_spin.setMaximum(1000)
        self.delay_spin.setSuffix(" min")

        self.apply_btn = QPushButton("Appliquer filtre")

        layout.addRow("Origine :", self.origin_cb)
        layout.addRow("Destination :", self.destination_cb)
        layout.addRow("Retard supérieur à :", self.delay_spin)
        layout.addRow("", self.apply_btn)

        self.setLayout(layout)

    def get_filters(self) -> dict:
        origin = self.origin_cb.currentText()
        dest = self.destination_cb.currentText()
        delay = self.delay_spin.value()
        return {
            "origin": None if origin == "Any" else origin,
            "destination": None if dest == "Any" else dest,
            "min_delay": delay
        }
