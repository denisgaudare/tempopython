import matplotlib.pyplot as plt
import numpy as np

# Tonalités majeures et mineures en cercle
major_keys = ["Do", "Sol", "Ré", "La", "Mi", "Si", "Fa♯", "Do♯", "La♭", "Mi♭", "Si♭", "Fa"]
minor_keys = ["La", "Mi", "Si", "Fa♯", "Do♯", "Sol♯", "Ré♯", "La♯", "Fa", "Do", "Sol", "Ré"]

# Angle pour chaque tonalité (12 au total)
angles = np.linspace(0, 2 * np.pi, 12, endpoint=False)

# Création du graphique
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'projection': 'polar'})
ax.set_theta_direction(-1)  # Sens des aiguilles d'une montre
ax.set_theta_offset(np.pi / 2)  # Mettre Do en haut

# Suppression des axes inutiles
ax.set_xticks([])
ax.set_yticks([])

# Placement des tonalités majeures
for angle, key in zip(angles, major_keys):
    ax.text(angle, 1.1, key, ha='center', va='center', fontsize=12, weight='bold', color='navy')

# Placement des tonalités mineures
for angle, key in zip(angles, minor_keys):
    ax.text(angle, 0.7, key + " m", ha='center', va='center', fontsize=11, color='darkred')

# Cercles décoratifs
ax.plot(np.linspace(0, 2*np.pi, 100), [1.1]*100, color='lightgray', linestyle='--')
ax.plot(np.linspace(0, 2*np.pi, 100), [0.7]*100, color='lightgray', linestyle='--')

# Titre
plt.title("Cercle des quintes (gammes majeures et mineures)", fontsize=14, weight='bold', pad=20)

plt.tight_layout()
plt.show()
