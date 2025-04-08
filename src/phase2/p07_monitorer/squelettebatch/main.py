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
