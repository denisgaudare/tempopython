import sys
import os
import argparse
import csv
import time
from datetime import datetime
import random
from tqdm import tqdm  # ✅ Progress bar

def generer_rapport_csv(n, output):
    """Génère un fichier CSV avec n lignes de données simulées."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    header = ["timestamp", "id", "valeur"]

    with open(output, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        for i in tqdm(range(1, n + 1), desc="Génération", unit="ligne"):
            valeur = round(random.uniform(0, 100), 2)
            writer.writerow([now, i, valeur])
            time.sleep((0.30))

    print(f"[OK] Rapport CSV généré : {output}")

def parse_args():
    parser = argparse.ArgumentParser(description="Script batch avec CSV et barre de progression")
    parser.add_argument("-n", "--nombre", type=int, default=10,
                        help="Nombre de lignes à générer (défaut : 10)")
    parser.add_argument("-o", "--output", default="rapport.csv",
                        help="Nom du fichier de sortie CSV (défaut : rapport.csv)")
    return parser.parse_args()

def main():
    print("=== Traitement batch démarré ===")
    args = parse_args()
    generer_rapport_csv(args.nombre, args.output)
    print("=== Traitement terminé ===")

if __name__ == "__main__":
    main()