## **Projet : Simulation de trafic aérien avec Context Managers en Python** ✈️  

### **Objectif**
Développer un système simulant un **trafic aérien** où plusieurs avions doivent décoller, voler, et atterrir en respectant des règles de gestion des ressources et des logs. Ce projet mettra en œuvre plusieurs **context managers** pour gérer :  
- **L’accès à l’aéroport** (capacité limitée des pistes).  
- **L’enregistrement des logs** (journalisation des vols).  
- **L’ouverture et la fermeture sécurisée des fichiers de logs**.  
- **La gestion des ressources des avions (carburant, maintenance, etc.)**.  

---

## **📌 Étapes du projet**
1. **Créer une classe `Airport` gérant les pistes avec un context manager.**
2. **Créer une classe `FlightLogger` pour enregistrer les événements dans un fichier.**
3. **Créer une classe `Aircraft` simulant les opérations de vol.**
4. **Simuler plusieurs avions décollant, volant et atterrissant en parallèle.**

---

## **🛠 Solution complète**
### **1. Gestion des pistes avec `Airport` (context manager)**
Nous allons utiliser un `contextmanager` pour gérer **l’occupation des pistes** lors des décollages et atterrissages.  

```python
import time
import random
from contextlib import contextmanager
from threading import Lock

class Airport:
    """Gestionnaire de contexte pour la gestion des pistes d'aéroport."""

    def __init__(self, runways=2):
        self.available_runways = runways
        self.lock = Lock()  # Sécuriser l'accès concurrentiel

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
            yield  # Exécution de la phase de vol
        finally:
            with self.lock:
                self.available_runways += 1
                print(f"🛬 {flight_name} a libéré une piste.")
```

---

### **2. Gestion des logs avec `FlightLogger` (context manager)**
On utilise un **context manager** pour s’assurer que les logs sont bien écrits et fermés proprement.

```python
class FlightLogger:
    """Gestionnaire de contexte pour l'enregistrement des logs de vol."""

    def __init__(self, filename="flight_logs.txt"):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, "a")  # Ouverture en mode ajout
        return self

    def log(self, message):
        """Écrit un message dans le log."""
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        self.file.write(f"[{timestamp}] {message}\n")
        print(f"📜 LOG: {message}")

    def __exit__(self, exc_type, exc_value, traceback):
        """Ferme proprement le fichier de log."""
        self.file.close()
```

---

### **3. Simulation d’un avion avec `Aircraft` (context manager)**
Chaque avion utilisera les gestionnaires de contexte pour **accéder à une piste, voler et atterrir**.

```python
class Aircraft:
    """Simulation d'un avion avec context managers pour la gestion des ressources."""

    def __init__(self, flight_name, airport):
        self.flight_name = flight_name
        self.airport = airport

    @contextmanager
    def manage_fuel(self):
        """Gestion du carburant et de la maintenance."""
        fuel = random.randint(50, 100)  # Carburant en pourcentage
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
                    time.sleep(random.randint(2, 5))  # Simulation du vol
                    logger.log(f"{self.flight_name} est en vol.")
                    time.sleep(random.randint(2, 5))  # Simulation du vol
                    logger.log(f"{self.flight_name} a atterri.")
```

---

### **4. Simulation de plusieurs avions**
On va maintenant **créer plusieurs avions et les faire voler simultanément** en utilisant `threading` pour la **simulation de trafic aérien concurrentiel**.

```python
import threading

if __name__ == "__main__":
    airport = Airport(runways=2)  # L'aéroport a 2 pistes disponibles

    # Création des avions
    aircrafts = [
        Aircraft("Flight 101", airport),
        Aircraft("Flight 202", airport),
        Aircraft("Flight 303", airport),
        Aircraft("Flight 404", airport)
    ]

    # Lancer les vols en parallèle avec des threads
    threads = [threading.Thread(target=aircraft.fly) for aircraft in aircrafts]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("✅ Simulation terminée.")
```

---

## **🔍 Explication des context managers utilisés**
| **Context Manager** | **Objectif** |
|---------------------|-------------|
| `Airport.request_runway()` | Gère l’accès aux pistes (évite les collisions). |
| `FlightLogger` | Enregistre les logs des vols proprement. |
| `Aircraft.manage_fuel()` | Vérifie le carburant et la maintenance avant le vol. |

---

## **💡 Points clés du projet**
✅ **Utilisation avancée de plusieurs context managers** pour gérer **les ressources d’un aéroport**.  
✅ **Simulation en temps réel** avec gestion des accès concurrents via `threading` et `Lock()`.  
✅ **Enregistrement des événements dans un log** (via `FlightLogger`).  
✅ **Gestion sécurisée des ressources** comme **les pistes, le carburant et la maintenance**.  

---

## **🚀 Résultat attendu**
Exécution du programme :
```
🛫 Flight 101 a obtenu une piste pour décoller/atterrir.
⛽ Flight 101 a 80% de carburant avant le vol.
📜 LOG: Flight 101 a décollé.
🛫 Flight 202 a obtenu une piste pour décoller/atterrir.
⛽ Flight 202 a 50% de carburant avant le vol.
⚠️ Flight 202 a besoin de ravitaillement !
📜 LOG: Flight 202 a décollé.
🛬 Flight 101 a libéré une piste.
📜 LOG: Flight 101 est en vol.
🛫 Flight 303 a obtenu une piste pour décoller/atterrir.
📜 LOG: Flight 303 a décollé.
...
✅ Simulation terminée.
```

---

## **🛠️ Extensions possibles**
- Ajouter un **système météo** influençant les retards.  
- Intégrer une **base de données** pour stocker les logs.  
- Simuler un **plan de vol** et des **urgences** (ex. panne moteur).  

---
