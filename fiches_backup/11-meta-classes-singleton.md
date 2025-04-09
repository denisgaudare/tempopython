### **Cas Pratique : Métaclasse pour un Singleton en Python**
Un **singleton** est un design pattern qui garantit qu'une **classe donnée n'a qu'une seule instance** dans tout le programme.

On peut implémenter un singleton en Python avec une **métaclasse**, ce qui permet d’appliquer cette contrainte à **toutes les classes qui l’utilisent**.

---

## **1. Implémentation d'un Singleton avec une Métaclasse**
```python
class SingletonMeta(type):
    """Métaclasse pour implémenter le pattern Singleton"""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """S'assure qu'une seule instance est créée"""
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

# Classe utilisant la métaclasse Singleton
class SingletonClass(metaclass=SingletonMeta):
    def __init__(self, value):
        self.value = value

# Test du singleton
obj1 = SingletonClass("Premier")
obj2 = SingletonClass("Deuxième")

print(obj1.value)  # Affiche "Premier"
print(obj2.value)  # Affiche "Premier"
print(obj1 is obj2)  # True, c'est bien la même instance !
```

---

### **🔍 Explication**
- `SingletonMeta` stocke **une seule instance** pour chaque classe utilisant cette métaclasse.
- `__call__` est **surchargée** : avant de créer une nouvelle instance, on vérifie si une instance existe déjà.
- Si une instance **existe déjà**, on la retourne au lieu de créer un nouvel objet.

---

## **2. Version plus avancée : Singleton avec Thread-Safety**
Si ton application est **multi-threadée**, il faut protéger l’accès concurrentiel à l’instance.

```python
import threading

class ThreadSafeSingletonMeta(type):
    """Métaclasse pour un Singleton thread-safe"""
    _instances = {}
    _lock = threading.Lock()  # Protection contre les accès concurrents

    def __call__(cls, *args, **kwargs):
        with cls._lock:  # Verrou pour éviter la création multiple en parallèle
            if cls not in cls._instances:
                cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

# Classe utilisant la métaclasse Singleton thread-safe
class SingletonThreadSafe(metaclass=ThreadSafeSingletonMeta):
    def __init__(self, value):
        self.value = value

# Test en multi-threading
def create_instance():
    instance = SingletonThreadSafe("Unique Instance")
    print(f"Instance ID: {id(instance)} - Value: {instance.value}")

# Lancement de plusieurs threads
threads = [threading.Thread(target=create_instance) for _ in range(5)]

for t in threads:
    t.start()

for t in threads:
    t.join()
```

✅ **Pourquoi utiliser `_lock` ?**
- **Évite les instanciations concurrentes** si plusieurs threads appellent la classe en même temps.
- **Garantit l’unicité de l’instance**, même dans des environnements multi-threadés.

---

## **3. Version utilisant `contextlib` pour une Factory Singleton**
Si tu veux **simplifier l’usage du singleton** avec `contextlib`, voici une version alternative :

```python
from contextlib import contextmanager

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class MySingleton(metaclass=SingletonMeta):
    def __init__(self, value):
        self.value = value

@contextmanager
def singleton_context(value):
    """Permet d'utiliser un singleton temporairement"""
    instance = MySingleton(value)
    yield instance

# Utilisation avec `with`
with singleton_context("Test") as obj:
    print(obj.value)  # "Test"
```

✅ **Pourquoi cette approche ?**
- Permet **d’utiliser un singleton temporairement** sans l’imposer globalement.
- Idéal si l’on veut encapsuler un singleton **dans un contexte limité**.

---

### **📌 Comparatif des Approches**
| Méthode | Cas d'utilisation | Avantages | Inconvénients |
|---------|------------------|-----------|--------------|
| **Métaclasse Singleton classique** | Assurer une seule instance | Simple et efficace | Pas thread-safe |
| **Métaclasse Singleton thread-safe** | Environnements multi-threadés | Protège l'instance | Légère surcharge |
| **`contextlib` avec Factory** | Singleton temporaire | Flexible | Moins standard |

---

### **📌 Conclusion**
- **Si tu veux un singleton simple** → Utilise la **métaclasse `SingletonMeta`**.
- **Si ton application est multi-threadée** → Ajoute **un verrou (`_lock`)**.
- **Si tu veux un singleton temporaire** → Utilise **`contextlib`**.
