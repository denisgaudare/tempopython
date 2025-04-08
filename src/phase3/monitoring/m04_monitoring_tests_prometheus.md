Yes ! Je te montre comment **intégrer Prometheus dans ton projet Python** pour **exposer des métriques de tests ou de performance** (et les visualiser ensuite avec Grafana).

---

## 🧪 Objectif
- Tu as des fonctions Python que tu veux **monitorer** (durée d'exécution, nombre d'appels, erreurs, etc.)
- Tu veux les exposer en **HTTP via Prometheus**
- Bonus : tu pourras connecter Grafana dessus si tu veux des dashboards

---

## 📦 1. Installation des packages

Ajoute dans ton `requirements.txt` :

```txt
prometheus_client
```

Installe :
```bash
pip install prometheus_client
```

---

## ⚙️ 2. Exemple de fichier avec instrumentation

```python
# mon_module/metrics_app.py

from prometheus_client import start_http_server, Counter, Histogram
import time
import random

# Compteur du nombre total d'appels
REQUEST_COUNT = Counter("test_requests_total", "Nombre de tests exécutés")

# Histogramme pour la durée d’exécution
EXEC_TIME = Histogram("test_exec_duration_seconds", "Durée des tests")

# Exemple de fonction instrumentée
@EXEC_TIME.time()
def simulated_test_case():
    REQUEST_COUNT.inc()
    duration = random.uniform(0.1, 0.5)
    time.sleep(duration)
    if random.random() < 0.1:
        raise Exception("Test échoué")

if __name__ == "__main__":
    print("Serveur Prometheus en cours d'exécution sur http://localhost:8000/metrics")
    start_http_server(8000)  # Lancer le serveur d'exposition Prometheus

    while True:
        try:
            simulated_test_case()
        except Exception as e:
            print("❌", e)
```

---

## 🌐 3. Lancer le script

```bash
python mon_module/metrics_app.py
```

🔗 Va ensuite sur [http://localhost:8000/metrics](http://localhost:8000/metrics)

Tu y verras des lignes comme :
```
# HELP test_requests_total Nombre de tests exécutés
# TYPE test_requests_total counter
test_requests_total 17

# HELP test_exec_duration_seconds Durée des tests
# TYPE test_exec_duration_seconds histogram
test_exec_duration_seconds_count 17
test_exec_duration_seconds_sum 5.674
...
```

---

## 📈 4. Côté Prometheus

Ajoute cette cible à ton `prometheus.yml` :

```yaml
scrape_configs:
  - job_name: 'python-app'
    static_configs:
      - targets: ['localhost:8000']
```

Puis relance Prometheus :
```bash
./prometheus --config.file=prometheus.yml
```

---

## 🎨 5. Et Grafana ?

Tu connectes Prometheus comme datasource, et tu peux créer des dashboards avec :
- Nombre de tests exécutés
- Temps moyen de test
- Histogrammes de temps d’exécution

---

## ➕ BONUS : exposer les erreurs avec `Counter`

Ajoute un compteur pour les erreurs :

```python
ERRORS = Counter("test_errors_total", "Nombre de tests échoués")

try:
    simulated_test_case()
except Exception as e:
    ERRORS.inc()
```

---

Souhaites-tu que je te fasse une version orientée **API Flask ou FastAPI** avec Prometheus intégré, ou tu veux rester sur des scripts Python classiques pour le moment ?