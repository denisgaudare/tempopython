# ✅ Outils Python, 
## pour la documentation, la génération de l'aide,
## et interaction avec objets ou modules Python

## Usages courants des outils Python, 
## y compris pydoc

### 1. **pydoc** – Documentation Python

**pydoc** est un module qui génère de la documentation pour les modules Python, les classes, les fonctions, et plus encore. Il permet aux développeurs de comprendre rapidement le code Python sans avoir à parcourir les fichiers source.
https://docs.python.org/3/library/pydoc.html

#### Utilisation courante de `pydoc` :
- **Affichage de la documentation d'un module :**
  ```bash
  pydoc nom_du_module
  ```
  Cela affiche la documentation du module dans le terminal. Par exemple :
  ```bash
  pydoc math
  ```
  Cela vous donne la documentation pour le module **math** de Python.

- **Affichage de la documentation pour une fonction ou une classe :**
  ```bash
  pydoc nom_du_module.nom_de_la_fonction
  ```
  Exemple :
  ```bash
  pydoc math.sqrt
  ```
  Cela vous donnera la documentation pour la fonction `sqrt` du module **math**.

- **Lancement d'un serveur web pour la documentation locale :**
  ```bash
  pydoc -p 1234
  ```
  Cela démarre un serveur web local sur le port **1234**, et vous pouvez consulter la documentation via un navigateur à l'adresse `http://localhost:1234`.

### 2. **help()** – Aide interactive

`help()` est une fonction intégrée qui peut être utilisée dans une session Python interactive pour obtenir de l'aide sur des objets, des modules, des classes, ou des fonctions.

#### Exemple d'utilisation :
- **Afficher de l'aide pour une fonction ou une classe :**
  ```python
  help(math.sqrt)
  ```
  Cela affiche la documentation pour la fonction `sqrt` du module **math** dans l'interpréteur Python.

- **Afficher de l'aide générale :**
  ```python
  help()
  ```
  Cela ouvre un environnement interactif où vous pouvez taper des commandes pour obtenir de l'aide sur des objets ou des modules.

### 3. **dir()** – Afficher les attributs d'un objet

La fonction `dir()` est utilisée pour lister les attributs et méthodes d'un objet, d'un module ou d'une classe.

#### Exemple :
```python
dir(math)
```
Cela affiche toutes les fonctions et attributs disponibles dans le module **math**.

### 4. **inspect** – Inspection des objets Python

Le module **inspect** permet d'examiner les objets Python en détail, comme obtenir des informations sur les fonctions, les classes, ou les modules.

#### Exemple :
- **Lister les fonctions d’un module :**
```python
import inspect
import math
print(inspect.getmembers(math, inspect.isfunction))
```

Cela listera toutes les fonctions disponibles dans le module **math**.

### 5. **doctest** – Tester la documentation

**doctest** est un module qui permet d'exécuter des tests unitaires directement dans la documentation. Vous pouvez insérer des exemples d'utilisation dans vos docstrings, et **doctest** vérifiera que ces exemples fonctionnent comme prévu.

#### Exemple :
Dans le fichier Python :
```python
def add(a, b):
    """
    Add two numbers together.

    >>> add(2, 3)
    5
    >>> add(10, 20)
    30
    """
    return a + b
```
Ensuite, vous pouvez tester les docstrings avec :
```
python
import doctest
doctest.testmod()
```

Cela vérifiera si les exemples dans la docstring fonctionnent correctement.

### 6. **timeit** – Mesurer les performances du code

Le module **timeit** permet de mesurer le temps d'exécution des petites portions de code.

#### Exemple :
```python
import timeit
print(timeit.timeit('math.sqrt(16)', setup='import math', number=1000000))
```
Cela mesure le temps nécessaire pour exécuter l'expression `math.sqrt(16)` un million de fois.

### 7. **argparse** – Gestion des arguments en ligne de commande

Le module **argparse** est utilisé pour créer des interfaces de ligne de commande où vous pouvez définir des options et arguments.

#### Exemple :
```python
import argparse

parser = argparse.ArgumentParser(description="Exemple de programme")
parser.add_argument('name', type=str, help="Votre nom")
args = parser.parse_args()
print(f"Bonjour, {args.name}!")
```
Cela permet d'interagir avec le programme via la ligne de commande pour recevoir des arguments.


