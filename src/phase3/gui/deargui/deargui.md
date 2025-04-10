# Interface pédagogique avec DearPyGui – Exemple d’implémentation complète

Dans ce qui suit, nous présentons une interface pédagogique réalisée en Python avec la bibliothèque **DearPyGui**. Cette interface montre différents **widgets** (boutons, champs de texte, sliders, tableaux, menus déroulants) et utilise des **callbacks** (fonctions de rappel) pour interagir avec ces widgets. Elle est construite avec **plusieurs fenêtres** afin d’illustrer la navigation entre modules, et applique un **thème clair et coloré** pour une apparence agréable. Le code est organisé en plusieurs fichiers Python pour une meilleure lisibilité et maintenabilité.

**Fonctionnalités principales :**
- Utilisation de widgets variés : boutons, champ de saisie texte, slider numérique, tableau de données, menu déroulant, etc.
- Association de **callbacks** aux widgets pour gérer les interactions (clics, changements de valeur…).
- Présence de **plusieurs fenêtres** (une fenêtre principale et deux fenêtres de module) permettant de naviguer entre différentes sections de l’interface.
- Application d’un **thème personnalisé clair** avec des couleurs d’accentuation pour un rendu visuel coloré.
- Organisation du code en **modules séparés** (plusieurs fichiers) : un fichier principal de lancement, et des fichiers dédiés aux widgets, callbacks, thème et configuration.

## Structure du projet

Le projet est structuré en un seul répertoire contenant les fichiers suivants :  

- **`config.py`** – Contient les constantes de configuration, notamment les identifiants uniques (*tags*) des différentes fenêtres.  
- **`theme.py`** – Définit le thème visuel (couleurs et styles) de l’interface, ici un thème clair avec quelques couleurs d’accent.  
- **`widgets.py`** – Construit les fenêtres et widgets de l’interface (fenêtre principale et fenêtres de module avec leur contenu).  
- **`callbacks.py`** – Définit les fonctions de rappel associées aux widgets pour gérer les actions de l’utilisateur (navigation entre fenêtres, mise à jour de champs, etc.).  
- **`main.py`** – Point d’entrée de l’application, qui initialise DearPyGui, crée l’interface en s’appuyant sur les modules ci-dessus, applique le thème, et lance la boucle événementielle.

Chaque section de code ci-dessous correspond à l’un de ces fichiers. L’ensemble du code est **complet, exécutable et commenté** pour faciliter la compréhension. Il suffit de placer tous ces fichiers dans le même dossier et d’exécuter `main.py` pour lancer l’interface.

### Fichier `config.py` – Configuration globale

Le fichier `config.py` définit quelques constantes utilisées à travers l’application, par exemple les tags (identifiants uniques) attribués à chaque fenêtre. Ces identifiants seront importés dans les autres modules pour référencer les fenêtres lors du show/hide ou d’autres opérations.

```python
# config.py
# Ce module définit des constantes utilisées à travers l'application

# Identifiants (tags) uniques pour les fenêtres principales et modules
MAIN_WINDOW = "MainWindow"
MODULE1_WINDOW = "Module1Window"
MODULE2_WINDOW = "Module2Window"
```

### Fichier `theme.py` – Thème clair et coloré de l’interface

Le fichier `theme.py` crée un thème personnalisé pour styliser l’interface. Ici, nous utilisons un **thème clair** en définissant un fond de fenêtre gris très clair, un texte en noir, et nous ajoutons une couleur d’accent bleue pour les boutons (avec variantes pour l’état survolé et cliqué). La fonction `create_theme()` construit ce thème et le renvoie pour être appliqué globalement.

```python
# theme.py
# Ce module configure un thème clair et coloré pour l'interface

import dearpygui.dearpygui as dpg

def create_theme():
    """Crée et renvoie un thème clair et coloré pour l'interface."""
    with dpg.theme() as theme:
        # Composante globale pour tous les widgets (mvAll)
        with dpg.theme_component(dpg.mvAll):
            # Couleur de fond des fenêtres (WindowBg) en gris très clair
            dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (240, 240, 240), category=dpg.mvThemeCat_Core)
            # Couleur du texte en noir (presque noir)
            dpg.add_theme_color(dpg.mvThemeCol_Text, (10, 10, 10), category=dpg.mvThemeCat_Core)
        # Composante spécifique aux boutons (mvButton)
        with dpg.theme_component(dpg.mvButton):
            # Couleur de fond des boutons (bleu clair) et variantes hover/active
            dpg.add_theme_color(dpg.mvThemeCol_Button, (100, 150, 250), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (120, 170, 250), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (90, 130, 230), category=dpg.mvThemeCat_Core)
    return theme
```

