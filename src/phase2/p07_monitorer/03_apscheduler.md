# ✅ Squelette de projet basé sur `APScheduler`**, une solution robuste et modulaire pour **planifier des tâches** (récurrentes, uniques, différées, etc.) dans un script Python.

---

# 🛠️ Worker Python avec `APScheduler`

## ⚙️ Avantages de `APScheduler`
- 🔁 Planification simple de tâches récurrentes
- ⏱ Support des jobs périodiques, cron, ou datés
- 🧩 Exécution en background via ThreadPool
- 📦 Persistable (SQLite, Redis…) si besoin

---

## 📁 Arborescence

```
apscheduler_worker/
├── worker.py
├── monitor.py
├── config.py
├── tasks.py
├── requirements.txt
└── logs/
    └── apscheduler.log
```

---

## 📦 `requirements.txt`

```txt
apscheduler
loguru
psutil
sentry-sdk
```

---

## ⚙️ `config.py`

```python
import os

LOG_PATH = os.getenv("LOG_PATH", "logs/apscheduler.log")
SENTRY_DSN = os.getenv("SENTRY_DSN", "")
```

---

## 📋 `monitor.py`

```python
from loguru import logger
import psutil
import sentry_sdk
from config import LOG_PATH, SENTRY_DSN

# Logger configuré
logger.add(LOG_PATH, rotation="1 MB", retention="7 days", level="INFO")

# Sentry
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
            logger.exception("Erreur dans la tâche")
            sentry_sdk.capture_exception(e)
            raise
    return wrapper
```

---

## 🧠 `tasks.py`

```python
import time
from monitor import logger, log_resources, monitor_exceptions

@monitor_exceptions
def scheduled_job():
    logger.info("🔧 Tâche planifiée démarrée")
    log_resources()
    time.sleep(2)  # Simule un traitement
    logger.info("✅ Tâche terminée")
```

---

## 🔄 `worker.py`

```python
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ThreadPoolExecutor
from tasks import scheduled_job
from monitor import logger
import time

if __name__ == "__main__":
    logger.info("=== APScheduler Worker démarré ===")

    # Configuration du scheduler
    scheduler = BackgroundScheduler(
        executors={'default': ThreadPoolExecutor(4)},
        job_defaults={'coalesce': False, 'max_instances': 2}
    )

    # Ajouter une tâche toutes les 10 secondes
    scheduler.add_job(scheduled_job, 'interval', seconds=10, id='main_job')

    # Démarrer le scheduler
    scheduler.start()

    try:
        while True:
            time.sleep(1)  # Main thread reste vivant
    except (KeyboardInterrupt, SystemExit):
        logger.info("Arrêt demandé. Shutdown du scheduler.")
        scheduler.shutdown()
```

---

## ✅ Fonctionnalités incluses

| Fonctionnalité                    | Inclus |
|----------------------------------|--------|
| Logging structuré                | ✅     |
| Monitoring CPU/RAM               | ✅     |
| Gestion d’erreurs avec Sentry    | ✅     |
| Tâche planifiée toutes les X sec | ✅     |
| ThreadPool pour multitâche       | ✅     |
| Gestion des erreurs isolée par tâche | ✅ |

---

## 🧪 Bonus : autres types de tâches possibles

```python
# Tâche à une date précise
scheduler.add_job(scheduled_job, 'date', run_date='2025-03-22 14:00:00')

# Tâche style cron (ex: tous les lundis à 8h)
scheduler.add_job(scheduled_job, 'cron', day_of_week='mon', hour=8, minute=0)
```

---

Souhaites-tu une version avec **persistance en base (SQLite ou Redis)** pour que les tâches survivent au redémarrage ? Ou qu’on intègre des **metrics Prometheus** ou un dashboard Grafana ?