### **📌 Définir une classe dynamiquement en Python**

Python permet de **créer des classes dynamiquement** à l'exécution, notamment avec la fonction intégrée `type()`. Cette approche est utile pour la **métaprogrammation**, la **génération de classes dynamiques**, ou encore l'**optimisation de code**.

---

## **1️⃣ Exemple de base : Création d'une classe avec `type()`**
La fonction `type()` peut être utilisée de deux manières :

- **Cas classique** : `type(objet)`
- **Cas avancé** : `type(nom, bases, attributs)`

Voici comment créer une classe **dynamiquement** :

```python
# Création d'une classe "Personne" avec type()
Personne = type("Personne", (object,), {"nom": "Alice", "age": 30})

# Instanciation
p = Personne()
print(p.nom, p.age)  # Alice 30
```
📌 `type("NomClasse", (Base,), {dictionnaire d'attributs})` crée une classe sur le moment.

---

## **2️⃣ Ajout de méthodes dynamiquement**
On peut ajouter des **méthodes** dynamiquement :

```python
def se_presenter(self):
    return f"Je m'appelle {self.nom} et j'ai {self.age} ans."

# Création dynamique de la classe
Personne = type("Personne", (object,), {"nom": "Alice", "age": 30, "se_presenter": se_presenter})

p = Personne()
print(p.se_presenter())  # Je m'appelle Alice et j'ai 30 ans.
```
📌 On passe **une fonction** comme méthode de la classe.

---

## **3️⃣ Création avancée avec `__init__`**
On peut ajouter un constructeur `__init__` dynamiquement :

```python
def init(self, nom, age):
    self.nom = nom
    self.age = age

Personne = type("Personne", (object,), {"__init__": init, "se_presenter": se_presenter})

p = Personne("Bob", 25)
print(p.se_presenter())  # Je m'appelle Bob et j'ai 25 ans.
```
📌 Ici, `__init__` est défini dynamiquement pour prendre des arguments.

---

## **4️⃣ Héritage dynamique**
On peut aussi créer une classe **dérivée dynamiquement** :

```python
Employe = type("Employe", (Personne,), {"poste": "Développeur"})

e = Employe("Charlie", 40)
print(e.se_presenter())  # Je m'appelle Charlie et j'ai 40 ans.
print(e.poste)  # Développeur
```
📌 `Employe` hérite dynamiquement de `Personne` !

---

## **5️⃣ Création avec `metaclass` (Programmation avancée)**
Une **métaclasse** est une classe qui génère **d'autres classes** :

```python
class MetaPersonne(type):
    def __new__(cls, name, bases, dct):
        dct["presentation"] = lambda self: f"Je suis {self.nom}"
        return super().__new__(cls, name, bases, dct)

class Personne(metaclass=MetaPersonne):
    def __init__(self, nom):
        self.nom = nom

p = Personne("Alice")
print(p.presentation())  # Je suis Alice
```
📌 Ici, **MetaPersonne** modifie la classe **Personne** au moment de sa création.

---

## **🎯 Quand utiliser ces techniques ?**
✅ Générer des classes **en fonction de la configuration** (ex. API, bases de données).  
✅ Modifier le comportement des classes **sans toucher au code source**.  
✅ **Éviter le code répétitif** en créant plusieurs classes similaires automatiquement.  
