import threading
import multiprocessing
import time

# ----------- THREADING -----------
def thread_increment(compteur):
    for _ in range(100_000):
        compteur[0] += 1

def do_threads():
    compteur = [0]  # liste mutable pour partager entre threads
    t1 = threading.Thread(target=thread_increment, args=(compteur,))
    t2 = threading.Thread(target=thread_increment, args=(compteur,))
    start = time.time()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end = time.time()
    print(f"[Threading] Compteur final: {compteur[0]}, Temps: {end - start:.4f} sec")


# ----------- MULTIPROCESSING -----------
def process_increment(compteur):
    for _ in range(100_000):
        compteur.value += 1

def do_processes():
    compteur = multiprocessing.Value('i',0)  # mémoire partagée entre processus
    p1 = multiprocessing.Process(target=process_increment, args=(compteur,))
    p2 = multiprocessing.Process(target=process_increment, args=(compteur,))
    start = time.time()
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end = time.time()
    print(f"[Multiprocessing] Compteur final: {compteur.value}, Temps: {end - start:.4f} sec")


if __name__ == "__main__":
    print("=== Comparaison Threading vs Multiprocessing ===")
    do_threads()
    do_processes()
