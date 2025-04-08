import time
from monitor import logger, monitor_exceptions

@monitor_exceptions
def example_task(task_id: int):
    logger.info(f"🛠️  Tâche {task_id} démarrée")
    time.sleep(2)
    logger.info(f"✅ Tâche {task_id} terminée")


