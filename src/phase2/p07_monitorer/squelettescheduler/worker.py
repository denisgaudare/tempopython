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
