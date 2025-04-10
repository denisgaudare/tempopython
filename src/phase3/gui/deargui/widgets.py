# widgets.py
# Ce module définit la création des fenêtres et des widgets de l'interface

import dearpygui.dearpygui as dpg
import callbacks  # Importer le module des callbacks pour assigner les fonctions
import config  # Importer les constantes d'identifiants des fenêtres


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
    with dpg.window(label="Module 1 - Entrée utilisateur", tag=config.MODULE1_WINDOW, width=400, height=300, show=False,
                    no_close=True):
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
    with dpg.window(label="Module 2 - Widgets avancés", tag=config.MODULE2_WINDOW, width=500, height=400, show=False,
                    no_close=True):
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
