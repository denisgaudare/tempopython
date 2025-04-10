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
