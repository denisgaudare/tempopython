import random
import threading
import time
from concurrent.futures import ThreadPoolExecutor

verrou = threading.Lock()

counter = 0
counter2 = 0
FUZZ = True
def fuzz():
    if FUZZ:
        time.sleep(random.random())

def worker_verrou1():
    global counter
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

def worker_verrou2():
    global counter
    with verrou:
        fuzz()
        oldcnt = counter
        fuzz()
        counter2 = oldcnt + 1
        fuzz()
        print('The count is %d' % counter, end='')
        fuzz()
        print()
        fuzz()
        print('---------------', end='')
        fuzz()
        print()
        fuzz()

with ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(worker_verrou1) for _ in range(10)]
    for future in futures:
        future.result()

print("Valeur finale du compteur :", counter)

"""
### 🧠 Comparatif : Avantages / Inconvénients du verrou (`Lock`)
| Aspect | Avec `Lock` | Sans `Lock` |
|--------|-------------|-------------|
| ✅ **Exactitude** | Oui, résultat toujours correct | Non, résultats imprévisibles |
| ❌ **Performance** | Moins performant (car threads attendent le verrou) | Plus rapide, mais incorrect |
| ✅ **Sécurité** | Thread-safe | Non thread-safe |
| ❌ **Complexité** | Légèrement plus complexe à lire/écrire | Plus simple (mais risqué) |
| ⚠️ **Bloquages possibles** | Oui (si mal utilisé : deadlocks, starvation...) | Aucun blocage (mais erreurs silencieuses) |
"""
