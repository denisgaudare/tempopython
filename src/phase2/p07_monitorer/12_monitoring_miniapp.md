# ✅ Petite app réelle Python**, style "mini service CLI", qui :

- 👤 demande un nom d’utilisateur,
- 🔢 demande un âge,
- 💥 plante si l’âge est invalide (non entier ou négatif),
- 🛠️ et envoie **les erreurs à Sentry, Rollbar et Bugsnag**,
- 📝 enregistre aussi les logs localement.

---

# 🧰 Mini-app "inscription" (avec monitoring)

## 📁 Arborescence

```
mini_app_monitoring/
├── main.py
├── monitor.py
├── config.py
├── requirements.txt
└── logs/
    └── app.log
```

---

## 📦 `requirements.txt`

```txt
loguru
sentry-sdk
rollbar
bugsnag
```

---

## ⚙️ `config.py`

```python
SENTRY_DSN = "https://<your_sentry_dsn>"
ROLLBAR_TOKEN = "<your_rollbar_token>"
BUGSNAG_API_KEY = "<your_bugsnag_key>"
```

---

## 🛡️ `monitor.py`

```python
from loguru import logger
import sentry_sdk
import rollbar
import bugsnag
import config

logger.add("logs/app.log", rotation="500 KB")

# Init Sentry
sentry_sdk.init(dsn=config.SENTRY_DSN, traces_sample_rate=1.0)

# Init Rollbar
rollbar.init(config.ROLLBAR_TOKEN, environment="dev")

# Init Bugsnag
bugsnag.configure(api_key=config.BUGSNAG_API_KEY)

def report_exception(e):
    logger.exception("Erreur capturée :")
    sentry_sdk.capture_exception(e)
    rollbar.report_exc_info()
    bugsnag.notify(e)
```

---

## 🧠 `main.py`

```python
from monitor import logger, report_exception

def run():
    logger.info("🔧 Démarrage de l’application")

    name = input("Entrez votre nom : ").strip()
    age_input = input("Entrez votre âge : ").strip()

    if not age_input.isdigit():
        raise ValueError("Âge invalide : ce n’est pas un entier positif.")

    age = int(age_input)
    if age < 0:
        raise ValueError("Âge invalide : négatif.")

    logger.info(f"✅ Inscription réussie pour {name}, {age} ans.")

if __name__ == "__main__":
    try:
        run()
    except Exception as e:
        report_exception(e)
        print("❌ Une erreur est survenue. Elle a été signalée au support.")
```

---

## ▶️ Exécution

```bash
python main.py
```

- Entre un nom normal
- Puis un âge non entier (`trente`) ou négatif (`-3`)
- Tu verras l’erreur dans le terminal et elle sera **logguée + envoyée** à tous les services.

---

## ✅ Résumé

| Fonction                    | Inclus |
|----------------------------|--------|
| Interaction utilisateur    | ✅     |
| Logs structurés            | ✅     |
| Gestion d’erreurs multi-monitoring | ✅ (Sentry, Rollbar, Bugsnag) |
| Fichier de log persistant  | ✅     |
| Déployable en local & cloud | ✅     |
