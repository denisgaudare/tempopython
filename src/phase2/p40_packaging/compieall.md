Aperçu des principaux arguments que vous pouvez passer à **python.exe** (ou à l'exécutable Python) sur différents systèmes d'exploitation. Vous pouvez utiliser la commande suivante dans un terminal pour obtenir la liste complète des arguments disponibles :

```bash
python --help
```

### Principaux arguments de **python.exe** (ou `python`)

1. **`-c`**  
   Permet d'exécuter une commande Python passée en ligne de commande.

   ```bash
   python -c "print('Hello, World!')"
   ```

2. **`-m`**  
   Permet d'exécuter un module en tant que script. C'est particulièrement utile pour exécuter des modules comme des scripts (par exemple, `http.server`, `unittest`, etc.).

   ```bash
   python -m http.server 8000  # Lancer un serveur HTTP simple
   python -m unittest tests.py  # Lancer des tests unitaires
   ```

3. **`-i`**  
   Lancer une session interactive après l'exécution d'un script Python. Cela vous permet d'entrer dans l'interpréteur interactif après l'exécution d'un fichier Python.

   ```bash
   python -i script.py
   ```

4. **`-B`**  
   Empêche la création de fichiers `.pyc` dans les répertoires `__pycache__`.

   ```bash
   python -B script.py
   ```

5. **`-O`**  
   Active l'optimisation du bytecode Python (génère des fichiers `.pyo` au lieu de `.pyc`).

   ```bash
   python -O script.py
   ```

6. **`-OO`**  
   Active une optimisation supplémentaire, qui supprime les docstrings dans les fichiers compilés. Cela peut réduire la taille des fichiers `.pyo`.

   ```bash
   python -OO script.py
   ```

7. **`-m`**  
   Permet d'exécuter un module Python comme script. Vous devez spécifier le nom du module.

   ```bash
   python -m module_name
   ```

8. **`-v`**  
   Affiche des informations détaillées sur les modules importés (mode verbeux). Vous pouvez également utiliser `-vv` pour encore plus de détails.

   ```bash
   python -v script.py
   ```

9. **`-X`**  
   Permet de définir certaines options spécifiques à CPython. Par exemple :
   
   - **`-X dev`** : Active le mode de développement (affiche plus de messages d'avertissement, active certaines vérifications internes).
   - **`-X tracemalloc`** : Active la traçabilité de la mémoire.
   
   Exemple pour activer le mode développement :
   ```bash
   python -X dev script.py
   ```

10. **`-h` ou `--help`**  
    Affiche l'aide et la liste des options disponibles pour l'interpréteur Python.

    ```bash
    python --help
    ```

11. **`-u`**  
    Force Python à fonctionner en mode unbuffered. Cela désactive les tampons de sortie (utile pour l'affichage immédiat de sorties, comme dans les logs en temps réel).

    ```bash
    python -u script.py
    ```

12. **`-d`**  
    Active le mode de débogage. Cela affiche des messages de débogage internes.

    ```bash
    python -d script.py
    ```

13. **`-E`**  
    Désactive l'influence des variables d'environnement Python (comme `PYTHONPATH`).

    ```bash
    python -E script.py
    ```

14. **`--version`**  
    Affiche la version de l'interpréteur Python en cours d'exécution.

    ```bash
    python --version
    ```

15. **`-P`**  
    Spécifie un chemin d'installation de Python personnalisé. Vous pouvez l'utiliser pour utiliser une version différente de Python ou un environnement virtuel spécifique.

    ```bash
    python -P /chemin/vers/python
    ```

### Exemple pratique : Passer plusieurs arguments à `python.exe`

Supposons que vous souhaitez exécuter un script Python avec des options spécifiques et lancer une session interactive après l'exécution. Vous pouvez combiner plusieurs arguments comme ceci :

```bash
python -i -v script.py
```

Cela exécutera `script.py` en mode verbeux, puis entrera dans une session interactive après l'exécution du script.

### Pour résumer :
Voici quelques-unes des options les plus courantes de l'interpréteur Python :
- **`-c`** : Exécute un script Python en ligne de commande.
- **`-m`** : Exécute un module comme script.
- **`-i`** : Lance une session interactive après l'exécution d'un script.
- **`-O` / `-OO`** : Active les optimisations de bytecode.
- **`-B`** : Empêche la création des fichiers `.pyc`.
- **`--help`** : Affiche l'aide détaillée sur les options de l'interpréteur.

Pour obtenir la liste complète des options et de leur description, vous pouvez toujours exécuter la commande `python --help` ou consulter la documentation officielle de Python.

---
# .py VS .pyc

Voici les étapes et méthodes pour livrer uniquement les fichiers **`.pyc`** dans un projet Python :

### 1. **Générer les fichiers `.pyc`**
Avant de livrer les fichiers `.pyc`, vous devez d'abord les générer à partir des fichiers `.py` sources.

#### a. Utiliser la commande `compileall`
La commande `compileall` de Python permet de compiler tous les fichiers `.py` d'un répertoire (et de ses sous-répertoires) en fichiers `.pyc`. Cela place les fichiers `.pyc` dans un répertoire `__pycache__`.

Exécutez cette commande pour compiler un répertoire entier :
```bash
python -m compileall /chemin/vers/dossier
```

Cela crée des fichiers `.pyc` dans un répertoire `__pycache__` de chaque répertoire contenant des fichiers `.py`.

#### b. Utiliser `py_compile`
Si vous ne voulez compiler qu'un fichier spécifique, vous pouvez utiliser le module `py_compile` :
```bash
python -m py_compile fichier.py
```
Cela crée un fichier `.pyc` dans le répertoire `__pycache__` du répertoire contenant le fichier `.py` d'origine.

### 2. **Vérifier l'emplacement des fichiers `.pyc`**
Les fichiers `.pyc` sont stockés dans un sous-répertoire appelé **`__pycache__`**. Le nom du fichier `.pyc` inclura la version de Python utilisée pour le générer. Par exemple, pour Python 3.9, un fichier `.pyc` généré pour `script.py` sera nommé `script.cpython-39.pyc`.

Exemple :
```
mon_projet/
│
├── __pycache__/
│   └── script.cpython-39.pyc
│   └── autre_module.cpython-39.pyc
│
└── README.md
```

### 3. **Livrer uniquement les fichiers `.pyc`**
Une fois que vous avez généré les fichiers `.pyc`, vous pouvez décider de livrer uniquement ceux-ci.

#### a. Supprimer les fichiers `.py` avant la livraison
Une façon simple de livrer uniquement les fichiers `.pyc` est de supprimer tous les fichiers `.py` et ne garder que les fichiers `.pyc`. Vous pouvez faire cela manuellement ou avec un script.

Exemple avec un script Python qui supprime les fichiers `.py` :
```python
import os
import glob

# Répertoire contenant le code
project_dir = '/chemin/vers/dossier'

# Supprimer les fichiers .py
for file in glob.glob(os.path.join(project_dir, '**', '*.py'), recursive=True):
    os.remove(file)

print("Fichiers .py supprimés, seuls les .pyc restent.")
```

Cela supprimera les fichiers `.py` et laissera uniquement les fichiers `.pyc` dans le répertoire `__pycache__`.

#### b. Livrer le répertoire `__pycache__`
Une autre méthode consiste à livrer directement le répertoire **`__pycache__`** contenant les fichiers `.pyc`. Vous pouvez alors ignorer les fichiers `.py` dans le package que vous livrez.

Cela peut se faire dans un fichier compressé (tar, zip, etc.) ou tout simplement en transférant le répertoire `__pycache__`.

Par exemple, vous pouvez préparer une archive contenant uniquement le répertoire `__pycache__` :
```bash
tar czf mon_projet.tar.gz __pycache__
```

### 4. **Disons qu'il y a une exception à faire avec des fichiers `.pyc`**
L'inconvénient de ne livrer que des fichiers `.pyc` est que le bytecode peut être spécifique à une version de Python. Cela signifie que si le client utilise une version différente de Python, les fichiers `.pyc` risquent de ne pas être compatibles.

#### Solution :
- Vous pouvez soit compiler les fichiers `.py` pour plusieurs versions de Python et livrer les fichiers `.pyc` pour chaque version.
- Vous pouvez également fournir un fichier d'instructions expliquant comment le client peut compiler les fichiers `.py` par lui-même, en utilisant la commande `python -m compileall`.

### 5. **Exclure les fichiers `.py` de la distribution (via `.gitignore`, `.dockerignore`, etc.)**
Si vous utilisez un système de contrôle de version comme Git, ou si vous déployez dans un conteneur Docker, vous pouvez facilement ignorer les fichiers `.py` et ne livrer que les fichiers `.pyc` en modifiant les fichiers d'ignore.

- **Avec `.gitignore`** :
  Dans le fichier `.gitignore`, vous pouvez ajouter la ligne suivante pour ignorer tous les fichiers `.py` tout en gardant les `.pyc` :
  ```text
  *.py
  !__pycache__/
  ```

- **Avec `.dockerignore`** :
  Si vous travaillez avec Docker, vous pouvez également spécifier dans le fichier `.dockerignore` :
  ```text
  *.py
  !__pycache__/
  ```

Cela permet de livrer uniquement les fichiers `.pyc` tout en excluant les fichiers `.py`.

### Conclusion

Si vous souhaitez livrer uniquement les fichiers `.pyc` et non les fichiers source `.py`, voici les étapes principales :

1. Compilez vos fichiers `.py` en `.pyc` (avec `compileall`, `py_compile`, ou manuellement).
2. Supprimez les fichiers `.py` ou ignorez-les dans votre méthode de distribution.
3. Livrez uniquement les fichiers `.pyc` (par exemple, dans un répertoire `__pycache__` ou une archive).
4. (Optionnel) Fournissez des instructions pour la compilation ou compilez les fichiers `.pyc` pour plusieurs versions de Python, si nécessaire.

Cela peut être utile pour protéger votre code source ou pour rendre la distribution plus rapide et plus sûre, bien que la portabilité des fichiers `.pyc` entre différentes versions de Python puisse poser des problèmes.