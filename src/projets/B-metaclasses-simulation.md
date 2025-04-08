### **🔍 Extension du projet : Utilisation de métaclasses pour ajouter des contrôles avancés**
Dans cette version améliorée, nous allons introduire plusieurs **métaclasses** pour **assurer des contraintes sur nos classes** :

1. **Vérification de la convention de nommage** (CamelCase obligatoire pour les classes).  
2. **Interdiction de l'héritage** (Empêcher l'extension de certaines classes).  
3. **Limitation du nombre d'instances** (Singleton ou limitation à un nombre défini d'objets).  

Ces contraintes seront appliquées aux **classes du projet aérien** (ex: `Airport`, `FlightLogger`, `Aircraft`).  

---

## **🛠️ Implémentation des métaclasses**

### **1. Métaclasse pour imposer la convention de nommage (CamelCase)**
Cette métaclasse vérifie que toutes les classes respectent la convention **CamelCase**.

```python
import re

class NamingConventionMeta(type):
    """Métaclasse imposant une convention de nommage en CamelCase."""
    
    def __new__(cls, name, bases, class_dict):
        if not re.match(r'^[A-Z][a-zA-Z0-9]*$', name):
            raise TypeError(f"❌ Le nom de la classe '{name}' ne respecte pas la convention CamelCase.")
        return super().__new__(cls, name, bases, class_dict)
```

---

### **2. Métaclasse pour empêcher l'héritage**
Cette métaclasse **empêche toute sous-classe** de la classe à laquelle elle est appliquée.

```python
class NoInheritanceMeta(type):
    """Métaclasse empêchant l'héritage de la classe."""

    def __new__(cls, name, bases, class_dict):
        if any(isinstance(base, NoInheritanceMeta) for base in bases):
            raise TypeError(f"❌ La classe '{name}' ne peut pas hériter d'une classe utilisant NoInheritanceMeta.")
        return super().__new__(cls, name, bases, class_dict)
```

---

### **3. Métaclasse pour limiter le nombre d'instances**
Cette métaclasse permet de **limiter** le nombre d’instances créées d’une classe.

```python
class InstanceLimiterMeta(type):
    """Métaclasse limitant le nombre d'instances d'une classe."""

    _instances = {}
    _max_instances = 2  # Modifier ici pour changer la limite

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = []
        
        if len(cls._instances[cls]) >= cls._max_instances:
            raise RuntimeError(f"❌ Impossible de créer plus de {cls._max_instances} instances de '{cls.__name__}'.")

        instance = super().__call__(*args, **kwargs)
        cls._instances[cls].append(instance)
        return instance
```

---

## **🔍 Intégration des métaclasses dans le projet**
Nous allons maintenant appliquer ces métaclasses aux classes du projet.

### **1. Classe `Airport` (Utilise `InstanceLimiterMeta` pour limiter les aéroports)**
```python
class Airport(metaclass=InstanceLimiterMeta):
    """Gestion des pistes d'aéroport, avec un nombre limité d'instances."""

    def __init__(self, runways=2):
        self.available_runways = runways
        self.lock = Lock()

    @contextmanager
    def request_runway(self, flight_name):
        """Gestion de l'accès aux pistes."""
        with self.lock:
            if self.available_runways == 0:
                print(f"⏳ {flight_name} attend une piste...")
            while self.available_runways == 0:
                time.sleep(1)

            self.available_runways -= 1
            print(f"🛫 {flight_name} a obtenu une piste pour décoller/atterrir.")

        try:
            yield
        finally:
            with self.lock:
                self.available_runways += 1
                print(f"🛬 {flight_name} a libéré une piste.")
```

---

### **2. Classe `FlightLogger` (Utilise `NoInheritanceMeta` pour empêcher l'héritage)**
```python
class FlightLogger(metaclass=NoInheritanceMeta):
    """Gestionnaire de logs, empêchant l'héritage."""

    def __init__(self, filename="flight_logs.txt"):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, "a")
        return self

    def log(self, message):
        """Écrit un message dans le log."""
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        self.file.write(f"[{timestamp}] {message}\n")
        print(f"📜 LOG: {message}")

    def __exit__(self, exc_type, exc_value, traceback):
        """Ferme le fichier de log."""
        self.file.close()
```

**❌ Essayer d’hériter de `FlightLogger` lève une erreur** :
```python
class CustomLogger(FlightLogger):  
    pass
# TypeError: La classe 'CustomLogger' ne peut pas hériter d'une classe utilisant NoInheritanceMeta.
```

---

### **3. Classe `Aircraft` (Utilise `NamingConventionMeta` pour vérifier le nommage)**
```python
class Aircraft(metaclass=NamingConventionMeta):
    """Simulation d'un avion, avec contrôle de nommage en CamelCase."""

    def __init__(self, flight_name, airport):
        self.flight_name = flight_name
        self.airport = airport

    @contextmanager
    def manage_fuel(self):
        """Gestion du carburant et maintenance."""
        fuel = random.randint(50, 100)
        maintenance_check = random.choice([True, False])
        print(f"⛽ {self.flight_name} a {fuel}% de carburant avant le vol.")

        if fuel < 60:
            print(f"⚠️ {self.flight_name} a besoin de ravitaillement !")
        if maintenance_check:
            print(f"🔧 {self.flight_name} doit passer un contrôle technique avant le vol.")

        try:
            yield
        finally:
            print(f"🛑 {self.flight_name} vérifie son carburant après l'atterrissage.")

    def fly(self):
        """Simulation d'un cycle de vol."""
        with self.airport.request_runway(self.flight_name):
            with FlightLogger() as logger:
                with self.manage_fuel():
                    logger.log(f"{self.flight_name} a décollé.")
                    time.sleep(random.randint(2, 5))
                    logger.log(f"{self.flight_name} est en vol.")
                    time.sleep(random.randint(2, 5))
                    logger.log(f"{self.flight_name} a atterri.")
```

---

## **🔍 Test des nouvelles contraintes**

### **1. Vérification de la convention de nommage**
✅ **Valide** :
```python
class MyPlane(Aircraft):  # ✅ Correct
    pass
```
❌ **Erreur** :
```python
class my_plane(Aircraft):  # ❌ Mauvaise convention de nommage
    pass
# TypeError: Le nom de la classe 'my_plane' ne respecte pas la convention CamelCase.
```

---

### **2. Empêcher l’héritage**
❌ **Erreur** :
```python
class CustomLogger(FlightLogger):  
    pass
# TypeError: La classe 'CustomLogger' ne peut pas hériter d'une classe utilisant NoInheritanceMeta.
```

---

### **3. Limiter le nombre d’instances**
```python
airport1 = Airport()
airport2 = Airport()
airport3 = Airport()  # ❌ Erreur : dépassement de la limite d'instances
# RuntimeError: Impossible de créer plus de 2 instances de 'Airport'.
```

---

## **🚀 Conclusion**
Ce projet utilise **plusieurs métaclasses** pour ajouter des **règles strictes** aux classes :
1. ✅ **Convention de nommage** avec `NamingConventionMeta`.  
2. ✅ **Empêcher l’héritage** avec `NoInheritanceMeta`.  
3. ✅ **Limiter le nombre d’instances** avec `InstanceLimiterMeta`.  

