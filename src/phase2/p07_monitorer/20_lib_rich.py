# Exemple simple : rich.traceback.install()

from rich.traceback import install

# Active le rendu d'erreur enrichi pour toutes les exceptions
install()

def division():
    return 1 / 0

division()