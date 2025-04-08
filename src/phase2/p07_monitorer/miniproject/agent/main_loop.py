import os
import random
import socket
import threading
import time

import psutil
import requests

from primecalc import check_prime, fibonacci_matrix

SERVER_URL = "http://localhost:88/metrics"
PROCESS = psutil.Process(os.getpid())
AGENT_ID = socket.gethostname()

def get_metrics():
    return {
        "id": AGENT_ID,
        "cpu": PROCESS.cpu_percent(interval=0.1),
        "memory": PROCESS.memory_info().rss / 1024 / 1024
    }

def send_metrics_loop():
    while True:
        try:
            data = get_metrics()
            requests.post(SERVER_URL, json=data, timeout=1)
        except Exception as e:
            print(f"[!] Erreur envoi métriques : {e}")
        time.sleep(2)

def long_loop():
    i = 0
    while True:
        n = random.randint(10000,20000) * 3
        print(f"Fibo {fibonacci_matrix(random.randint(50,100))}")
        check_prime(n)
        print(f"[loop] tâche #{i}")
        i += 1
        time.sleep(2)

if __name__ == "__main__":
    threading.Thread(target=send_metrics_loop, daemon=True).start()
    long_loop()
