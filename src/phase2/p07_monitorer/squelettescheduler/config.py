import os

WORKER_INTERVAL = int(os.getenv("WORKER_INTERVAL", 10))  # secondes
LOG_PATH = os.getenv("LOG_PATH", "logs/worker.log")
SENTRY_DSN = os.getenv("SENTRY_DSN", "")

