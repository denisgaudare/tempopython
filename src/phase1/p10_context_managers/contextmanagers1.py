import os.path
import sys


class MonContext:

    def __init__(self, repertoire):
        print(repertoire)
        self.repertoire = repertoire

    def __enter__(self):
        print("Enter")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exit")

with MonContext("../data") as rep:
    print(rep)

# --------------------------------------------
from contextlib import ContextDecorator # hybride

class ForceConfig(ContextDecorator):

    def __init__(self,rep):
        self.exist_avant = True
        self.rep = rep
    def __enter__(self):
        if not os.path.isfile("config.txt"):
            f = open("config.txt",mode="wt")
            f.write("DATA")
            f.close()
            self.exist_avant = False
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if not self.exist_avant:
            os.remove("config.txt")

with ForceConfig("../data") as force:
    print(force.exist_avant)
    print(force.rep)
    print(rep)


class Logger:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        return self

    def log(self, message):
        """Ouverture automatique du fichier"""
        if not self.file:
            self.file = open(self.filename, "a")
        """Écrit un message dans le fichier log"""
        self.file.write(message + "\n")

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            """Fermeture automatique du fichier"""
            self.file.close()

# Utilisation avec `with`
with Logger("../error.log") as logger:
    logger.log("Démarrage de l'application")
    logger.log("Une action a été effectuée")


class RedirectStdout:
    def __init__(self, filename):
        self.filename = filename
        self.file = None
        self.original_stdout = sys.stdout  # Sauvegarde du stdout original

    def __enter__(self):
        """Redirige la sortie standard vers un fichier"""
        self.file = open(self.filename, "w")
        sys.stdout = self.file  # Redirection du stdout
        return self  # Permet d'accéder à l'instance dans le `with`

    def __exit__(self, exc_type, exc_value, traceback):
        try:
            sys.stdout = self.original_stdout
            self.file.close()
        except:
            pass

        #  Si erreur survenue dans le bloc with
        if exc_type:
            print(f"Exception interceptée : {exc_type.__name__}: {exc_value}")
            return True  # L'exception est gérée et n'est pas propagée
        return False  # Permet à l'exception de se propager si elle existe

        """Restaure la sortie standard et ferme le fichier"""


# Utilisation :
with RedirectStdout("../output.txt"):
    print("Ce message sera écrit dans output.txt")
    print("Même ce deuxième message !")
    raise ValueError()

print("Ce message s'affiche normalement dans la console.")