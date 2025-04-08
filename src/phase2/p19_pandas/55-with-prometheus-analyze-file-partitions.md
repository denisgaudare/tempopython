Traitement concurrentiel avec Prometheus **sans erreur de doublons** — prêt à être exécuté dans un script Python localement 👇

---

### ✅ **Script avec Prometheus + Dask-style traitement par fichier**

```python
import pandas as pd
import time
import random
import os
import concurrent.futures
from prometheus_client import CollectorRegistry, start_http_server, Summary, Counter, generate_latest

# Créer un registre Prometheus personnalisé (évite les doublons si tu réexécutes le script)
registry = CollectorRegistry()

# Définition des métriques
FILE_PROCESS_TIME = Summary(
    "file_process_time_seconds", 
    "Temps de traitement d'un fichier CSV", 
    registry=registry
)
FILES_PROCESSED = Counter(
    "files_processed_total", 
    "Nombre total de fichiers traités", 
    registry=registry
)
ROWS_PROCESSED = Counter(
    "rows_processed_total", 
    "Nombre total de lignes traitées", 
    registry=registry
)

# Traitement avec métriques
@FILE_PROCESS_TIME.time()
def process_file_with_metrics(path):
    df = pd.read_csv(path, parse_dates=["date"])
    ROWS_PROCESSED.inc(len(df))
    df = df[df["montant"] > 500]
    result = df.groupby("categorie")["montant"].mean()
    FILES_PROCESSED.inc()
    time.sleep(random.uniform(0.1, 0.3))  # Simulation d'un traitement
    return result

def main():
    # Dossier avec les fichiers CSV
    input_dir = "big_transactions"
    files = [os.path.join(input_dir, f) for f in os.listdir(input_dir) if f.endswith(".csv")]

    # Lancer le serveur Prometheus sur le port 9000
    start_http_server(9000, registry=registry)
    print("Prometheus disponible sur http://localhost:9000/metrics")

    # Traitement parallèle des fichiers
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        for r in executor.map(process_file_with_metrics, files):
            results.append(r)

    # Fusion des résultats
    summary_df = pd.concat(results).groupby(level=0).mean()
    summary_df.to_csv("aggregated_metrics.csv")
    print("Fichier agrégé écrit dans aggregated_metrics.csv")

if __name__ == "__main__":
    main()
```

---

## 🧪 Tu peux ensuite :
- Lancer ce script
- Accéder aux métriques : [http://localhost:9000/metrics](http://localhost:9000/metrics)
- Ajouter cette cible dans Prometheus :

```yaml
scrape_configs:
  - job_name: 'python_csv_processor'
    static_configs:
      - targets: ['localhost:9000']
```

Tu veux aussi un exemple de **dashboard Grafana** avec ces métriques ?