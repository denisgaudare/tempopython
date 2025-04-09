import random
import threading
import time

counter = 0 # COURSE A LA VALEUR
verrou = threading.Lock()

FUZZ = True
def fuzz():
    if FUZZ:
        time.sleep(random.random())

def worker(index):
    'My job is to increment the counter and print the current count'
    global counter

    with verrou:
        fuzz()
        oldcnt = counter
        fuzz()
        counter = oldcnt + 1
        fuzz()
        print(f"{index} The count is %d' % counter", end='')
        fuzz()
        print()
        fuzz()
        print('---------------', end='')
        fuzz()
        print()
        fuzz()


# on gere ses threads
# on demarre direct
print('Starting up')
fuzz()
for i in range(10):
    t = threading.Thread(target=worker, args=(i))
    fuzz()
    t.start()
    fuzz()
    t.join()
print('Finishing up')
fuzz()

print("Valeur finale du compteur :", counter)

