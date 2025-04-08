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
