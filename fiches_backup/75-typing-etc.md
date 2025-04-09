### **📌 Utilisation avancée de `typing` **

Le module `typing` de Python permet de **typer explicitement les fonctions, les classes et les structures de données**. Cela améliore la **lisibilité**, la **détection d'erreurs** et la **compréhension du code**.

---

# **🔹 1. Typage des variables et des fonctions**
```python
from typing import List, Dict

# Typage explicite des variables
flight_name: str = "Flight 101"
passenger_count: int = 180
fuel_level: float = 100.0
is_ready: bool = True

# Fonction avec annotation des types
def get_fuel_status(fuel: float) -> str:
    """Retourne le statut du carburant."""
    return "OK" if fuel > 50 else "LOW"

print(get_fuel_status(30.0))  # LOW
```
✅ **Avantages** :
- **Clarifie le code** dès la lecture.
- **Facilite la détection des erreurs** avec des outils comme `mypy`.

---

# **🔹 2. Typage des collections (`List`, `Dict`, `Tuple`)**
```python
from typing import List, Dict, Tuple

# Liste de noms de vols
flight_list: List[str] = ["Flight 101", "Flight 202", "Flight 303"]

# Dictionnaire contenant des vols avec leur nombre de passagers
flight_passengers: Dict[str, int] = {
    "Flight 101": 180,
    "Flight 202": 200
}

# Tuple représentant un avion (Nom, Capacité, Carburant)
aircraft_info: Tuple[str, int, float] = ("Flight 101", 180, 75.5)

print(flight_list, flight_passengers, aircraft_info)
```
✅ **Avantages** :
- **Garantit la structure des données**.
- **Évite les erreurs de manipulation**.

---

# **🔹 3. Utilisation de `TypedDict` pour structurer des dictionnaires**
```python
from typing import TypedDict

class FlightData(TypedDict):
    flight_name: str
    capacity: int
    fuel: float

# Exemple de vol stocké sous forme de dictionnaire structuré
flight: FlightData = {
    "flight_name": "Flight 404",
    "capacity": 150,
    "fuel": 80.0
}

print(flight)
```
✅ **Avantages** :
- **Définit des structures claires** pour les dictionnaires.
- **Facilite la validation des données**.

---

# **🔹 4. Utilisation de `Protocol` pour une interface générique**
```python
from typing import Protocol

class Flyable(Protocol):
    def fly(self) -> None:
        """Méthode obligatoire pour voler."""
        pass

class Aircraft:
    def fly(self) -> None:
        print("🛫 L'avion décolle.")

class Drone:
    def fly(self) -> None:
        print("🚁 Le drone s'envole.")

def start_flight(vehicle: Flyable) -> None:
    """Accepte tout objet respectant l'interface `Flyable`."""
    vehicle.fly()

plane = Aircraft()
drone = Drone()

start_flight(plane)  # 🛫 L'avion décolle.
start_flight(drone)  # 🚁 Le drone s'envole.
```
✅ **Avantages** :
- Permet de **vérifier qu'un objet implémente bien une interface**.
- Facilite **l'écriture de code générique et extensible**.

---

# **🔹 5. Utilisation de `NewType` pour renforcer les types**
```python
from typing import NewType

FlightCode = NewType("FlightCode", str)

def validate_flight_code(code: FlightCode) -> str:
    """Valide un code de vol spécifique."""
    if not code.startswith("FL"):
        raise ValueError("❌ Code de vol invalide")
    return f"✅ {code} est valide."

flight = FlightCode("FL1234")
print(validate_flight_code(flight))  # ✅ FL1234 est valide.
```
✅ **Avantages** :
- **Empêche la confusion entre types**.
- **Force un contrôle strict sur les valeurs acceptées**.

---

# **🔹 6. Utilisation de `Callable` pour typer des fonctions comme arguments**
```python
from typing import Callable

def execute_task(task: Callable[[str, int], str], name: str, priority: int) -> str:
    return task(name, priority)

def sample_task(name: str, priority: int) -> str:
    return f"Tâche {name} exécutée avec priorité {priority}."

result = execute_task(sample_task, "Maintenance", 1)
print(result)  # Tâche Maintenance exécutée avec priorité 1.
```
✅ **Avantages** :
- **Permet d'accepter des fonctions en argument avec des types stricts**.
- **Rend le code plus flexible et modulaire**.

---

# **🔹 7. Utilisation de `Union`, `Optional` et `Literal` pour plus de flexibilité**
```python
from typing import Union, Optional, Literal

# Une variable qui peut être un `int` ou `str`
data: Union[int, str] = "Flight 101"
data = 404  # Pas d'erreur

# Une valeur optionnelle
fuel: Optional[float] = None  # Peut être `None` ou un `float`

# Contraindre une variable à une liste de valeurs possibles
status: Literal["On Time", "Delayed", "Cancelled"] = "On Time"

print(data, fuel, status)
```
✅ **Avantages** :
- **Rend le code plus flexible** en acceptant plusieurs types.
- **Améliore la lisibilité et la validation automatique**.

---

## **📌 Récapitulatif des concepts `typing` avancés**
| **Concept**          | **Utilisation** | **Exemple** |
|----------------------|----------------|-------------|
| **Typage des fonctions** | Contraindre les types des paramètres et du retour | `def foo(x: int) -> str:` |
| **List, Dict, Tuple** | Typage explicite des collections | `List[int]`, `Dict[str, float]`, `Tuple[str, int]` |
| **TypedDict** | Structurer des dictionnaires | `class FlightData(TypedDict)` |
| **Protocol** | Définir des interfaces génériques | `class Flyable(Protocol):` |
| **NewType** | Créer un alias de type strict | `FlightCode = NewType("FlightCode", str)` |
| **Callable** | Accepter des fonctions comme arguments | `Callable[[int, int], str]` |
| **Union** | Autoriser plusieurs types | `Union[str, int]` |
| **Optional** | Accepter `None` comme valeur possible | `Optional[float]` |
| **Literal** | Restreindre à des valeurs précises | `Literal["On Time", "Delayed"]` |

---

# **🔥 Conclusion**
Le module `typing` permet d'écrire **un code plus lisible, sécurisé et maintenable**.  
✅ **Meilleure détection des erreurs**.  
✅ **Documentation et compréhension améliorées**.  
✅ **Permet l'utilisation d'outils de vérification comme `mypy`**.  

**🚀 Un bon développeur Python doit maîtriser `typing` pour produire du code professionnel et robuste !** 🔥