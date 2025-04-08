# ✅ [**OpenTelemetry**](https://opentelemetry.io/) est une solution standard moderne pour l’**observabilité** : traçabilité, métriques, logs — tout en un, compatible avec **Prometheus**, **Jaeger**, **Zipkin**, **Grafana**, etc.

# 📡 OpenTelemetry pour Python — Guide express

## 🎯 À quoi ça sert ?

| Ce que tu veux monitorer | OpenTelemetry permet de…             |
|--------------------------|--------------------------------------|
| 🔄 Traçabilité des appels | Générer des **traces distribuées**    |
| 📊 Métriques système/app | Exposer des **métriques Prometheus** |
| 📝 Logs enrichis         | Structurer et exporter les logs      |

---

## 🧰 Installation de base

```bash
pip install opentelemetry-api opentelemetry-sdk
```

Tu peux ensuite ajouter des **exporteurs**, ex :

```bash
pip install opentelemetry-exporter-otlp
pip install opentelemetry-exporter-prometheus
pip install opentelemetry-exporter-jaeger
```

---

## 🚀 Exemple minimal : Tracing (local)

```python
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor, ConsoleSpanExporter

# Init
trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)
trace.get_tracer_provider().add_span_processor(
    SimpleSpanProcessor(ConsoleSpanExporter())
)

# Exemple de trace
with tracer.start_as_current_span("traitement"):
    print("Tâche en cours...")
```

👉 Cela affiche une trace **dans la console**, mais tu peux facilement **l’envoyer ailleurs (Jaeger, Zipkin, etc.)**.

---

## 📊 Exemple : Métriques Prometheus

```bash
pip install opentelemetry-exporter-prometheus
```

```python
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import (
    PeriodicExportingMetricReader,
)
from opentelemetry.exporter.prometheus import PrometheusExporter
from prometheus_client import start_http_server

# Start HTTP server for scraping
start_http_server(8000)

exporter = PrometheusExporter()
reader = PeriodicExportingMetricReader(exporter)
provider = MeterProvider(metric_readers=[reader])
meter = provider.get_meter(__name__)

counter = meter.create_counter("taches_total")

counter.add(1, {"type": "traitement"})
```

🟢 Accès aux métriques Prometheus : [http://localhost:8000/metrics](http://localhost:8000/metrics)

---

## 🔧 Exemple avec Flask

```bash
pip install opentelemetry-instrumentation-flask
```

```python
from flask import Flask
from opentelemetry.instrumentation.flask import FlaskInstrumentor

app = Flask(__name__)
FlaskInstrumentor().instrument_app(app)

@app.route("/")
def index():
    return "Hello OpenTelemetry!"
```

➡️ Cela trace automatiquement les routes Flask dans OpenTelemetry.

---

## 🧩 Exporters disponibles

| Backend       | Exporter Py                              |
|---------------|-------------------------------------------|
| 🐘 **Jaeger**     | `opentelemetry-exporter-jaeger`         |
| 📦 **Zipkin**     | `opentelemetry-exporter-zipkin`         |
| 🧠 **OTLP (Grafana, NewRelic…)** | `opentelemetry-exporter-otlp` |
| 📊 **Prometheus** | `opentelemetry-exporter-prometheus`     |
| 📄 **Console**    | `ConsoleSpanExporter`, `ConsoleMetricExporter` |

---

## ✅ Tu peux instrumenter…

| Élément                    | Instrumentation automatique |
|----------------------------|-----------------------------|
| Flask / FastAPI / Django   | ✅                          |
| Requests / urllib / httpx  | ✅                          |
| SQLAlchemy / psycopg2      | ✅                          |
| Redis, Kafka, Celery       | ✅ via plugins              |

---

## 🎁 Bonus : instrumentation auto

```bash
opentelemetry-instrument python my_app.py
```

✅ Cela instrumente automatiquement ton code, sans modifier le source, si tu as installé les bons plugins.

---

## 🚀 En résumé

| Besoin                         | Ce qu’OpenTelemetry offre               |
|-------------------------------|-----------------------------------------|
| Logs enrichis                 | avec `structured_logging`, OTLP        |
| Traces distribuées            | via spans, context, exporters           |
| Métriques Prometheus          | via exporters                           |
| Compatibilité avec Grafana    | via OTLP ou Prometheus scrape           |
| Monitoring complet & standard | ✅                                      |
