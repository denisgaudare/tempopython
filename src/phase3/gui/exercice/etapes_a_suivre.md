
## 🧩 **Étape 1 : Squelette de projet et modèles de données**

### 🎯 Objectif :
Mettre en place l’arborescence du projet, créer les modèles `Flight` et `Airport`, et un loader de données depuis des CSV.

### 📁 Fichiers créés :
- `models/flight.py` → dataclass `Flight`
- `models/airport.py` → dataclass `Airport`
- `models/data_loader.py` → fonctions `load_flights()` et `load_airports()`
- `main.py` → test de chargement des données
- Dossier `flight_app` avec sous-dossiers : `models`, `widgets`, `actions`, `ui`, `config`, `data`

---

## 🖼️ **Étape 2 : Affichage des vols dans une table**

### 🎯 Objectif :
Afficher les vols dans un `QTableView` avec un `QAbstractTableModel`.

### 📁 Fichiers créés :
- `models/flight_table_model.py` → `FlightTableModel` hérite de `QAbstractTableModel`
- `widgets/flight_table_view.py` → widget `FlightTableView` avec quelques options de vue
- `ui/main_window.py` → fenêtre principale PySide6 avec le tableau
- `main.py` → modifié pour lancer l’application PySide6

---

## 🔍 **Étape 3 : Interface de filtrage/recherche**

### 🎯 Objectif :
Ajouter une UI pour filtrer les vols par origine, destination, et retard minimum.

### 📁 Fichiers créés :
- `widgets/flight_filter_widget.py` → `FlightFilterWidget` avec `QComboBox`, `QSpinBox`, `QPushButton`
- `actions/filter_logic.py` → fonction `filter_flights()` pour appliquer les filtres

### 📁 Fichiers modifiés :
- `ui/main_window.py` :
  - Intègre le widget de filtre
  - Connecte le bouton "Appliquer filtre" à la fonction de filtrage
  - Met à jour dynamiquement le modèle de table avec les résultats filtrés

---

## 🗺️ **Étape 4 : Carte interactive des aéroports** *(à venir)*

### 🎯 Objectif :
Afficher les aéroports sur une carte HTML via `QWebEngineView`, et permettre un clic pour filtrer les vols depuis cet aéroport.

### 📁 Fichiers à créer :
- `widgets/map_view.py` → carte avec `QWebEngineView`
- `ui/map_window.py` → fenêtre séparée ou zone dans `MainWindow` contenant la carte
- `actions/map_logic.py` → génération HTML dynamique avec Leaflet ou autre lib
- `models/airport_geo.py` *(optionnel)* → utilitaires géographiques

### 📁 Fichiers à modifier :
- `main_window.py` → intégrer la carte dans l’UI
- `filter_logic.py` → filtrage par clic sur la carte

---

## 🧾 **Étape 5 : Ajouter / modifier / supprimer un vol** *(à venir)*

### 🎯 Objectif :
Permettre à l’utilisateur de gérer les données depuis l’interface.

### 📁 Fichiers à créer :
- `widgets/flight_form.py` → `QDialog` ou `QWidget` pour saisir un vol
- `actions/crud.py` → logique d’ajout, édition, suppression de vols

### 📁 Fichiers à modifier :
- `main_window.py` → ajouter les boutons "Ajouter", "Modifier", "Supprimer"
- `flight_table_model.py` → méthodes pour ajouter/supprimer dans le modèle

---

## 🎨 **Étape 6 : Thème clair/sombre** *(à venir)*

### 🎯 Objectif :
Ajouter un thème visuel personnalisable.

### 📁 Fichiers à créer :
- `config/theme.py` → définitions de stylesheets ou palettes

### 📁 Fichiers à modifier :
- `main_window.py` → menu ou bouton pour basculer le thème

---

## 📤 **Étape 7 : Export CSV / PDF** *(à venir)*

### 🎯 Objectif :
Exporter les données affichées dans un fichier.

### 📁 Fichiers à créer :
- `actions/export.py` → fonction d’export `to_csv()` et `to_pdf()`

### 📁 Fichiers à modifier :
- `main_window.py` → ajouter boutons/menu d’export

---

## 🧠 **Étape 8 : Refactor en MVC / structuration finale** *(optionnel mais recommandé)*

### 🎯 Objectif :
Réorganiser le projet avec une architecture MVC claire.

### 📁 Impact :
- Modèle : `models/`
- Vue : `widgets/`, `ui/`
- Contrôleur : `actions/`
- Séparer `logic` / `ui` / `data` proprement
- Ajouter une documentation / README

---