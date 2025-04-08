import threading
import time


class ThreadManager:
    def __init__(self, foo):
        self.thread = None
        self.running = False
        self.foo = foo

    def __enter__(self):
        """Démarre automatiquement le thread"""
        self.running = True
        self.thread = threading.Thread(target=self.foo)
        self.thread.start()
        return self  # Retourne l'instance pour pouvoir appeler `log()`

    def __exit__(self, exc_type, exc_value, traceback):
        """Arrête automatiquement le thread à la sortie du `with`"""
        self.running = False
        self.thread.join()  # Attendre la fin propre du thread

def runme():
    print("Thread en cours d'exécution...")
    time.sleep(5)

def runother():
    pass

# Utilisation avec `with`
with ThreadManager(runme):
    time.sleep(3)  # Laisser le thread tourner un peu
    print("Fin du bloc `with`, arrêt automatique du thread")



