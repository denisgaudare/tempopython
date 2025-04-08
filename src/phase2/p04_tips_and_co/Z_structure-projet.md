## 📂 **Structure d'un projet Python standard**
Voici une structure typique pour un projet Python bien organisé :

```
my_project/                # Nom du projet
│── src/                   # Contient le code source principal
│   ├── my_package/        # Le package principal (même nom que le projet)
│   │   ├── __init__.py    # Fichier permettant d'importer le package
│   │   ├── module1.py     # Un module
│   │   ├── module2.py     # Un autre module
│   │   ├── utils.py       # Fonctions utilitaires
│   ├── main.py            # Point d’entrée du programme (si script)
│
│── tests/                 # Dossier des tests unitaires
│   ├── test_module1.py    # Tests pour module1.py
│   ├── test_module2.py    # Tests pour module2.py
│
│── docs/                  # Documentation du projet
│   ├── index.md           # Documentation principale
│
│── scripts/               # Scripts d'automatisation (optionnel)
│   ├── setup_db.py        # Exemple : script pour initialiser une base de données
│
│── requirements.txt       # Dépendances (pip)
│── pyproject.toml         # Métadonnées du projet (remplace setup.py pour Poetry)
│── setup.py               # Configuration d'installation (si distribution via pip)
│── setup.cfg              # Configuration additionnelle
│── MANIFEST.in            # Liste des fichiers à inclure dans le package
│── .gitignore             # Fichiers à exclure du versionnement
│── README.md              # Description du projet
│── LICENSE                # Licence open source
│── .flake8                # Configuration pour Flake8 (linter)
│── .pre-commit-config.yaml# Configuration des hooks de pre-commit
│── .github/               # Actions GitHub (CI/CD)
│── Dockerfile             # Fichier pour Docker (si besoin)
│── Makefile               # Automatisation des tâches
│── tox.ini                # Configuration pour tests multi-environnements
```

---

## 🔥 **Détails des éléments clés**

### 1️⃣ **Répertoire du code source (`src/`)**
👉 **Pourquoi `src/` ?**
- Évite les conflits avec les imports lorsque le projet est exécuté à la racine.
- Empêche l’import accidentel de modules en dehors d’un environnement virtuel.

📌 **Bonne pratique** : nommer le package `my_package` en **snake_case**.

---

### 2️⃣ **Tests (`tests/`)**
- Contient les **tests unitaires et d’intégration**.
- Utilise des **noms clairs** (`test_xxx.py`).
- Utilisation de **pytest** (`pytest tests/` pour exécuter les tests).

📌 **Bonne pratique** : chaque fichier de test correspond à un module du package.

---

### 3️⃣ **Dépendances (`requirements.txt` ou `pyproject.toml`)**
- **`requirements.txt`** : liste des packages installés (`pip install -r requirements.txt`).
- **`pyproject.toml`** : recommandé pour les nouveaux projets (via **Poetry**).

📌 **Bonne pratique** :
```sh
pip freeze > requirements.txt
```

---

### 4️⃣ **Fichiers de configuration (`setup.py`, `pyproject.toml`)**
- `setup.py` : configuration standard pour créer un package installable.
- `pyproject.toml` : nouvelle alternative avec **Poetry**.

📌 **Bonne pratique** : si ton projet est un package, utilise `pyproject.toml`.

---

### 5️⃣ **README.md**
Doit inclure :
- 📌 **Nom du projet**
- 🎯 **Description**
- 🛠️ **Installation et utilisation**
- 📝 **Exemples de code**
- 🏗️ **Contributions et licences**

📌 **Bonne pratique** : bien formaté en **Markdown**.

---

### 6️⃣ **.gitignore**
Empêche de versionner :
```txt
__pycache__/
*.pyc
.env
venv/
.idea/
.vscode/
```
📌 **Bonne pratique** : utilise [ce modèle de `.gitignore` pour Python](https://github.com/github/gitignore/blob/main/Python.gitignore).

---

## 🚀 **Bonus : outils pour respecter les standards**
Pour assurer une bonne qualité de code :
1. **PEP 8 (Style guide)** :  
   ```sh
   pip install flake8
   flake8 src/
   ```
2. **Formatage automatique (Black)** :  
   ```sh
   pip install black
   black src/
   ```
3. **Vérification des imports (isort)** :  
   ```sh
   pip install isort
   isort src/
   ```
4. **Pre-commit hooks** (empêche de commit du code mal formatté) :  
   ```sh
   pip install pre-commit
   pre-commit install
   ```

---

## 🏆 **Conclusion**
### 🎯 À respecter pour une structure **professionnelle** :
✅ **Code source** dans un dossier `src/`  
✅ **Tests séparés** dans `tests/`  
✅ **Dépendances gérées** via `requirements.txt` ou `pyproject.toml`  
✅ **Documentation claire** (`README.md`)  
✅ **CI/CD** via `.github/` (optionnel)  
✅ **Linting & formatage** (`flake8`, `black`, `isort`)  
