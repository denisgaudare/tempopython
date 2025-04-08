# **Frameworks et librairies Python sous-estimés** mais **très pratiques**, selon les domaines. Certains sont des pépites souvent éclipsées par des outils plus populaires :
# non https://docs.python.org/3/library/index.html
---

### 🔧 **Outils utilitaires et helpers**
- **`boltons`** : Une collection de petites fonctions utilitaires très bien conçues (inspirées de `toolz` et `collections`).
- **`funcy`** : Programmation fonctionnelle légère pour Python (map/filter, memoization, etc.) avec une API claire.
- **`more-itertools`** : Une extension puissante à `itertools`, avec plein de fonctions géniales pour manipuler les itérables.
https://pypi.org/project/more-itertools/
---

### 🗂️ **Traitement de données / fichiers**
- **`pyjanitor`** : Une surcouche à pandas pour écrire du code plus lisible façon "chainable verbs" (comme `clean_names()`, `remove_columns()`).
- **`datatable`** : Un concurrent à pandas, très rapide pour les gros jeux de données (inspiré de R).
- **`mimesis`** : Générateur de données fake ultra complet (plus rapide et localisé que Faker parfois).
- **`glom`** : Pour manipuler des structures de données profondes (JSON, dicts imbriqués) avec une syntaxe expressive.

---

### 🧪 **Tests**
- **`hypothesis`** : Test basé sur la génération automatique de données — très puissant pour détecter des bugs improbables.
- **`testcontainers`** : Lancer des bases de données ou services dans des conteneurs Docker pendant les tests.

---

### 🌐 **Web / API**
- **`apistar`** : Framework API minimaliste basé sur la validation de schéma — très propre, même s’il a été abandonné.
- **`responder`** : Créé par l’auteur de `requests`, un mini framework web async, élégant et rapide.
- **`httpx`** : Une alternative à `requests`, mais en supportant HTTP/2, l’async et plus de fonctionnalités modernes.

---

### ⏲️ **Batch, CLI, scheduling**
- **`rich`** : CLIs pluis userfriendly.
- **`rich-click`** : Combine la puissance de Click avec l’esthétique de Rich pour des CLIs plus belles.
- **`schedule`** : Pour planifier des tâches de façon humaine (`schedule.every().day.at("10:30").do(job)`).
- **`prefect`** : Moins connu que Airflow, très bon pour des workflows de data science / ETL simples et lisibles.

---

### 🎨 **Graphique / Image / UI**
- **`Pillow`** : LA librairie de manip images
- **`drawsvg`** : Manipulation et création de SVG en Python (simple et efficace).
- **`textual`** / **`textualize/rich`** : Framework TUI (terminal UI) pour créer des interfaces riches dans un terminal.
- **`dearpygui`** : UI native rapide et scriptable pour du prototypage graphique en Python.

---

### 🧠 **IA / Maths / Algèbre**
- **`sympy`** : Très pratique pour faire du calcul symbolique en Python (résolution d’équations, dérivées...).
- **`numba`** : Compile du code Python en natif (LLVM), super utile pour accélérer les boucles numpy.
- **`tinygrad`** : Une implémentation pédagogique mais fonctionnelle d’un moteur de deep learning minimaliste.

---
