import random
import threading
import time
from concurrent.futures import ThreadPoolExecutor

counter = 0
FUZZ = False

def fuzz():
    if FUZZ:
        time.sleep(random.random())

def worker_nolock():
    'My job is to increment the counter and print the current count'
    global counter

    fuzz()
    oldcnt = counter
    fuzz()
    counter = oldcnt + 1
    fuzz()
    print('The count is %d' % counter, end='')
    fuzz()
    print()
    fuzz()
    print('---------------', end='')
    fuzz()
    print()
    fuzz()


verrou = threading.Lock()
def worker_lock():
    global counter
    for _ in range(1000):
        with verrou:
            fuzz()
            oldcnt = counter
            fuzz()
            counter = oldcnt + 1
            fuzz()
            print('The count is %d' % counter, end='')
            fuzz()
            print()
            fuzz()
            print('---------------', end='')
            fuzz()
            print()
            fuzz()


worker = worker_lock
OPTION = 3


# on gere ses threads
if OPTION==1:
    # on demarre direct
    print('Starting up')
    fuzz()
    for i in range(10):
        threading.Thread(target=worker).start()
        fuzz()
    print('Finishing up')
    fuzz()

# Option 2
# Créer et lancer 10 threads par 'blocs'
if OPTION==2:
    # on cree, on run et join pour attendre la fin de tous
    threads = []
    for _ in range(10):
        t = threading.Thread(target=worker)
        threads.append(t)
        t.start()
    # Attendre que tous les threads aient fini
    for t in threads:
        t.join()

# on utilise un threadpool
if OPTION ==3:
    # Créer un ThreadPool avec 10 workers
    with ThreadPoolExecutor(max_workers=4) as executor:
        # Lancer 10 tâches en parallèle
        futures = [executor.submit(worker) for _ in range(10)]

        # Attendre la fin de toutes les tâches
        for future in futures:
            future.result()

print("Valeur finale du compteur :", counter)