### Fichier `widgets.py` – Création des fenêtres et widgets

Le fichier `widgets.py` construit l’ensemble de l’interface utilisateur en créant les fenêtres et en y ajoutant les différents widgets requis. On y définit : 

- **La fenêtre principale** (`Menu Principal`) contenant du texte de bienvenue et trois boutons – deux pour ouvrir les modules, et un pour quitter l’application. Un séparateur visuel est inséré avant le bouton *Quitter* pour le distinguer.  
- **La fenêtre Module 1** (initialement cachée) qui présente un formulaire simple : un champ de texte pour saisir un nom, un bouton « Dire bonjour » qui affiche un message de salutation personnalisé, ainsi qu’un slider numérique accompagné d’un texte affichant sa valeur en temps réel. Un bouton *Retour* permet de revenir à la fenêtre principale.  
- **La fenêtre Module 2** (également cachée au démarrage) qui contient un menu déroulant (*combo box*) pour sélectionner une option (avec affichage de l’option choisie), et un tableau de données à 3 colonnes illustrant l’affichage tabulaire. Cette fenêtre a aussi un bouton *Retour* vers l’accueil.  

Chaque widget important est associé à un callback défini dans `callbacks.py` (par exemple `callbacks.open_module1` pour le bouton ouvrant le module 1, `callbacks.on_slider_change` pour le slider, etc.). Les fenêtres Module 1 et Module 2 sont créées avec `show=False` pour être invisibles au lancement, et avec `no_close=True` pour empêcher l’utilisateur de les fermer via la barre de titre (la navigation se fait uniquement via les boutons prévus).

```python
# widgets.py
# Ce module définit la création des fenêtres et des widgets de l'interface

import dearpygui.dearpygui as dpg
import callbacks  # Importer le module des callbacks pour assigner les fonctions
import config     # Importer les constantes d'identifiants des fenêtres

def create_ui():
    """Crée les fenêtres (UI) et leurs widgets dans le contexte DearPyGui."""
    # Fenêtre principale - contient des boutons pour naviguer vers les modules
    with dpg.window(label="Menu Principal", tag=config.MAIN_WINDOW, width=300, height=200, no_close=True):
        dpg.add_text("Bienvenue dans l'interface de démonstration")
        # Bouton pour ouvrir le Module 1
        dpg.add_button(label="Ouvrir Module 1", callback=callbacks.open_module1)
        # Bouton pour ouvrir le Module 2
        dpg.add_button(label="Ouvrir Module 2", callback=callbacks.open_module2)
        # Séparateur visuel avant le bouton Quitter
        dpg.add_separator()
        # Bouton pour quitter l'application
        dpg.add_button(label="Quitter", callback=callbacks.stop_application)
    
    # Fenêtre Module 1 - cachée par défaut
    with dpg.window(label="Module 1 - Entrée utilisateur", tag=config.MODULE1_WINDOW, width=400, height=300, show=False, no_close=True):
        dpg.add_text("Module 1 : Exemple de formulaires et sliders")
        # Champ de texte pour saisir un nom
        name_input = dpg.add_input_text(label="Votre nom:")
        # Texte initialement vide qui affichera le message de salutation
        hello_text = dpg.add_text("", wrap=0)
        # Bouton qui déclenche un message utilisant le nom saisi
        dpg.add_button(label="Dire bonjour", callback=callbacks.greet_user, user_data=(name_input, hello_text))
        
        dpg.add_separator()  # Séparateur visuel
        
        # Texte affichant la valeur du slider
        value_text = dpg.add_text("Valeur: 0")
        # Slider (entier) de 0 à 100 
        dpg.add_slider_int(label="Ajustez la valeur", min_value=0, max_value=100,
                           callback=callbacks.on_slider_change, user_data=value_text)
        
        dpg.add_separator()  # Séparateur visuel
        
        # Bouton de retour pour revenir à la fenêtre principale
        dpg.add_button(label="Retour", callback=callbacks.back_to_main_from_module1)
    
    # Fenêtre Module 2 - cachée par défaut
    with dpg.window(label="Module 2 - Widgets avancés", tag=config.MODULE2_WINDOW, width=500, height=400, show=False, no_close=True):
        dpg.add_text("Module 2 : Exemple de menu déroulant et tableau")
        # Texte qui affichera l'option sélectionnée
        selected_text = dpg.add_text("Option choisie: Aucune")
        # Menu déroulant (combo box) avec quelques options
        dpg.add_combo(label="Choisissez une option", items=["Option A", "Option B", "Option C"],
                      callback=callbacks.on_combo_change, user_data=selected_text)
        
        dpg.add_separator()  # Séparateur visuel
        
        dpg.add_text("Exemple de tableau :")
        # Création d'un tableau avec 3 colonnes
        with dpg.table(header_row=True, resizable=True):
            dpg.add_table_column(label="Nom")
            dpg.add_table_column(label="Âge")
            dpg.add_table_column(label="Ville")
            # Première ligne du tableau
            with dpg.table_row():
                dpg.add_text("Alice")
                dpg.add_text("30")
                dpg.add_text("Paris")
            # Deuxième ligne du tableau
            with dpg.table_row():
                dpg.add_text("Bob")
                dpg.add_text("25")
                dpg.add_text("Lyon")
            # Troisième ligne du tableau
            with dpg.table_row():
                dpg.add_text("Charlie")
                dpg.add_text("35")
                dpg.add_text("Marseille")
        
        dpg.add_separator()  # Séparateur visuel
        
        # Bouton de retour à la fenêtre principale
        dpg.add_button(label="Retour", callback=callbacks.back_to_main_from_module2)
```

