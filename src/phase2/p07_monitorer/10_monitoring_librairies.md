#👌 ! Voici un **même script Python 
## Pour monitorer, instrumenté avec **Sentry**, **Rollbar** et **Bugsnag**, dans **trois versions distinctes**.

### 🧪 Objectif du script

Une fonction `run()` qui plante volontairement avec `1 / 0`, et qu'on veut **monitorer via chaque service** de monitoring pour :

- Capturer les erreurs
- Les envoyer au backend (Sentry, Rollbar ou Bugsnag)
- Les logger localement

---

# 📄 Code 1 : Monitoring avec **Sentry**

## ✅ Prérequis

```bash
pip install sentry-sdk loguru
```

## 🧠 Code

```python
# sentry_example.py
import sentry_sdk
from loguru import logger

# ⚠️ Remplace par ton DSN réel
sentry_sdk.init("https://<public_key>@sentry.io/<project_id>", traces_sample_rate=1.0)

logger.add("sentry.log", rotation="500 KB")

def run():
    logger.info("Début du traitement")
    1 / 0  # Exception volontaire

if __name__ == "__main__":
    try:
        run()
    except Exception as e:
        logger.exception("Une erreur est survenue")
        sentry_sdk.capture_exception(e)
```

---

# 📄 Code 2 : Monitoring avec **Rollbar**

## ✅ Prérequis

```bash
pip install rollbar loguru
```

## 🧠 Code

```python
# rollbar_example.py
import rollbar
from loguru import logger

# ⚠️ Remplace par ton access token
rollbar.init('POST_SERVER_ITEM_ACCESS_TOKEN', environment='development')

logger.add("rollbar.log", rotation="500 KB")

def run():
    logger.info("Début du traitement")
    1 / 0

if __name__ == "__main__":
    try:
        run()
    except Exception as e:
        logger.exception("Une erreur est survenue")
        rollbar.report_exc_info()
```

---

# 📄 Code 3 : Monitoring avec **Bugsnag**

## ✅ Prérequis

```bash
pip install bugsnag loguru
```

## 🧠 Code

```python
# bugsnag_example.py
import bugsnag
from loguru import logger

# ⚠️ Remplace par ta clé API
bugsnag.configure(
    api_key="YOUR_API_KEY_HERE",
    project_root=".",
    release_stage="development",
)

logger.add("bugsnag.log", rotation="500 KB")

def run():
    logger.info("Début du traitement")
    1 / 0

if __name__ == "__main__":
    try:
        run()
    except Exception as e:
        logger.exception("Une erreur est survenue")
        bugsnag.notify(e)
```

---

# 🧪 Résultat attendu pour les trois versions

- L’erreur est logguée localement dans un fichier (`*.log`)
- Elle est transmise au service distant concerné
- Le message d’erreur est visible dans ton dashboard Sentry / Rollbar / Bugsnag

