En Python, une **fonction interne** (ou **fonction imbriquée**) est une fonction définie à l'intérieur d'une autre fonction. Elles sont utiles pour organiser le code, encapsuler une logique spécifique et limiter la portée d'une fonction aux besoins de la fonction englobante.

### 1. **Définition d'une fonction interne**
Une fonction interne est définie comme une fonction normale mais **à l'intérieur d'une autre fonction** :

```python
def externe():
    print("Je suis la fonction externe.")

    def interne():
        print("Je suis la fonction interne.")

    interne()  # Appel de la fonction interne

externe()
```
**Sortie :**
```
Je suis la fonction externe.
Je suis la fonction interne.
```
La fonction `interne()` **n’est accessible que dans `externe()`**.

---

### 2. **Utilisation des fonctions internes**
Les fonctions internes sont souvent utilisées pour :
- **Encapsulation de logique**
- **Limiter la portée d’une fonction** (éviter qu’elle soit accessible ailleurs)
- **Utiliser des fermetures (closures)**

#### **Exemple 1 : Fonction interne avec des variables de la fonction externe**
```python
def message_utilisateur(nom):
    def construire_message():
        return f"Bonjour, {nom} !"
    
    return construire_message()  # Appel de la fonction interne

print(message_utilisateur("Alice"))
```
**Sortie :**  
```
Bonjour, Alice !
```
Ici, `construire_message()` accède à la variable `nom` définie dans `message_utilisateur()`.

---

### 3. **Utilisation des fermetures (Closures)**
Une **closure** est une fonction interne qui capture les variables de la fonction englobante même après que celle-ci ait terminé son exécution.

#### **Exemple 2 : Retourner une fonction (Closure)**
```python
def create_multiplier(facteur):
    def multiplier(nombre):
        return nombre * facteur  # Utilise `facteur` défini dans `create_multiplier`
    return multiplier  # Retourne la fonction interne

double = create_multiplier(2)
triple = create_multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15
```
Ici, `multiplier()` garde en mémoire la valeur de `facteur` même après que `create_multiplier()` ait terminé son exécution.

---

### 4. **Utilisation avec `nonlocal` pour modifier une variable externe**
Si la fonction interne doit modifier une variable de la fonction englobante, il faut utiliser `nonlocal`.

#### **Exemple 3 : Modifier une variable avec `nonlocal`**
```python
def compteur():
    nombre = 0  # Variable locale

    def incrementer():
        nonlocal nombre  # Permet de modifier la variable externe
        nombre += 1
        return nombre
    
    return incrementer

compte = compteur()
print(compte())  # 1
print(compte())  # 2
print(compte())  # 3
```
Sans `nonlocal`, `nombre` serait une nouvelle variable à chaque appel de `incrementer()`.

---

### 5. **Utilisation en tant que décorateur**
Les fonctions internes sont souvent utilisées pour **créer des décorateurs**, qui permettent de modifier dynamiquement le comportement d’une fonction.

#### **Exemple 4 : Décorateur simple**
```python
def decorateur(fonction):
    def wrapper():
        print("Avant l'exécution")
        fonction()
        print("Après l'exécution")
    return wrapper

@decorateur
def dire_bonjour():
    print("Bonjour !")

dire_bonjour()
```
**Sortie :**
```
Avant l'exécution
Bonjour !
Après l'exécution
```
Ici, `wrapper()` est une fonction interne qui ajoute du code avant et après l’exécution de `fonction()`.

---

### **Résumé**
✔ Une fonction interne est définie **dans une autre fonction**  
✔ Elle est utile pour **encapsuler** une logique et **réduire la portée**  
✔ Une **closure** permet de capturer des variables de la fonction englobante  
✔ `nonlocal` permet de **modifier une variable externe**  
✔ On les utilise fréquemment pour **les décorateurs**
