# ✅ Utiliser [`rich`](https://rich.readthedocs.io/en/stable/) pour améliorer la **gestion et l'affichage des exceptions en Python** avec un **visuel coloré et lisible**, super utile en dev ou en ligne de commande.

---

# 🎨 `rich` pour la gestion des exceptions

## ✅ Ce que ça permet

- Afficher les **exceptions avec des couleurs et un joli stack trace**
- Rendre les erreurs plus lisibles dans la console
- Utilisable avec ou sans framework
- Peut s'intégrer dans un logger custom

---

## 📦 Installation

```bash
pip install rich
```

---

## 🔥 Exemple simple : `rich.traceback.install()`

```python
from rich.traceback import install

# Active le rendu d'erreur enrichi pour toutes les exceptions
install()

def division():
    return 1 / 0

division()
```

Résultat en console 👇

```
Traceback (most recent call last):
  File "main.py", line 8, in <module>
    division()
  File "main.py", line 5, in division
    return 1 / 0
ZeroDivisionError: division by zero
```

...avec couleurs, numéro de ligne, extraits de code, etc. 🌈

---

## 🧠 Exemple avec `try/except` et affichage manuel

```python
from rich.console import Console
from rich.traceback import Traceback

console = Console()

try:
    1 / 0
except Exception:
    tb = Traceback(show_locals=True)
    console.print(tb)
```

---

## 🧰 Pour usage plus avancé (lib / app)

Tu peux créer une fonction d'affichage global des exceptions :

```python
# rich_handler.py
from rich.console import Console
from rich.traceback import install

console = Console()
install(show_locals=True)

def report_exception(e):
    console.print_exception()
```

Et dans ton script :

```python
from rich_handler import report_exception

try:
    raise ValueError("Erreur critique")
except Exception as e:
    report_exception(e)
```

---

## ✨ Bonus : intégration avec `loguru`

Tu peux aussi rediriger les logs vers la console `rich` :

```python
from loguru import logger
from rich.console import Console

console = Console()

logger.remove()
logger.add(console.print, level="INFO")
logger.info("Hello depuis loguru + rich")
```

---

## 🧩 En résumé

| Fonction                 | Comment utiliser                |
|--------------------------|---------------------------------|
| Exception auto en couleur | `rich.traceback.install()`      |
| Affichage manuel         | `console.print_exception()`     |
| Stack avec variables     | `Traceback(show_locals=True)`   |
| Intégration logging      | Rediriger loguru vers `console` |

