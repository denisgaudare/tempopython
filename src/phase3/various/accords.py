import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Définition des tonalités majeures avec dièses et leurs accords
tonalites_diese = [
    ("Do", ["C4", "E4", "G4"], ["D4", "F4", "A4"], ["E4", "G4", "B4"], ["F4", "A4", "C5"],
     ["G4", "B4", "D5"], ["A4", "C5", "E5"], ["B4", "D5", "F5"]),
    ("Sol", ["G4", "B4", "D5"], ["A4", "C5", "E5"], ["B4", "D5", "F♯5"], ["C5", "E5", "G5"],
     ["D5", "F♯5", "A5"], ["E5", "G5", "B5"], ["F♯5", "A5", "C6"]),
    ("Ré", ["D4", "F♯4", "A4"], ["E4", "G4", "B4"], ["F♯4", "A4", "C♯5"], ["G4", "B4", "D5"],
     ["A4", "C♯5", "E5"], ["B4", "D5", "F♯5"], ["C♯5", "E5", "G5"]),
    ("La", ["A4", "C♯5", "E5"], ["B4", "D5", "F♯5"], ["C♯5", "E5", "G♯5"], ["D5", "F♯5", "A5"],
     ["E5", "G♯5", "B5"], ["F♯5", "A5", "C♯6"], ["G♯5", "B5", "D6"]),
    ("Mi", ["E4", "G♯4", "B4"], ["F♯4", "A4", "C♯5"], ["G♯4", "B4", "D♯5"], ["A4", "C♯5", "E5"],
     ["B4", "D♯5", "F♯5"], ["C♯5", "E5", "G♯5"], ["D♯5", "F♯5", "A5"]),
    ("Si", ["B3", "D♯4", "F♯4"], ["C♯4", "E4", "G♯4"], ["D♯4", "F♯4", "A♯4"], ["E4", "G♯4", "B4"],
     ["F♯4", "A♯4", "C♯5"], ["G♯4", "B4", "D♯5"], ["A♯4", "C♯5", "E5"]),
    ("Fa♯", ["F♯4", "A♯4", "C♯5"], ["G♯4", "B4", "D♯5"], ["A♯4", "C♯5", "E♯5"], ["B4", "D♯5", "F♯5"],
     ["C♯5", "E♯5", "G♯5"], ["D♯5", "F♯5", "A♯5"], ["E♯5", "G♯5", "B5"])
]

# Fonction pour dessiner une portée serrée
def dessiner_portee(ax, x_base, y_base):
    for i in range(5):
        ax.plot([x_base, x_base + 1.5], [y_base + i * 0.3] * 2, color='black', linewidth=1)

def position_note(note_name):
    notes_order = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
    base_height = 1.5
    step = 0.15
    if len(note_name) == 3:
        note, alt, octave = note_name[0], note_name[1], int(note_name[2])
    else:
        note, alt, octave = note_name[0], '', int(note_name[1])
    index = notes_order.index(note)
    semitone_shift = {'': 0, '♯': 0.01, '♭': -0.01, '♮': 0}.get(alt, 0)
    return base_height + ((octave - 4) * 7 + index) * step + semitone_shift

# Créer la figure
fig, ax = plt.subplots(figsize=(16, 10))
ax.set_xlim(0, 11)
ax.set_ylim(-1, len(tonalites_diese) * 3.5)
ax.axis('off')

# Dessiner les gammes avec dièses
for i, (nom, *accords) in enumerate(tonalites_diese):
    y_base = len(tonalites_diese) * 3.2 - i * 3.2
    ax.text(0.3, y_base + 1.7, f"{nom} Majeur", fontsize=11, weight='bold', ha='left')

    for j, notes in enumerate(accords):
        x_base = 1 + j * 1.3
        dessiner_portee(ax, x_base, y_base)

        # Clé de sol symbolique
        if j == 0:
            ax.text(x_base - 0.1, y_base + 1.1, "𝄞", fontsize=16, ha='center', va='center')

        for idx, n in enumerate(notes):
            ypos = position_note(n) + y_base
            color = 'green' if idx == 1 else 'black'  # note du milieu en vert
            ax.add_patch(patches.Circle((x_base + 0.75, ypos), 0.08, color=color))
            if ypos > y_base + 1.2 or ypos < y_base:
                ax.plot([x_base + 0.65, x_base + 0.85], [ypos] * 2, color='black', linewidth=1)

plt.tight_layout()
plt.show()