### Fichier `callbacks.py` – Fonctions de rappel (interactions)

Le fichier `callbacks.py` définit les différentes fonctions de rappel déclenchées par les actions de l’utilisateur sur l’interface. Chaque fonction correspond à un événement particulier :

- `open_module1` / `open_module2` : affichent la fenêtre du module correspondant et masquent la fenêtre principale, lorsqu’on clique sur le bouton *Ouvrir Module 1/2*.  
- `back_to_main_from_module1` / `back_to_main_from_module2` : font l’inverse, c’est-à-dire cacher la fenêtre de module et re-montrer la fenêtre principale (lorsqu’on clique sur *Retour* dans un module).  
- `greet_user` : appelée quand on clique sur le bouton *Dire bonjour* (module 1). Elle récupère le texte saisi dans le champ de nom et met à jour le label texte pour afficher un message de salutation (`"Bonjour, ... !"`).  
- `on_slider_change` : appelée à chaque modification du slider (module 1). Elle reçoit la nouvelle valeur (app_data) et met à jour le texte associé pour afficher la valeur actuelle du slider.  
- `on_combo_change` : appelée lorsque l’utilisateur sélectionne une option dans le combo box (module 2). Elle met à jour le texte `selected_text` pour indiquer l’option choisie.  
- `stop_application` : appelée lors du clic sur *Quitter* (fenêtre principale). Elle arrête la boucle principale de DearPyGui (`dpg.stop_dearpygui()`), ce qui provoque la fermeture de l’application.

Toutes ces fonctions utilisent l’API DearPyGui pour manipuler l’interface (par ex. `dpg.show_item`/`hide_item` pour afficher/masquer des éléments, `dpg.get_value` pour lire la valeur d’un widget, `dpg.set_value` pour modifier le contenu d’un widget). Les paramètres `sender, app_data, user_data` fournis par DearPyGui aux callbacks sont gérés selon les besoins (on utilise `user_data` pour passer des références de widgets à mettre à jour, par exemple).

