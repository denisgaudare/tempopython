from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl

class MapView(QWebEngineView):
    def __init__(self, html_path: str):
        super().__init__()
        self.load(QUrl.fromLocalFile(html_path))

    def handle_url(self, url: QUrl):
        if url.scheme() == "filter":
            code = url.path().lstrip("/")
            self.airport_selected.emit(code)