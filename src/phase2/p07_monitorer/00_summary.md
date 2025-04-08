# ✅ Monitoring

En Python (et en général), **monitorer** le code permet d’observer ce qu’il fait **en temps réel ou a posteriori**, pour :

- Détecter les erreurs et lenteurs
- Optimiser les performances
- Comprendre le comportement applicatif

Voici les **aspects à monitorer**, classés par thème, avec les **outils ou méthodes associées** 👇

---

## 🔧 1. **Erreurs et exceptions**

**À monitorer :**

- Exceptions non capturées
- Traces d'erreurs
- Fréquence des erreurs

**Outils / techniques :**

- Logger les erreurs avec `logging` ou `loguru`
- Envoyer les erreurs à un service comme **Sentry**, **Rollbar** ou **Bugsnag**

```python
import logging

logging.basicConfig(level=logging.ERROR)
try:
    1 / 0
except Exception as e:
    logging.exception("Une erreur est survenue")
```

---

## 🐢 2. **Performance et temps d’exécution**

**À monitorer :**

- Temps d’exécution d’un bloc de code
- Fonctions lentes ou bloquantes
- Goulots d’étranglement

**Outils / techniques :**

- `time`, `timeit`, `cProfile`, `line_profiler`
- Librairies : [`pyinstrument`](https://github.com/joerick/pyinstrument), [`viztracer`](https://github.com/gaogaotiantian/viztracer)
- cProfile : https://docs.python.org/3/library/profile.html

```python
import time

start = time.time()
# Code à mesurer
time.sleep(0.2)
print(f"Durée : {time.time() - start:.3f}s")
```

---

## 📈 3. **Utilisation des ressources (RAM, CPU, IO)**

**À monitorer :**

- Mémoire utilisée
- Charge CPU
- Accès disque / réseau

**Outils :**

- [`psutil`](https://github.com/giampaolo/psutil) (monitoring système)
- `tracemalloc` (profiling mémoire)
- `memory_profiler` pour voir la RAM par ligne

```python
import psutil

print("RAM utilisée (Mo) :", psutil.Process().memory_info().rss / 1e6)
print("CPU (%) :", psutil.cpu_percent(interval=1))
```

---

## 💬 4. **Logs et traces**

**À monitorer :**

- Actions métier (utilisateur, traitement, etc.)
- Événements déclenchés
- Chronologie

**Outils :**

- `logging`, [`loguru`](https://github.com/Delgan/loguru) (plus moderne)
- Intégration avec Elastic / Graylog / Datadog

```python
from loguru import logger

logger.info("Traitement démarré")
```

---

## 🔄 5. **Appels externes (API, DB, etc.)**

**À monitorer :**

- Temps de réponse des APIs
- Nombre d'appels
- Erreurs réseau ou SQL

**Outils :**

- Middleware de tracing HTTP (ex : `requests_toolbelt`, `httpx`)
- Intégration avec APM (ex: New Relic, Datadog, OpenTelemetry)

```python
import requests
import time

start = time.time()
resp = requests.get("https://api.github.com")
print(f"API répondue en {time.time() - start:.3f}s")
```

---

## 🔎 6. **État de l'application (health check)**

**À monitorer :**

- L’application est-elle toujours vivante ?
- Les threads/process sont-ils actifs ?
- Services dépendants sont-ils OK ?

**Outils :**

- Ping/heartbeat régulier
- Endpoints `/healthz`
- Watchdog / supervisor

---

## 🧪 7. **Tests et couverture**

**À monitorer :**

- Combien de tests passent / échouent ?
- Quelle part du code est testée ?
- Régressions ?

**Outils :**

- `pytest`, `unittest`
- `coverage.py`, `pytest-cov`

---

## 📊 8. **Indicateurs métier (KPIs)**

**À monitorer :**

- Nombre d'utilisateurs / requêtes / opérations par minute
- Échecs fonctionnels (ex: paiement échoué, tâche rejetée)
- Taux de succès global

**Outils :**

- Compteurs via Prometheus / Grafana
- Logs structurés envoyés vers un ELK stack
- InfluxDB, Datadog…

---

## 🧰 9. **Surveillance live (observabilité)**

**Tu peux intégrer :**

- **Prometheus** (scraping + métriques)
- **Grafana** (dashboards temps réel)
- **OpenTelemetry** (standard tracing/logs/metrics)
- **Datadog**, **New Relic**, **Elastic APM**, etc.

