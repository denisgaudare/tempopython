Voici une **solution complète avec Celery**, 
adaptée pour des tâches Python distribuées, planifiées ou asynchrones.  
Elle inclut : 
    monitoring, 
    logs, 
    erreurs, 
    timeout, 
    planification périodique
    possibilité de scaling.

---

# 🍒 Solution Celery Complète (avec monitoring, logs, planification)

---

## 🔧 À quoi sert Celery ?

Celery est une **librairie de gestion de workers distribués**, idéale pour :
- Exécuter des **tâches en arrière-plan**
- **Planifier** des tâches (avec `celery-beat`)
- **Distribuer la charge** (multi-nœuds / Docker / cloud)
- Gérer la **reprise après crash**

---

## 📦 Dépendances

On part sur :
- **Celery** avec **Redis** comme broker
- **loguru** pour les logs
- **sentry-sdk** pour la gestion des erreurs
- **psutil** pour le monitoring local
- **celery[redis]**, **celery[beat]** pour le scheduling

---

## 🗂️ Arborescence du projet

```
celery_worker_project/
├── tasks/
│   ├── __init__.py
│   ├── monitor.py
│   └── jobs.py
├── worker.py
├── beat_scheduler.py
├── config.py
├── requirements.txt
└── logs/
    └── celery.log
```

---

## 📄 `requirements.txt`

```txt
celery[redis]
psutil
loguru
sentry-sdk
```

---

## ⚙️ `config.py`

```python
import os

BROKER_URL = os.getenv("BROKER_URL", "redis://localhost:6379/0")
LOG_PATH = os.getenv("LOG_PATH", "logs/celery.log")
SENTRY_DSN = os.getenv("SENTRY_DSN", "")
```

---

## 📋 `tasks/monitor.py`

```python
from loguru import logger
import psutil
import sentry_sdk
from config import LOG_PATH, SENTRY_DSN

logger.add(LOG_PATH, rotation="1 MB", retention="7 days", level="INFO")

if SENTRY_DSN:
    sentry_sdk.init(dsn=SENTRY_DSN)

def log_resources():
    process = psutil.Process()
    mem = process.memory_info().rss / 1e6
    cpu = psutil.cpu_percent(interval=0.1)
    logger.info(f"[RESOURCES] RAM: {mem:.2f} MB | CPU: {cpu}%")

def monitor_exceptions(fn):
    def wrapper(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except Exception as e:
            logger.exception("Erreur dans une tâche Celery")
            sentry_sdk.capture_exception(e)
            raise
    return wrapper
```

---

## 📋 `tasks/jobs.py`

```python
import time
from celery import shared_task
from .monitor import logger, log_resources, monitor_exceptions

@shared_task(bind=True, name="tasks.process_data", soft_time_limit=10)
@monitor_exceptions
def process_data(self, job_id):
    logger.info(f"🔧 Tâche #{job_id} lancée")
    log_resources()
    time.sleep(3)  # Simulation de traitement
    logger.info(f"✅ Tâche #{job_id} complétée")
```

---

## 🔁 `worker.py`

```python
from celery import Celery
from config import BROKER_URL

app = Celery("worker", broker=BROKER_URL)
app.config_from_object("tasks.settings")  # Pour options avancées

# Auto-découverte des tâches dans tasks/
app.autodiscover_tasks(["tasks"])

if __name__ == "__main__":
    app.worker_main()
```

---

## ⏰ `beat_scheduler.py` (planification)

```python
from celery import Celery
from celery.schedules import crontab
from config import BROKER_URL

app = Celery("beat", broker=BROKER_URL)
app.config_from_object("tasks.settings")
app.autodiscover_tasks(["tasks"])

app.conf.beat_schedule = {
    "run-process-data-every-30s": {
        "task": "tasks.process_data",
        "schedule": 30.0,
        "args": [42],
    },
    # Exemple cron : tous les jours à 8h
    # "daily-job": {
    #     "task": "tasks.process_data",
    #     "schedule": crontab(hour=8, minute=0),
    #     "args": [99],
    # },
}
```

---

## ⚙️ `tasks/settings.py` (optionnel)

```python
task_serializer = "json"
accept_content = ["json"]
result_backend = None
worker_prefetch_multiplier = 1
task_acks_late = True
```

---

## ▶️ Lancement

**Démarrer Redis (via Docker ou local)** :

```bash
docker run -d -p 6379:6379 redis
```

**Lancer le worker :**

```bash
celery -A worker worker --loglevel=info
```

**Lancer le scheduler (beat) :**

```bash
celery -A beat_scheduler beat --loglevel=info
```

---

## ✅ Fonctionnalités incluses

| Fonction                    | Inclus |
|----------------------------|--------|
| Worker Celery + Redis      | ✅     |
| Monitoring CPU / RAM       | ✅     |
| Logs persistants            | ✅     |
| Gestion d'erreurs Sentry   | ✅     |
| Timeout par tâche (soft)   | ✅     |
| Planification régulière    | ✅     |
| Tâches distribuées         | ✅     |
