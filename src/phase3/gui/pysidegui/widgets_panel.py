from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QTabWidget, QLabel, QPushButton, QTableWidget,
    QTableWidgetItem, QTextEdit, QFrame
)
from PySide6.QtCore import Qt, QTimer
from animations import fade_in_widget

class WidgetsPanel(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.tabs = QTabWidget()

        self.dashboard_tab = self.build_dashboard_tab()
        self.users_tab = self.build_users_tab()
        self.messages_tab = self.build_messages_tab()

        self.tabs.addTab(self.dashboard_tab, "Dashboard")
        self.tabs.addTab(self.users_tab, "Utilisateurs")
        self.tabs.addTab(self.messages_tab, "Messages")

        layout.addWidget(self.tabs)
        self.setLayout(layout)

        # Animation après 300ms (sinon trop tôt)
        QTimer.singleShot(300, lambda: fade_in_widget(self.dashboard_tab))

    def build_dashboard_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()

        welcome = QLabel("📊 Bienvenue sur le tableau de bord")
        welcome.setStyleSheet("font-size: 20px; font-weight: bold;")
        layout.addWidget(welcome)

        stats = QLabel("📈 Nombre d'utilisateurs actifs : 128\n📥 Nouveaux messages : 34")
        layout.addWidget(stats)

        tab.setLayout(layout)
        return tab

    def build_users_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()

        table = QTableWidget(3, 3)
        table.setHorizontalHeaderLabels(["Nom", "Email", "Rôle"])
        data = [
            ("Alice Dupont", "alice@example.com", "Admin"),
            ("Bob Martin", "bob@example.com", "Modérateur"),
            ("Chloé Durand", "chloe@example.com", "Utilisateur"),
        ]
        for i, row in enumerate(data):
            for j, cell in enumerate(row):
                table.setItem(i, j, QTableWidgetItem(cell))

        layout.addWidget(QLabel("Liste des utilisateurs"))
        layout.addWidget(table)
        tab.setLayout(layout)
        return tab

    def build_messages_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()

        layout.addWidget(QLabel("💬 Derniers messages :"))

        messages = QTextEdit()
        messages.setReadOnly(True)
        messages.setPlainText(
            "Alice : Bonjour tout le monde !\n"
            "Bob : La réunion commence à 14h.\n"
            "Chloé : D'accord, à tout à l'heure !"
        )

        layout.addWidget(messages)

        # Bouton d’actualisation simulée
        refresh_btn = QPushButton("🔄 Rafraîchir")
        refresh_btn.clicked.connect(lambda: messages.append("Nouvel utilisateur : bienvenue !"))
        layout.addWidget(refresh_btn)

        tab.setLayout(layout)
        return tab
