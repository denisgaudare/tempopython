import sys
import os
import argparse
import csv
import time
from datetime import datetime
import random

from tqdm import tqdm
from rich.progress import Progress, BarColumn, TextColumn, TimeElapsedColumn, TimeRemainingColumn

def generer_rapport_csv(n, output, progress_mode):
    """Génère un rapport CSV avec barre de progression selon le mode choisi."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    header = ["timestamp", "id", "valeur"]

    with open(output, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)

        it = None
        match progress_mode:
            case "silent": it = range(1, n + 1)
            case "tqdm" : it = tqdm(range(1, n + 1), desc="Génération", unit="ligne")

        if it:
            for i in it:
                valeur = round(random.uniform(0, 100), 2)
                writer.writerow([now, i, valeur])
                time.sleep(30/n)
        else:
            with Progress(
                TextColumn("[bold blue]{task.description}"),
                BarColumn(),
                "[progress.percentage]{task.percentage:>3.0f}%",
                TimeElapsedColumn(),
                TimeRemainingColumn()
            ) as progress:
                task = progress.add_task("Génération", total=n)
                for i in range(1, n + 1):
                    valeur = round(random.uniform(0, 100), 2)
                    writer.writerow([now, i, valeur])
                    progress.update(task, advance=1)

    print(f"[OK] Rapport CSV généré : {output}")

def parse_args():
    parser = argparse.ArgumentParser(description="Script batch avec CSV, tqdm et rich progress bar")
    parser.add_argument("-n", "--nombre", type=int, default=1000,
                        help="Nombre de lignes à générer (défaut : 1000)")
    parser.add_argument("-o", "--output", default="rapport.csv",
                        help="Nom du fichier de sortie CSV (défaut : rapport.csv)")
    parser.add_argument("--silent", action="store_true",
                        help="Désactiver la barre de progression")
    parser.add_argument("--rich", action="store_true",
                        help="Utiliser rich.progress à la place de tqdm")
    return parser.parse_args()

def main():
    print("=== Traitement batch démarré ===")
    args = parse_args()

    # Déterminer le mode de progress
    if args.silent:
        progress_mode = "silent"
    elif args.rich:
        progress_mode = "rich"
    else:
        progress_mode = "tqdm"

    generer_rapport_csv(args.nombre, args.output, progress_mode)
    print("=== Traitement terminé ===")

if __name__ == "__main__":
    main()