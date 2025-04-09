### **📌 Création d'une Classe Dynamique en Python**

---

## **1️⃣ Pourquoi créer une classe dynamiquement ?**
Voici quelques cas d'utilisation :
- **Génération automatique de modèles** (ex: ORM comme SQLAlchemy).
- **Personnalisation des objets à la volée** en fonction de paramètres d'entrée.
- **Éviter le code répétitif** en générant des classes adaptées dynamiquement.
- **Extensions et plugins** où les classes sont définies au moment de l'exécution.

---

## **2️⃣ Création d'une classe dynamique avec `type()`**
La fonction `type()` permet de **créer une classe à la volée**.

### **Exemple simple : Génération d'une classe "Aircraft" dynamique**
```python
# Définition dynamique d'une classe Aircraft
Aircraft = type("Aircraft", (object,), {"model": "Boeing 747", "max_speed": 900})

# Création d'une instance
plane = Aircraft()
print(plane.model)       # Boeing 747
print(plane.max_speed)   # 900
```
### **💡 Explication**
- `type("Aircraft", (object,), {...})` crée une **classe nommée `Aircraft`**.
- `(object,)` indique qu'elle hérite de `object` (comme une classe classique).
- Le dictionnaire `{"model": "Boeing 747", "max_speed": 900}` définit les attributs de classe.

---

## **3️⃣ Ajouter des méthodes dynamiquement**
On peut aussi **ajouter des méthodes** dynamiquement :

```python
# Définition d'une méthode
def fly(self):
    return f"{self.model} vole à {self.max_speed} km/h !"

# Création de la classe avec une méthode dynamique
Aircraft = type("Aircraft", (object,), {"model": "Boeing 747", "max_speed": 900, "fly": fly})

# Création d'une instance
plane = Aircraft()
print(plane.fly())  # Boeing 747 vole à 900 km/h !
```

### **💡 Explication**
- On définit une fonction `fly(self)`.
- On l’ajoute au dictionnaire passé à `type()`.
- La méthode est maintenant disponible dans la classe dynamique.

---

## **4️⃣ Création de classes dynamiques avec une métaclasse**
Pour un contrôle plus avancé, on peut utiliser **les métaclasses**.

### **Exemple : Ajouter automatiquement un préfixe aux attributs**
```python
class MetaAircraft(type):
    def __new__(cls, name, bases, dct):
        new_dct = {f"aircraft_{key}": value for key, value in dct.items()}  # Préfixe des attributs
        return super().__new__(cls, name, bases, new_dct)

# Utilisation de la métaclasse
class Aircraft(metaclass=MetaAircraft):
    model = "Airbus A320"
    max_speed = 850

# Création d'une instance
plane = Aircraft()
print(plane.aircraft_model)      # Airbus A320
print(plane.aircraft_max_speed)  # 850
```

### **💡 Explication**
- `MetaAircraft` modifie la création de la classe en **préfixant les attributs** avec `"aircraft_"`.
- `super().__new__(cls, name, bases, new_dct)` génère la classe modifiée.

---

## **📌 Quand utiliser quelle approche ?**
| **Méthode** | **Quand l'utiliser ?** |
|------------|----------------------|
| `type()` | Lorsque la classe est créée **dynamiquement** en fonction de l'exécution (ex: génération automatique de modèles). |
| Métaclasses | Lorsque **toutes** les classes d’un type doivent avoir des comportements spéciaux (ex: ORM, frameworks). |

