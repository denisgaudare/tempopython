### **🚀 Amélioration du projet de simulation `Aircraft`**

Nous allons **étendre notre projet** en y ajoutant :
1. ✅ **Un décorateur `@type_check`** pour **vérifier automatiquement les types des arguments** des méthodes.
2. ✅ **Un générateur** pour **optimiser la gestion des numéros de vol**.

---

## **🔹 1. Ajout du décorateur `@type_check`**
📌 **Pourquoi ?**  
- **Sécurise les entrées** en s'assurant que les arguments sont bien du bon type.  
- **Évite les erreurs difficiles à détecter** en cas de mauvaise utilisation de la classe.  
- **Alternative légère à `pydantic` pour la validation de types.**  

```python
from functools import wraps
import inspect

def type_check(func):
    """Décorateur qui vérifie que les booster sont du bon type."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        signature = inspect.signature(func)
        parameters = signature.parameters

        bound_arguments = signature.bind(*args, **kwargs)
        bound_arguments.apply_defaults()

        for name, value in bound_arguments.arguments.items():
            expected_type = parameters[name].annotation
            if expected_type is not inspect._empty and not isinstance(value, expected_type):
                raise TypeError(f"❌ Type invalide pour `{name}` : attendu {expected_type}, reçu {type(value)}")

        return func(*args, **kwargs)
    return wrapper
```

✅ **Ce décorateur inspecte les annotations des fonctions et vérifie les types au moment de l'exécution.**  

---

## **🔹 2. Ajout d’un générateur pour les numéros de vol**
📌 **Pourquoi ?**  
- **Évite de stocker une liste en mémoire** et génère les numéros **à la demande**.  
- **Optimise la gestion des ressources** en évitant la répétition.  
- **Utile dans un système en production où les numéros de vol doivent être générés dynamiquement.**  

```python
from itertools import count

def flight_number_generator(prefix: str):
    """Générateur infini de numéros de vol."""
    counter = count(start=100)  # Commence à 100 pour éviter les doublons
    while True:
        yield f"{prefix}{next(counter)}"
```

✅ **Un générateur `flight_number_generator("AF")` créera une séquence infinie : `AF100, AF101, AF102...`**  

---

## **🔹 3. Intégration dans la classe `Aircraft`**
📌 **Améliorations** :
- 🎯 **Vérification des types** avec `@type_check`.  
- ⚡ **Utilisation du générateur** pour attribuer un numéro de vol dynamique.  
- 🔄 **Optimisation des ressources mémoire et CPU**.  

```python
class Aircraft:
    flight_gen = flight_number_generator("AF")  # Générateur partagé entre toutes les instances

    @type_check
    def __init__(self, capacity: int, fuel: float):
        self.flight_name = next(Aircraft.flight_gen)  # Génération dynamique du vol
        self.capacity = capacity
        self.fuel = fuel  # En pourcentage

    @type_check
    def refuel(self, amount: float):
        """Ajoute du carburant jusqu'à un maximum de 100%."""
        self.fuel = min(self.fuel + amount, 100)
        print(f"⛽ {self.flight_name} ravitaillé ({self.fuel}%)")

    @type_check
    def fly(self, distance: float):
        """Simule un vol et réduit le carburant."""
        fuel_needed = distance * 0.1  # 10% de consommation par 100 km
        if self.fuel < fuel_needed:
            print(f"🚨 {self.flight_name} n'a pas assez de carburant pour voler {distance} km!")
            return
        self.fuel -= fuel_needed
        print(f"✈️ {self.flight_name} a volé {distance} km, carburant restant: {self.fuel:.1f}%")

# 🚀 Test du nouveau système avec décorateurs et générateurs
plane1 = Aircraft(capacity=180, fuel=50.0)
plane2 = Aircraft(capacity=220, fuel=75.0)

print(plane1.flight_name)  # AF100
print(plane2.flight_name)  # AF101

plane1.fly(200)  # ✅ Effectue un vol et réduit le carburant
plane1.refuel(30)  # ✅ Recharge du carburant
# plane1.refuel("beaucoup")  # ❌ TypeError (grâce au décorateur @type_check)
```

---

## **🔹 4. Résumé des améliorations**
| **Amélioration** | **Pourquoi ?** | **Impact** |
|-----------------|---------------|-----------|
| **`@type_check`** | Vérifie les types des arguments | **Évite les erreurs inattendues** |
| **Générateur `flight_number_generator`** | Génère des numéros à la demande | **Optimise la mémoire et évite les doublons** |
| **Utilisation du décorateur `@type_check` dans `Aircraft`** | Sécurise les entrées utilisateur | **Améliore la robustesse du code** |

---

## **🔥 Conclusion**
✅ **Un code plus sécurisé** avec le **décorateur `@type_check`**.  
✅ **Un code plus optimisé** avec un **générateur de numéros de vol**.  
✅ **Facilité d’extension** et **bonne gestion des ressources**.  
