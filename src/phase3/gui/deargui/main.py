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
