# ✅ Exemple concret d’utilisation de Datadog** en Python pour monitorer un script ou une application.

### ⚙️ **Contexte**  
A partir d'un script Python (batch ou worker) et tu veux envoyer des **metrics personnalisées**, des **logs**, ou encore des **traces** à **Datadog** pour surveiller son comportement.

---

## ✅ 1. **Installation**

```bash
pip install datadog
```

---

## 📦 2. **Configuration du client**

```python
from datadog import initialize, api

options = {
    "api_key": "ta_clé_api",
    "app_key": "ta_clé_app"
}

initialize(**options)
```

⚠️ Les clés sont à récupérer depuis [Datadog > API Keys](https://app.datadoghq.com/account/settings#api)

---

## 📊 3. **Envoyer une métrique personnalisée**

```python
from datadog import api

# Envoie une métrique (ex: temps de traitement)
api.Metric.send(
    metric='mon_app.temps_traitement',
    points=123.4,  # ou [(timestamp, valeur)]
    tags=["env:dev", "tache:import_csv"],
    type="gauge"
)
```

---

## 📋 4. **Envoyer un log (optionnel, si tu as le Datadog Agent)**

Si tu as installé le **Datadog Agent**, tu peux simplement logger dans stdout/stderr, et configurer ton script pour envoyer les logs via l'agent.

Sinon, tu peux envoyer des logs via l’API HTTP :

```python
import requests
import json

log_entry = {
    "message": "Import terminé avec succès",
    "ddsource": "python",
    "hostname": "mon-serveur",
    "service": "import-csv",
    "status": "info"
}

requests.post(
    "https://http-intake.logs.datadoghq.com/v1/input",
    headers={
        "Content-Type": "application/json",
        "DD-API-KEY": "ta_clé_api"
    },
    data=json.dumps(log_entry)
)
```

---

## 🔁 5. **Utiliser les intégrations de traces (APM)**

Si tu veux **tracer un workflow**, par exemple une tâche async ou un appel API, tu peux utiliser `ddtrace` :

```bash
pip install ddtrace
```

```python
from ddtrace import tracer

@tracer.wrap()
def traiter_fichier():
    # ton traitement ici
    pass
```

---

## 💡 Exemple combiné dans un worker :

```python
import time
from datadog import initialize, api

initialize(api_key="ta_api_key", app_key="ta_app_key")

def traiter_fichier(nom_fichier):
    debut = time.time()
    print(f"Traitement de {nom_fichier}")
    time.sleep(1.2)  # simulation
    duree = time.time() - debut

    api.Metric.send(
        metric='worker.temps_traitement',
        points=duree,
        tags=["fichier:" + nom_fichier]
    )
    print(f"{nom_fichier} traité en {duree:.2f}s")

traiter_fichier("data.csv")
```
