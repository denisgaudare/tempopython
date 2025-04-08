import os

WORKER_INTERVAL = int(os.getenv("WORKER_INTERVAL", 10))       # En secondes
TASK_TIMEOUT = int(os.getenv("TASK_TIMEOUT", 5))               # Timeout max par tâche
MAX_WORKERS = int(os.getenv("MAX_WORKERS", 2))                 # Thread pool
LOG_PATH = os.getenv("LOG_PATH", "logs/worker.log")
SENTRY_DSN = os.getenv("SENTRY_DSN", "")
