import time
from concurrent.futures import ThreadPoolExecutor, TimeoutError
from monitor import logger, log_resources
from config import WORKER_INTERVAL, TASK_TIMEOUT, MAX_WORKERS
from tasks import example_task

def run_task_with_timeout(executor, fn, *args, timeout=10):
    future = executor.submit(fn, *args)
    try:
        future.result(timeout=timeout)
    except TimeoutError:
        logger.warning("⏱️ Tâche expirée (timeout)")
    except Exception as e:
        logger.error(f"❌ Erreur dans la tâche : {e}")

if __name__ == "__main__":
    logger.info("=== WORKER ROBUSTE DÉMARRÉ ===")
    executor = ThreadPoolExecutor(max_workers=MAX_WORKERS)
    task_id = 1

    while True:
        start_time = time.time()
        logger.info(f"⏳ Lancement tâche #{task_id}")
        log_resources()

        run_task_with_timeout(executor, example_task, task_id, timeout=TASK_TIMEOUT)

        duration = time.time() - start_time
        logger.info(f"🕒 Tâche #{task_id} terminée en {duration:.2f}s")

        pause = max(0, WORKER_INTERVAL - duration)
        logger.info(f"⏸️ Attente de {pause:.2f}s avant la prochaine tâche\n")
        time.sleep(pause)

        task_id += 1
