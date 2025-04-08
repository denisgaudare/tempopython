#https://www.datacamp.com/tutorial/python-garbage-collection
import time
from contextlib import contextmanager

import gc
import os
import psutil

# Code gourmand en mémoire : créer une grande quantité de données
def fonction_gourmande():
    data = []
    for i in range(10000000):
        data.append('x' * 1000)  # Création de chaînes de caractères de 100 caractères
    del data
def memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / (1024 * 1024)  # Retourne la mémoire en Mo

@contextmanager
def without_gc():
    # Code avant le `yield` (partie d'entrée)
    print("Entrée dans le contexte")
    gc.disable()
    try:
        yield "Valeur de contexte"  # Le code entre `yield` et `exit` est l'intérieur du contexte
    finally:
        # Code après le `yield` (partie de sortie)
        gc.enable()
        print("Sortie du contexte")

if __name__=="__main__":
    # Désactiver le garbage collector
    print(f"Avant l'exécution : {memory_usage()} Mo")
    with without_gc():

        # Affichage de la mémoire après avoir alloué de la mémoire
        print(f"Après avoir alloué : {memory_usage()} Mo")

        # Désactivation explicite du garbage collector
        gc.collect()  # Cela ne devrait pas libérer de mémoire car le GC est désactivé

        # Affichage de la mémoire après l'exécution du code gourmand
        print(f"Après GC collect() (le GC est désactivé) : {memory_usage()} Mo")

    # Activer le GC pour voir qu'il n'a pas effectué de nettoyage

    # Forcer le garbage collector à nettoyer

    gc.set_debug(gc.DEBUG_STATS)
    gc.collect()

    time.sleep(2) # GC Thread, on lui laisse du temps
    mu = memory_usage()

    # Affichage de la mémoire après avoir activé et collecté le garbage collector
    print(f"Après GC collect() (le GC est activé) : {mu} Mo")
