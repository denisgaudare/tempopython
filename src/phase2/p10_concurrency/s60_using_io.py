import threading
import time

def thread_io_task(id):
    time.sleep(1)  # Simule une opération I/O (ex: accès disque, réseau)
    with open("log_thread.txt", "a") as f:
        for _ in range(10000):
            f.write(f"[Thread {id}] Tâche terminée\n")

def do_test_io():
    start = time.time()
    threads = []
    for i in range(10):
        t = threading.Thread(target=thread_io_task, args=(i,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    end = time.time()
    print(f"[Threading I/O] Temps total : {end - start:.2f} sec")

import multiprocessing
import time

def process_io_task(id):
    time.sleep(1)  # Simule une opération I/O
    with open("log_process.txt", "a") as f:
        for _ in range(10000):
            f.write(f"[Process {id}] Tâche terminée\n")

def do_processes_io():
    start = time.time()
    processes = []
    for i in range(3):
        p = multiprocessing.Process(target=process_io_task, args=(i,))
        p.start()
        processes.append(p)
    for p in processes:
        p.join()
    end = time.time()
    print(f"[Multiprocessing I/O] Temps total : {end - start:.2f} sec")

if __name__ == "__main__":
    print("=== Tâches I/O avec Threads ===")
    do_test_io()
    print("\n=== Tâches I/O avec Processus ===")
    do_processes_io()
