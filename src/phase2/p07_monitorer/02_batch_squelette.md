# ✅ Projet pour un script batch** avec du monitoring intégré, puis je te proposerai celui orienté **scheduler / worker**.

---

# 🗂️ Squelette : Script Batch Python avec Monitoring

### 📁 Arborescence

```
my_batch_project/
├── main.py
├── monitor.py
├── config.py
├── requirements.txt
└── logs/
    └── app.log
```

---

### 📄 `requirements.txt`

```txt
loguru
psutil
sentry-sdk
```

---

### ⚙️ `config.py`

```python
import os

LOG_PATH = os.getenv("LOG_PATH", "logs/app.log")
SENTRY_DSN = os.getenv("SENTRY_DSN", "")  # Ajouter ton DSN Sentry ici
```

---

### 📋 `monitor.py`

```python
from loguru import logger
import psutil
import sentry_sdk
from config import LOG_PATH, SENTRY_DSN

# Setup Logging
logger.add(LOG_PATH, rotation="1 MB", retention="7 days", level="INFO")

# Setup Sentry
if SENTRY_DSN:
    sentry_sdk.init(dsn=SENTRY_DSN)

def log_resource_usage():
    process = psutil.Process()
    mem_mb = process.memory_info().rss / 1e6
    cpu = psutil.cpu_percent(interval=0.1)
    logger.info(f"[RESOURCE] RAM: {mem_mb:.2f} MB | CPU: {cpu}%")

def monitor_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.exception("Erreur inattendue")
            sentry_sdk.capture_exception(e)
            raise
    return wrapper
```

---

### 🧠 `main.py`

```python
import time
from monitor import logger, log_resource_usage, monitor_errors

@monitor_errors
def run_batch():
    logger.info("Traitement batch démarré")
    time.sleep(2)  # Simulation
    result = 1 / 0  # Provoque une erreur pour test
    logger.info(f"Résultat : {result}")

if __name__ == "__main__":
    logger.info("==== SCRIPT LANCÉ ====")
    log_resource_usage()
    run_batch()
    logger.info("==== SCRIPT TERMINÉ ====")
```

---

Tu peux l'exécuter via :  
```bash
python main.py
```