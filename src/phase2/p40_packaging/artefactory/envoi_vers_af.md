# Artefactory 
## 📦 1. Prérequis

Avant tout :

- ✅ **Artifactory** configuré pour héberger des packages **Python** (type `pypi` repo).
- ✅ **compte utilisateur** ou un **token API**.
- ✅ **URL du dépôt Python Artifactory**, ex :
  ```
  https://your-company.jfrog.io/artifactory/api/pypi/python-local/
  ```

---

## 🛠️ 2. Avec `setuptools` (et `twine`)

### 🔧 `setup.py` ou `pyproject.toml`
Pas besoin de changement spécifique, sauf que le `version` doit être bien défini.

### 📦 Construction du package
```bash
python -m build  # ou pip install build && python -m build
```
Cela génère :
```
dist/
  hello_pkg-0.1.0.tar.gz
  hello_pkg-0.1.0-py3-none-any.whl
```

### 🚀 Déploiement avec `twine`

Crée un fichier `~/.pypirc` :

```ini
[distutils]
index-servers =
    artifactory

[artifactory]
repository = https://your-company.jfrog.io/artifactory/api/pypi/python-local/
username = <TON_UTILISATEUR>
password = <TON_MOT_DE_PASSE_OU_TOKEN>
```

Puis pousse le package :

```bash
twine upload -r artifactory dist/*
```

---

## 🛠️ 3. Avec `poetry`

### Configuration du dépôt distant dans `pyproject.toml` :

Tu peux déclarer le dépôt :

```toml
[[tool.poetry.source]]
name = "artifactory"
url = "https://your-company.jfrog.io/artifactory/api/pypi/python-local/"
default = false
```

Ou ajouter avec la commande :

```bash
poetry source add artifactory https://your-company.jfrog.io/artifactory/api/pypi/python-local/
```

### Authentification :

```bash
poetry config http-basic.artifactory <username> <password-ou-token>
```

### Build et déploiement :

```bash
poetry build
poetry publish --repository artifactory
```

---

## 🔐 Alternatives sécurisées

- Utilise un **token API** à la place du mot de passe.
- Stocke tes credentials dans des variables d’environnement.
- Certains Artifactory peuvent aussi utiliser `pip` avec un `.netrc` ou directement des URLs de type :

```bash
pip install --index-url https://<username>:<token>@your-company.jfrog.io/artifactory/api/pypi/python-local/simple hello_pkg
```
