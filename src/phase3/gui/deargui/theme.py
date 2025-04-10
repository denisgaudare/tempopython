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
