from loguru import logger
import psutil
import sentry_sdk
from config import LOG_PATH, SENTRY_DSN

# Setup Logging (loguru)
logger.add(LOG_PATH, rotation="1 MB", retention="7 days", level="INFO")

# Setup Sentry
if SENTRY_DSN:
    sentry_sdk.init(dsn=SENTRY_DSN)

def log_resource_usage():
    process = psutil.Process()
    mem_mb = process.memory_info().rss / 1e6
    cpu = psutil.cpu_percent(interval=0.1)
    thr = process.num_threads()
    logger.info(f"[RESOURCE] RAM: {mem_mb:.2f} MB | CPU: {cpu}%, | Threads: {thr}%")

def monitor_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.exception("Erreur inattendue")
            sentry_sdk.capture_exception(e)
            raise
    return wrapper
