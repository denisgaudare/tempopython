from contextlib import contextmanager

@contextmanager
def mon_context_manager():
    # Code avant le `yield` (partie d'entrée)
    print("Entrée dans le contexte")
    try:
        yield "Valeur de contexte"  # Le code entre `yield` et `exit` est l'intérieur du contexte
    finally:
        # Code après le `yield` (partie de sortie)
        print("Sortie du contexte")


