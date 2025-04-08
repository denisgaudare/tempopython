import threading
import queue
import time

FUZZ = False
compteur = 0

def fuzz():
    if FUZZ:
        time.sleep(0.01)

# File partagée
q = queue.Queue()

# Producteur : met 1000 "1" dans la file
def producteur():
    fuzz()
    print("on ajoute 1")
    fuzz()
    q.put(1)
    fuzz()

# Consommateur : lit les valeurs et les ajoute au compteur
def consommateur():
    for i in range(1000):
        global compteur
        fuzz()
        val = q.get()
        fuzz()
        compteur += val
        print(f"compteur {compteur}")
        fuzz()
        q.task_done()
        fuzz()

# Démarrer le thread consommateur
t_cons = threading.Thread(target=consommateur)
t_cons.start()

# Démarrer 10 producteurs
threads_prod = []
for _ in range(10):
    t = threading.Thread(target=producteur)
    t.start()
    threads_prod.append(t)

# Attendre que les producteurs terminent
for t in threads_prod:
    t.join()

# Attendre que toute la queue soit vidée
q.join()

# Attendre que le consommateur termine
t_cons.join()

print("Valeur finale du compteur :", compteur)
