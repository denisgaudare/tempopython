import sys
from PySide6.QtWidgets import QApplication
from window import MainWindow
from PySide6.QtGui import QPalette, QColor

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    # Thème sombre
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor("#2b2b2b"))
    palette.setColor(QPalette.WindowText, QColor("white"))
    palette.setColor(QPalette.Base, QColor("#3c3f41"))
    palette.setColor(QPalette.AlternateBase, QColor("#2b2b2b"))
    palette.setColor(QPalette.Text, QColor("white"))
    palette.setColor(QPalette.Button, QColor("#3c3f41"))
    palette.setColor(QPalette.ButtonText, QColor("white"))
    app.setPalette(palette)

    win = MainWindow()
    win.show()
    sys.exit(app.exec())
