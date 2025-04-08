# Les Décorateurs

Les **décorateurs** sont une fonctionnalité puissante qui permet **d’ajouter dynamiquement du comportement aux fonctions et aux classes**, sans modifier leur code source.  
Ils reposent sur **les closures (fonctions internes)** et rendent le code **plus lisible, modulaire et maintenable**.

---

## **🔹 1. Avantages des décorateurs**
| **Avantages** | **Explication** |
|--------------|----------------|
| **Factorisation du code** 🛠️ | Évite la duplication en **réutilisant des comportements communs** (ex: logging, sécurité, validation). |
| **Lisibilité améliorée** 👀 | Permet de **séparer la logique métier** des aspects techniques (ex: gestion des erreurs). |
| **Modularité et extensibilité** 🚀 | Ajoute **de nouvelles fonctionnalités sans modifier la fonction originale**. |
| **Utilisation intuitive** 🎯 | Grâce au **`@decorator`**, le code reste **simple et naturel**. |

---

## **🔹 2. Comment créer un décorateur ?**
Les **décorateurs** utilisent des **fonctions internes (closures)** pour encapsuler un comportement **autour** d’une fonction.

---

### **2.1 Création d'un décorateur de base**
Un **décorateur** est une **fonction qui prend une fonction en argument et retourne une nouvelle fonction**.

```python
def uppercase_decorator(func):
    """Décorateur qui met en majuscules le retour d'une fonction."""
    def wrapper():
        result = func()
        return result.upper()
    return wrapper  # Retourne la fonction interne

@uppercase_decorator
def greet():
    return "hello world"

print(greet())  # HELLO WORLD
```
✅ **Pourquoi utiliser une closure ?**  
- La fonction `wrapper` **garde en mémoire** la fonction originale `func`.  
- On peut **modifier son comportement** **sans la réécrire**.  

---

### **2.2 Décorateur avec arguments**
Un décorateur peut gérer **des arguments de fonction** en utilisant `*args` et `**kwargs`.

```python
def repeat_decorator(times: int):
    """Décorateur qui exécute une fonction plusieurs fois."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator  # Retourne le décorateur configuré

@repeat_decorator(3)
def say_hello():
    print("👋 Hello!")

say_hello()
# 👋 Hello!
# 👋 Hello!
# 👋 Hello!
```
✅ **Pourquoi utiliser une fonction interne ?**  
- **`decorator(func)` est une closure** qui capture `times`.  
- Permet **de personnaliser le décorateur** lors de son application (`@repeat_decorator(3)`).  

---

## **🔹 3. Utilisation avancée des décorateurs**
### **3.1 Décorateur pour le logging**
📌 **Ajoute automatiquement un log chaque fois qu’une fonction est appelée.**

```python
import time

def log_execution(func):
    """Décorateur qui log l'exécution d'une fonction."""
    def wrapper(*args, **kwargs):
        print(f"📜 Exécution de `{func.__name__}` avec {args}, {kwargs}")
        start_time = time.time()
        result = func(*args, **kwargs)
        print(f"✅ Terminé en {time.time() - start_time:.4f}s")
        return result
    return wrapper

@log_execution
def process_data(data: list):
    time.sleep(1)  # Simule un calcul long
    return [x * 2 for x in data]

print(process_data([1, 2, 3]))
```
✅ **Utilisation automatique du logging** sans modifier `process_data()`.  
✅ **Factorisation du code** pour plusieurs fonctions.  

---

### **3.2 Décorateur pour limiter l'accès (Ex: Authentification)**
📌 **Empêche l’exécution d’une fonction si l’utilisateur n’est pas autorisé.**

```python
def require_auth(func):
    """Décorateur qui vérifie si l'utilisateur est connecté."""
    def wrapper(user):
        if not user.get("authenticated", False):
            print("⛔ Accès refusé !")
            return
        return func(user)
    return wrapper

@require_auth
def show_dashboard(user):
    print(f"📊 Tableau de bord de {user['name']}")

user1 = {"name": "Alice", "authenticated": True}
user2 = {"name": "Bob", "authenticated": False}

show_dashboard(user1)  # ✅ Affiche le dashboard
show_dashboard(user2)  # ⛔ Accès refusé !
```
✅ **Sépare la logique métier (dashboard) de la gestion de la sécurité**.  

---

### **3.3 Décorateur `@property` pour créer des getters intelligents**
📌 **Transforme une méthode en attribut dynamique.**

```python
class Aircraft:
    def __init__(self, fuel: float):
        self._fuel = fuel  # Convention: attribut privé

    @property
    def fuel_status(self) -> str:
        """Retourne un statut lisible du carburant."""
        return "🔴 Bas" if self._fuel < 50 else "🟢 OK"

plane = Aircraft(30)
print(plane.fuel_status)  # 🔴 Bas
# plane.fuel_status = 100  # ❌ Erreur, car readonly
```
✅ **Évite d'écrire `plane.fuel_status()`**, améliore la lisibilité.  
✅ **Encapsulation propre** en empêchant la modification directe (`_fuel` reste privé).  

---

## **🔹 4. Décorateurs et classes (`@classmethod`, `@staticmethod`)**
Les décorateurs **natifs de Python** sont souvent utilisés dans les **classes**.

---

### **4.1 `@staticmethod` → Méthodes sans `self`**
📌 **Méthode liée à la classe mais n'accédant pas aux attributs de l’instance.**

```python
class Airport:
    @staticmethod
    def general_info():
        return "Tous les aéroports suivent les règles de l'OACI."

print(Airport.general_info())  # ✅ Fonctionne sans créer d'objet
```
✅ **Évite d’instancier une classe si ce n’est pas nécessaire.**  

---

### **4.2 `@classmethod` → Accéder à la classe directement**
📌 **Permet de modifier un attribut de classe au lieu de l'instance.**

```python
class Aircraft:
    fleet_size = 0  # Attribut de classe

    def __init__(self, name: str):
        self.name = name
        Aircraft.increment_fleet()

    @classmethod
    def increment_fleet(cls):
        cls.fleet_size += 1

plane1 = Aircraft("Boeing 737")
plane2 = Aircraft("Airbus A320")
print(Aircraft.fleet_size)  # 2
```
✅ **Permet d’agir sur tous les objets (`fleet_size`) sans les instancier.**  

---

## **🔹 5. Décorateurs emboîtés et chaînage**
📌 **Plusieurs décorateurs peuvent être appliqués à une fonction.**

```python
@log_execution
@uppercase_decorator
def greet():
    return "hello, python!"

print(greet())  
# 📜 Exécution de `wrapper`...
# HELLO, PYTHON!
# ✅ Terminé en 0.0001s
```
✅ **Les décorateurs sont appliqués de bas en haut (`uppercase_decorator` puis `log_execution`).**  

---

## **🔥 Conclusion**
| **Pourquoi utiliser les décorateurs ?** ✅ |
|---------------------------------------------|
| **Réduit la duplication du code** 📉 |
| **Rend le code plus lisible et modulaire** 🎯 |
| **Sépare les préoccupations (Logging, Auth, Timing...)** 🚀 |
| **Exploite la puissance des fonctions internes et closures** 🔥 |