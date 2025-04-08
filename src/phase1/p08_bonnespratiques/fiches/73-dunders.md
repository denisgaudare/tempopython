# **📌 Les Dunder Methods (`__dunder__`) en Python : Essentiels pour la lisibilité et les performances 🚀**

Les **Dunder Methods** (méthodes "double underscore", ex: `__init__`, `__str__`, `__call__`...) permettent de **personnaliser le comportement des objets** en Python. Elles sont **essentielles** pour :

✅ **Améliorer la lisibilité du code** (surcharge d'opérateurs, affichage personnalisé).  
✅ **Optimiser les performances** (éviter les répétitions, utiliser des structures internes optimisées).  
✅ **Créer des classes Python idiomatiques** et compatibles avec les fonctionnalités natives du langage.  

---

# **🔹 1. Dunder Methods essentielles pour la lisibilité**
Ces méthodes rendent le code **plus clair et intuitif** en définissant **comment un objet doit se comporter dans un contexte donné**.

## **1.1 `__str__` et `__repr__` → Améliorer l'affichage**
📌 **`__str__` est utilisé pour l'affichage utilisateur** (`print(obj)`).  
📌 **`__repr__` est utilisé pour le debugging et les développeurs** (`repr(obj)`).

### **Exemple**
```python
class Aircraft:
    def __init__(self, flight_name: str, capacity: int):
        self.flight_name = flight_name
        self.capacity = capacity

    def __str__(self):
        """Affichage convivial"""
        return f"✈️ Vol {self.flight_name}, Capacité: {self.capacity} passagers."

    def __repr__(self):
        """Affichage pour le debugging"""
        return f"Aircraft(flight_name='{self.flight_name}', capacity={self.capacity})"

plane = Aircraft("AF101", 180)
print(plane)  # Utilise __str__
print(repr(plane))  # Utilise __repr__
```
✅ **Lisibilité accrue** : `print(plane)` est plus parlant que `<Aircraft object at 0x...>`  
✅ **Facilite le debugging** : `repr()` permet de **reconstruire l’objet** à partir de la sortie.

---

## **1.2 `__len__` et `__bool__` → Personnaliser `len()` et `bool()`**
📌 **Définit comment un objet est évalué en termes de taille (`len()`) et de vérité (`bool()`).**

### **Exemple**
```python
class Airport:
    def __init__(self, flights: list):
        self.flights = flights

    def __len__(self):
        """Permet d'utiliser len(objet)"""
        return len(self.flights)

    def __bool__(self):
        """Un aéroport est considéré comme actif s'il a des vols"""
        return bool(self.flights)

airport = Airport(["AF101", "LH202"])
print(len(airport))  # 2
print(bool(airport))  # True

empty_airport = Airport([])
print(bool(empty_airport))  # False
```
✅ **Lisibilité** : `len(airport)` au lieu de `len(airport.flights)`.  
✅ **Code idiomatique** : `if airport:` est plus naturel que `if len(airport) > 0`.

---

# **🔹 2. Dunder Methods pour la surcharge d’opérateurs**
Ces méthodes permettent **d’utiliser des opérateurs (`+`, `-`, `==`, etc.) sur des objets personnalisés**.

## **2.1 `__eq__`, `__lt__`, `__gt__` → Comparer des objets**
📌 **Permet d’utiliser `<`, `>`, `==` pour comparer des objets comme des valeurs standards.**

### **Exemple**
```python
class Aircraft:
    def __init__(self, flight_name: str, capacity: int):
        self.flight_name = flight_name
        self.capacity = capacity

    def __eq__(self, other):
        """Deux avions sont égaux s'ils ont la même capacité"""
        return self.capacity == other.capacity

    def __lt__(self, other):
        """Un avion est plus petit qu'un autre si sa capacité est moindre"""
        return self.capacity < other.capacity

plane1 = Aircraft("AF101", 180)
plane2 = Aircraft("LH202", 200)
print(plane1 == plane2)  # False
print(plane1 < plane2)   # True
```
✅ **Lisibilité améliorée** : `plane1 < plane2` est plus naturel que `plane1.capacity < plane2.capacity`.  
✅ **Facilite le tri et les comparaisons dans des listes**.

---

## **2.2 `__add__`, `__sub__`, `__mul__` → Opérations arithmétiques**
📌 **Permet d'utiliser `+`, `-`, `*` entre objets personnalisés.**

### **Exemple**
```python
class Fuel:
    def __init__(self, liters: float):
        self.liters = liters

    def __add__(self, other):
        """Additionne la quantité de carburant"""
        return Fuel(self.liters + other.liters)

fuel1 = Fuel(50)
fuel2 = Fuel(30)
total_fuel = fuel1 + fuel2
print(total_fuel.liters)  # 80
```
✅ **Éviter d'écrire `fuel1.liters + fuel2.liters` partout**.  
✅ **Permet des calculs d’objets personnalisés de manière intuitive**.

---

# **🔹 3. Dunder Methods pour les performances**
Certains **dunders permettent d’optimiser l’exécution** en évitant des appels inutiles.

## **3.1 `__slots__` → Économie de mémoire**
📌 **Évite la création d’un `__dict__` pour chaque instance**, réduisant la mémoire utilisée.

### **Exemple**
```python
class OptimizedAircraft:
    __slots__ = ['flight_name', 'capacity']  # Restreint les attributs

    def __init__(self, flight_name: str, capacity: int):
        self.flight_name = flight_name
        self.capacity = capacity

plane = OptimizedAircraft("AF101", 180)
# plane.extra_attr = "Test"  # ❌ AttributeError (bloque les attributs non définis)
```
✅ **Réduction de la mémoire** pour les objets massivement créés.  
✅ **Sécurise la structure des objets**.

---

## **3.2 `__call__` → Rendre un objet appelable**
📌 **Permet de traiter une instance de classe comme une fonction.**

### **Exemple**
```python
class FlightScheduler:
    def __call__(self, flight_name):
        print(f"📅 Planification du vol {flight_name}")

scheduler = FlightScheduler()
scheduler("AF101")  # 📅 Planification du vol AF101
```
✅ **Facilite l’usage d’objets configurables** sans avoir besoin de méthodes spécifiques.  
✅ **Améliore la flexibilité et la lisibilité du code**.

---

## **3.3 `__iter__` et `__next__` → Rendre un objet itérable**
📌 **Permet d'utiliser `for` directement sur un objet.**

### **Exemple**
```python
class FlightIterator:
    def __init__(self, flights):
        self.flights = flights
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.flights):
            raise StopIteration
        flight = self.flights[self.index]
        self.index += 1
        return flight

airport = FlightIterator(["AF101", "LH202", "BA303"])
for flight in airport:
    print(flight)  # AF101, LH202, BA303
```
✅ **Évite de devoir gérer manuellement les index et les `while`**.  
✅ **Optimise les itérations sur de grandes structures de données**.

---

# **🔥 Conclusion : Pourquoi maîtriser les Dunder Methods ?**
| **Pourquoi utiliser les Dunder Methods ?** ✅ |
|---------------------------------------------|
| **Améliore la lisibilité** en surchargeant `print()`, `+`, `==`, etc. |
| **Optimise les performances** avec `__slots__`, `__iter__`, `__call__`. |
| **Rend les objets compatibles avec les structures Python natives** (`len(obj)`, `bool(obj)`, `for obj in iterable`). |
| **Facilite la maintenance** en évitant les méthodes redondantes et en intégrant les conventions Python. |
