from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel

class Sidebar(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Navigation"))
        layout.addWidget(QPushButton("Dashboard"))
        layout.addWidget(QPushButton("Utilisateurs"))
        layout.addWidget(QPushButton("Messages"))
        layout.addStretch()
        self.setLayout(layout)
