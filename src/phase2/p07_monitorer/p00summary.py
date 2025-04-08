import logging
from prometheus_client import Counter, start_http_server

LOG_ERRORS = Counter("log_errors_total", "Nombre de logs de niveau ERROR")

from prometheus_client import *
class PrometheusLoggingHandler(logging.Handler):
    def emit(self, record):
        if record.levelno == logging.ERROR:
            LOG_ERRORS.inc()

# 1. Créer un logger principal
logger = logging.getLogger("mon_app")
logger.setLevel(logging.DEBUG)  # niveau minimal pris en compte

# 2. Handler console : affiche que les WARNING+
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)

# 3. Handler fichier : enregistre tout (DEBUG+)
file_handler = logging.FileHandler("app.log")
file_handler.setLevel(logging.DEBUG)

#Envoi vers prometheus
logger.addHandler(PrometheusLoggingHandler())
# 4. Ajouter un filtre au file handler (optionnel)
class OnlyInfoAndAbove(logging.Filter):
    def filter(self, record):
        return record.levelno >= logging.INFO

#file_handler.addFilter(OnlyInfoAndAbove())

# 5. Formatage
formatter = logging.Formatter("[%(asctime)s] %(levelname)s - %(message)s")

console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# 6. Attacher les handlers au logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# 7. Log de test
logger.debug("Message DEBUG")
logger.info("Message INFO")
logger.warning("Message WARNING")
logger.error("Message ERROR")

#start_http_server(8000)

#Profiling

# utilisation
import cProfile
import re
#cProfile.run('re.compile("foo|bar")')


cProfile.run('re.compile("foo|bar")', 're_stats')
import pstats
from pstats import SortKey
p = pstats.Stats('re_stats')
p.strip_dirs().sort_stats(-1).print_stats()