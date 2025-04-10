
### 🧩 **Exercice 1 : Chargement et affichage des données**
#### Objectif :
Lire des fichiers JSON/CSV contenant les informations sur les vols et les aéroports, et les afficher dans une interface simple.

#### Tâches :
- Créer un dossier `data/` avec deux fichiers : `flights.csv` et `airports.csv`
- Créer des classes `Flight` et `Airport` pour représenter les données.
- Utiliser `QTableView` avec un modèle personnalisé (`QAbstractTableModel`).

#### Structure suggérée :
```
project/
│
├── main.py
├── config/
│   └── theme.py
├── data/
│   ├── flights.csv
│   └── airports.csv
├── models/
│   ├── flight_model.py
│   └── airport_model.py
├── widgets/
│   └── table_view.py
├── actions/
│   └── load_data.py
```

---

### 🎛️ **Exercice 2 : Interface graphique de recherche**
#### Objectif :
Créer une interface avec des champs de recherche (aéroport de départ, destination, etc.)

#### Tâches :
- Ajouter une barre de recherche (avec `QLineEdit`, `QComboBox`)
- Filtrer les données dans la table en fonction des champs sélectionnés.
- Ajouter un `QPushButton` "Rechercher".

#### Nouveaux dossiers :
```
├── ui/
│   └── main_window.py
```

---

### 🧭 **Exercice 3 : Carte interactive des aéroports**
#### Objectif :
Afficher les aéroports sur une carte (statique ou HTML) et permettre le clic pour voir les vols depuis cet aéroport.

#### Tâches :
- Utiliser `QWebEngineView` pour charger une carte HTML (Leaflet ou autre).
- Générer dynamiquement la carte avec les marqueurs (depuis `airports.csv`)
- Gérer les clics sur les marqueurs pour filtrer les vols.

---

### 🔄 **Exercice 4 : Ajouter / Modifier / Supprimer un vol**
#### Objectif :
Gérer l’édition des données via l’interface.

#### Tâches :
- Ajouter une fenêtre modale (`QDialog`) pour saisir un vol.
- Boutons Ajouter / Modifier / Supprimer
- Relier ces boutons aux actions via des signaux/slots

---

### 🎨 **Exercice 5 : Personnalisation du thème**
#### Objectif :
Changer dynamiquement le thème (clair/sombre).

#### Tâches :
- Créer un module `theme.py` avec des constantes de style.
- Ajouter un menu ou un bouton pour switcher entre deux thèmes.

---

### 🚀 **Exercice 6 : Export et sauvegarde**
#### Objectif :
Exporter les vols filtrés en CSV ou PDF.

#### Tâches :
- Ajouter des boutons "Exporter en CSV", "Exporter en PDF"
- Utiliser `QFileDialog` pour choisir l’emplacement
- Utiliser `pandas` pour exporter en CSV et `reportlab` ou `fpdf` pour PDF

---

### 🧹 Bonus : Refonte architecture MVC
Une fois tous les exercices faits, proposer de **réorganiser le projet** autour d’un vrai pattern **MVC (Model-View-Controller)**, en structurant bien :

- **Model** : accès aux données
- **View** : widgets PySide6
- **Controller** : logique métier et actions utilisateur

---