```python
# callbacks.py
# Ce module contient les fonctions de rappel (callbacks) appelées par les interactions utilisateur

import dearpygui.dearpygui as dpg
import config  # pour accéder aux identifiants de fenêtres

def open_module1(sender, app_data, user_data):
    """Callback pour le bouton 'Ouvrir Module 1'"""
    # Affiche la fenêtre Module 1 et cache la fenêtre principale
    dpg.show_item(config.MODULE1_WINDOW)
    dpg.hide_item(config.MAIN_WINDOW)

def open_module2(sender, app_data, user_data):
    """Callback pour le bouton 'Ouvrir Module 2'"""
    # Affiche la fenêtre Module 2 et cache la fenêtre principale
    dpg.show_item(config.MODULE2_WINDOW)
    dpg.hide_item(config.MAIN_WINDOW)

def back_to_main_from_module1(sender, app_data, user_data):
    """Callback pour le bouton 'Retour' dans le Module 1"""
    # Cache la fenêtre Module 1 et réaffiche la fenêtre principale
    dpg.hide_item(config.MODULE1_WINDOW)
    dpg.show_item(config.MAIN_WINDOW)

def back_to_main_from_module2(sender, app_data, user_data):
    """Callback pour le bouton 'Retour' dans le Module 2"""
    # Cache la fenêtre Module 2 et réaffiche la fenêtre principale
    dpg.hide_item(config.MODULE2_WINDOW)
    dpg.show_item(config.MAIN_WINDOW)

def greet_user(sender, app_data, user_data):
    """Callback pour le bouton 'Dire bonjour' – utilise le nom saisi pour afficher un message"""
    name_input_tag, output_text_tag = user_data
    # Récupère le texte saisi dans le champ de nom
    name = dpg.get_value(name_input_tag)
    # Met à jour le texte de salutation personnalisé
    dpg.set_value(output_text_tag, f"Bonjour, {name} !")

def on_slider_change(sender, app_data, user_data):
    """Callback appelée lorsque le slider est déplacé"""
    output_text_tag = user_data
    # `app_data` contient la nouvelle valeur du slider
    value = app_data
    # Met à jour le texte affichant la valeur actuelle
    dpg.set_value(output_text_tag, f"Valeur: {value}")

def on_combo_change(sender, app_data, user_data):
    """Callback pour le changement de sélection du menu déroulant (combo)"""
    output_text_tag = user_data
    # `app_data` contient l'option sélectionnée (texte)
    choice = app_data
    # Met à jour le texte affichant l'option choisie
    dpg.set_value(output_text_tag, f"Option choisie: {choice}")

def stop_application(sender=None, app_data=None, user_data=None):
    """Callback pour le bouton 'Quitter' qui ferme l'application"""
    dpg.stop_dearpygui()
```

### Fichier `main.py` – Lancement de l’application

Le fichier `main.py` est le script principal qui assemble le tout et lance l’application. Il crée le contexte DearPyGui, construit l’interface en appelant la fonction `create_ui()` du module widgets, applique le thème défini, puis ouvre la fenêtre principale (viewport) et démarre la boucle événementielle. À la fermeture de l’interface (par le bouton *Quitter* ou la fermeture de la fenêtre), la fonction `stop_application` arrête la boucle ce qui fait sortir de `dpg.start_dearpygui()`, et le contexte est détruit proprement via `dpg.destroy_context()`.

```python
# main.py
# Point d'entrée principal de l'application

import dearpygui.dearpygui as dpg
import widgets   # Module de création d'interface (fenêtres et widgets)
import theme     # Module définissant le thème visuel
import config    # Module de configuration (identifiants)

# Créer le contexte DearPyGui (initialisation de la bibliothèque)
dpg.create_context()

# Construire l'interface utilisateur en créant les fenêtres et widgets
widgets.create_ui()

# Appliquer un thème clair et coloré à l'ensemble de l'interface
app_theme = theme.create_theme()
dpg.bind_theme(app_theme)

# Configurer le viewport (fenêtre principale de l'application)
dpg.create_viewport(title="Interface DearPyGui", width=800, height=600)
# Définir une couleur de fond pour le viewport (un blanc légèrement bleuté)
dpg.set_viewport_clear_color((220, 220, 235, 255))

# Lancer l'interface graphique
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()

# Détruire le contexte à la fermeture de l'application
dpg.destroy_context()
```

**Comment exécuter :** Placez tous ces fichiers dans le même dossier, assurez-vous d’installer la bibliothèque **DearPyGui** (`pip install dearpygui`), puis exécutez le script `main.py`. Une fenêtre s’ouvrira avec le menu principal. Vous pourrez tester les boutons pour naviguer entre les fenêtres, saisir du texte et voir les messages s’afficher, bouger le slider pour mettre à jour la valeur affichée, ou choisir une option dans le menu déroulant et observer le texte mis à jour, le tout avec le thème clair défini. Cette structure de code modulaire et commentée peut servir de base pédagogique pour comprendre et enseigner l’utilisation de DearPyGui.