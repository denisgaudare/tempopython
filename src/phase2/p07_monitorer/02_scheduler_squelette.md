# ✅ Projet Scheduler/worker Python basé sur une boucle `while True`**, avec du monitoring intégré (logs, erreurs, ressources, fréquence de tâche, etc.).

# 🗂️ Squelette : Script Scheduler/Worker avec `while True`

### 📁 Arborescence

```
my_worker_project/
├── worker.py
├── monitor.py
├── config.py
├── requirements.txt
└── logs/
    └── worker.log
```

---

### 📦 `requirements.txt`

```txt
loguru
psutil
sentry-sdk
```

---

### ⚙️ `config.py`

```python
import os

WORKER_INTERVAL = int(os.getenv("WORKER_INTERVAL", 10))  # secondes
LOG_PATH = os.getenv("LOG_PATH", "logs/worker.log")
SENTRY_DSN = os.getenv("SENTRY_DSN", "")
```

---

### 🛡️ `monitor.py`

```python
from loguru import logger
import psutil
import sentry_sdk
from config import LOG_PATH, SENTRY_DSN

# Logger configuré
logger.add(LOG_PATH, rotation="1 MB", retention="7 days", level="INFO")

# Sentry configuré si présent
if SENTRY_DSN:
    sentry_sdk.init(dsn=SENTRY_DSN)

def log_resources():
    process = psutil.Process()
    mem = process.memory_info().rss / 1e6
    cpu = psutil.cpu_percent(interval=0.1)
    logger.debug(f"[RESOURCES] RAM: {mem:.2f} MB | CPU: {cpu}%")

def monitor_exceptions(fn):
    def wrapper(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except Exception as e:
            logger.exception("Erreur dans le worker")
            sentry_sdk.capture_exception(e)
            raise
    return wrapper
```

---

### 🔄 `worker.py`

```python
import time
from config import WORKER_INTERVAL
from monitor import logger, log_resources, monitor_exceptions

@monitor_exceptions
def do_work():
    logger.info("Traitement en cours...")
    # Simulation d'un travail
    time.sleep(2)
    # raise ValueError("Erreur simulée")  # Pour test
    logger.info("Traitement terminé.")

if __name__ == "__main__":
    logger.info("=== WORKER DÉMARRÉ ===")

    while True:
        logger.info("⏳ Tâche planifiée lancée")
        log_resources()
        do_work()
        logger.info(f"🕒 Pause de {WORKER_INTERVAL}s avant la prochaine exécution\n")
        time.sleep(WORKER_INTERVAL)
```

---

### 🛠️ Pour exécuter

```bash
python worker.py
```

---

### ✅ Fonctionnalités incluses

- Logs persistants avec rotation
- Logging structuré (via `loguru`)
- Monitoring CPU/RAM (`psutil`)
- Gestion et notification des erreurs (`sentry-sdk`)
- Tâche répétée via `while True + sleep`
