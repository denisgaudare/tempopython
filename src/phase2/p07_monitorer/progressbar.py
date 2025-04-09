import time

from rich.progress import Progress
import os

from tqdm import tqdm


def lire_gros_fichier(path):
    # Étape 1 : compter les lignes (rapidement)
    with open(path, "r", encoding="utf-8") as f:
        total_lines = sum(1 for _ in f)

        # Étape 2 : lecture avec barre tqdm
    with open(path, "r", encoding="utf-8") as f:
        for line in tqdm(f, total=total_lines, desc="Lecture fichier"):
            # Traitement éventuel ici
            time.sleep(0.025)

    print("✅ Lecture terminée.")



if __name__ == "__main__":
    path = "../../../data/pg2.txt"
    if os.path.exists(path):
        lire_gros_fichier(path)
