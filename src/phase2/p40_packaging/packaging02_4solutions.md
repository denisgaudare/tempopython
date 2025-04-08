
**Structure des dépôts :**

```
python-packaging-examples/
├── setuptools_setup_py/
│   ├── mypkg/
│   │   ├── __init__.py
│   │   └── cli.py
│   ├── tests/
│   │   └── test_cli.py
│   ├── setup.py
│   ├── README.md
│   └── LICENSE
├── setuptools_setup_cfg/
│   ├── mypkg/
│   │   ├── __init__.py
│   │   └── cli.py
│   ├── tests/
│   │   └── test_cli.py
│   ├── setup.cfg
│   ├── setup.py
│   ├── README.md
│   └── LICENSE
├── pyproject_toml/
│   ├── mypkg/
│   │   ├── __init__.py
│   │   └── cli.py
│   ├── tests/
│   │   └── test_cli.py
│   ├── pyproject.toml
│   ├── README.md
│   └── LICENSE
├── poetry_example/
│   ├── mypkg/
│   │   ├── __init__.py
│   │   └── cli.py
│   ├── tests/
│   │   └── test_cli.py
│   ├── pyproject.toml
│   ├── poetry.lock
│   ├── README.md
│   └── LICENSE
├── flit_example/
│   ├── mypkg/
│   │   ├── __init__.py
│   │   └── cli.py
│   ├── tests/
│   │   └── test_cli.py
│   ├── pyproject.toml
│   ├── README.md
│   └── LICENSE
└── hatch_example/
    ├── mypkg/
    │   ├── __init__.py
    │   └── cli.py
    ├── tests/
    │   └── test_cli.py
    ├── pyproject.toml
    ├── README.md
    └── LICENSE
```

### Contenu de chaque sous-répertoire

- **`mypkg/`** : Contient le code source du package avec un module simple et un point d'entrée CLI.
- **`tests/`** : Inclut des tests unitaires pour le package.
- **Fichiers de configuration** (`setup.py`, `setup.cfg`, `pyproject.toml`, etc.) : Configurent le packaging selon l'outil utilisé.
- **`README.md`** : Fournit des explications détaillées sur la configuration et l'utilisation de l'outil spécifique.
- **`LICENSE`** : Définit la licence du projet.

**Explorer les exemples :**

   Chaque sous-répertoire contient un projet complet avec des instructions spécifiques dans le fichier `README.md` correspondant. Vous pouvez naviguer dans ces répertoires et suivre les instructions pour comprendre et tester chaque configuration.

### Inclusion de `flit` et `hatch`

Les sous-répertoires `flit_example` et `hatch_example` démontreront l'utilisation de `flit` et `hatch` pour le packaging Python. Chaque exemple inclura :

- **`pyproject.toml`** configuré pour l'outil spécifique.
- Instructions pour installer l'outil, initialiser le projet, ajouter des dépendances, et créer des distributions.
- Comparaison des avantages et des inconvénients de l'outil par rapport aux autres.