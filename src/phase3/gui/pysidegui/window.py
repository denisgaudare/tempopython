from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout
from sidebar import Sidebar
from widgets_panel import WidgetsPanel
from animations import fade_in_widget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dashboard animé - PySide6")
        self.resize(1100, 650)

        main_widget = QWidget()
        layout = QHBoxLayout(main_widget)

        self.sidebar = Sidebar()
        self.panel = WidgetsPanel()

        layout.addWidget(self.sidebar, 1)
        layout.addWidget(self.panel, 4)

        self.setCentralWidget(main_widget)

        # Animation d’apparition
        fade_in_widget(self)
