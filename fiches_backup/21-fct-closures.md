Voici quelques **exemples concrets et avancés** qui exploitent **les fonctions internes en Python**, en mettant l'accent sur l'**encapsulation**, 
la **construction dynamique de fonctions** et la différence entre **fonctions internes** et **méthodes privées**.

---

## **1. Encapsulation : cacher une logique interne**
L’encapsulation permet d’empêcher l’accès direct à certaines parties du code. Les fonctions internes sont une bonne alternative aux méthodes privées (`_nom` ou `__nom` en Python).

### **Exemple : Gestion d’une base de données (sans exposer la logique interne)**
```python
def gestion_bd():
    _db = []  # Liste privée

    def ajouter_donnee(donnee):
        """Ajoute une donnée à la base."""
        _db.append(donnee)
        print(f"Donnée ajoutée : {donnee}")

    def afficher_donnees():
        """Affiche toutes les données stockées."""
        print("Données stockées :", _db)

    def supprimer_donnee(donnee):
        """Supprime une donnée si elle existe."""
        if donnee in _db:
            _db.remove(donnee)
            print(f"Donnée supprimée : {donnee}")
        else:
            print(f"Donnée non trouvée : {donnee}")

    return ajouter_donnee, afficher_donnees, supprimer_donnee

ajouter, afficher, supprimer = gestion_bd()

ajouter("Alice")
ajouter("Bob")
afficher()
supprimer("Alice")
afficher()
```
### **Pourquoi c'est utile ?**
- `_db` **n'est accessible que depuis les fonctions internes**.
- On ne peut **pas la modifier directement** depuis l'extérieur, évitant ainsi des incohérences.

---

## **2. Construction dynamique de fonctions (Closures avancées)**
Parfois, on a besoin de **générer dynamiquement des fonctions avec des paramètres capturés**.

### **Exemple : Génération d'une API pour une calculatrice**
```python
def create_calculator(operateur):
    """Crée dynamiquement une fonction de calcul en fonction de l'opérateur."""
    
    def addition(x, y):
        return x + y

    def soustraction(x, y):
        return x - y

    def multiplication(x, y):
        return x * y

    def division(x, y):
        return x / y if y != 0 else "Erreur : division par zéro"

    operations = {
        "+": addition,
        "-": soustraction,
        "*": multiplication,
        "/": division
    }

    return operations.get(operateur, lambda x, y: "Opérateur invalide")

calcul_plus = create_calculator("+")
calcul_moins = create_calculator("-")
calcul_div = create_calculator("/")

print(calcul_plus(10, 5))  # 15
print(calcul_moins(10, 5))  # 5
print(calcul_div(10, 0))  # Erreur : division par zéro
```
### **Pourquoi c'est utile ?**
- On génère des **fonctions spécifiques sans conditionnelles répétitives**.
- On **évite d'exposer la logique de choix d'opération**.

---

## **3. Différence entre Fonction Interne et Méthode Privée (`_private`)**
En Python, on peut utiliser des **fonctions internes** pour limiter l'accès à certaines fonctionnalités. Cependant, en programmation orientée objet (POO), on utilise aussi **les méthodes privées (`_nom`)**.

### **Exemple avec des méthodes privées :**
```python
class Utilisateur:
    def __init__(self, nom):
        self.nom = nom
        self._mot_de_passe = "1234"  # Convention pour dire que c'est privé

    def afficher_nom(self):
        return f"Utilisateur : {self.nom}"

    def _afficher_mot_de_passe(self):  # Méthode privée (convention)
        return f"Mot de passe : {self._mot_de_passe}"

u = Utilisateur("Alice")
print(u.afficher_nom())  # OK
print(u._mot_de_passe)  # Pas une vraie protection, juste une convention
```
**Problème ?** En Python, `_mot_de_passe` **reste accessible** malgré son underscore.

### **Alternative avec une fonction interne (meilleure encapsulation)**
```python
def creer_utilisateur(nom):
    mot_de_passe = "1234"  # Complètement inaccessible de l'extérieur

    def afficher_nom():
        return f"Utilisateur : {nom}"

    def verifier_mot_de_passe(mdp):
        return mdp == mot_de_passe

    return afficher_nom, verifier_mot_de_passe

afficher, verifier = creer_utilisateur("Alice")

print(afficher())  # OK
print(verifier("1234"))  # True
print(verifier("wrong"))  # False
# print(mot_de_passe)  # Erreur : non accessible
```
### **Pourquoi c'est mieux ?**
- **Le mot de passe n'est pas accessible en dehors de `creer_utilisateur()`**.
- Impossible de le modifier ou de le lire par erreur.

---

## **4. Fonction Interne dans une Classe : Protection avancée**
On peut combiner **POO et fonction interne** pour restreindre certaines actions.

### **Exemple : Banque avec transactions protégées**
```python
class CompteBancaire:
    def __init__(self, solde_initial):
        self.solde = solde_initial

    def _historique(self):  # Méthode privée (accessible dans la classe)
        historique_transactions = []

        def ajouter_transaction(montant):
            historique_transactions.append(montant)

        def afficher_historique():
            return historique_transactions

        return ajouter_transaction, afficher_historique

    def deposer(self, montant):
        if montant > 0:
            self.solde += montant
            self._historique()[0](montant)  # On ajoute à l'historique
            print(f"Dépôt : {montant}€ | Nouveau solde : {self.solde}€")

    def retirer(self, montant):
        if 0 < montant <= self.solde:
            self.solde -= montant
            self._historique()[0](-montant)
            print(f"Retrait : {montant}€ | Nouveau solde : {self.solde}€")
        else:
            print("Fonds insuffisants.")

    def afficher_historique(self):
        return self._historique()[1]()  # On récupère l'historique

compte = CompteBancaire(500)
compte.deposer(200)
compte.retirer(100)
print(compte.afficher_historique())  # [200, -100]
```
### **Pourquoi utiliser une fonction interne ici ?**
- **L’historique des transactions est complètement caché**.
- Il n’est **modifiable qu’à travers `deposer()` et `retirer()`**.

---

## **Conclusion**
| Méthode | Quand l'utiliser ? | Avantages |
|---------|-------------------|-----------|
| **Fonction interne** | Protéger des données ou une logique interne | Impossible d'accéder/modifier depuis l'extérieur |
| **Méthode privée (`_nom`)** | Quand on veut une convention sans vraie restriction | Peut être accédée/modifiée, mais indique une intention privée |
| **Closure (fonction qui retourne une autre fonction)** | Générer dynamiquement des comportements | Capture des variables et évite des structures complexes |
