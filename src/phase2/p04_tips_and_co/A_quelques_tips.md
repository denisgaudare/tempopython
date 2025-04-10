
#fusion

d1 = {"a": 1}
d2 = {"b": 2}
d3 = d1 | d2  # nouveau dictionnaire fusionné

# double liste
keys = ["a", "b"]
values = [1, 2]
d = dict(zip(keys, values))

# counter
from collections import Counter
c = Counter("abracadabra")
print(c["a"])  # 5

# intersection de set
s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(s1 & s2)  # {2, 3}

# a des doublons
def has_duplicates(seq):
    return len(seq) != len(set(seq))

# function partielle
from functools import partial

def power(base, exp):
    return base ** exp

square = partial(power, exp=2)
cube = partial(power, exp=3)

print(square(4))  # 16
print(cube(2))    # 8


# partial
bin_to_int = partial(int, base=2)
print(bin_to_int("1011"))  # 11

------

# 🧠 Design Patterns utiles en Python

---

## 1. **Singleton** (🧍Instance unique)

### 📌 Utilité :
Garder **une seule instance** partagée dans toute l’application (ex : connexion base, config globale).

### 🧱 Exemple :
```python
class Config:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
```

✅ Préférer l’utiliser avec **des modules Python** (qui sont eux-mêmes des singletons naturels).

---

## 2. **Factory** (🏭 Générateur d’objets)

### 📌 Utilité :
Créer des objets **sans exposer leur classe concrète** ; utile pour l’extensibilité.

### 🧱 Exemple :
```python
class Dog:
    def speak(self):
        return "Woof"

class Cat:
    def speak(self):
        return "Meow"

def animal_factory(kind: str):
    return {"dog": Dog(), "cat": Cat()}[kind]
```

---

## 3. **Strategy** (🎯 Comportement interchangeable)

### 📌 Utilité :
Changer dynamiquement le **comportement d’un objet** sans changer son code.

### 🧱 Exemple :
```python
from typing import Callable

def execute(strategy: Callable[[int, int], int], a: int, b: int):
    return strategy(a, b)

print(execute(lambda x, y: x + y, 2, 3))  # 5
```

✅ Très idiomatique en Python avec les fonctions de premier ordre (higher-order functions).

---

## 4. **Decorator** (🎁 Comportement autour d’une fonction)

### 📌 Utilité :
Ajouter des fonctionnalités à une fonction **sans la modifier** directement.

### 🧱 Exemple :
```python
def logged(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@logged
def greet(name: str):
    return f"Hello {name}"
```

---

## 5. **Observer** (📣 Événements et réactivité)

### 📌 Utilité :
Notifier plusieurs objets lorsqu’un changement a lieu dans un autre objet.

### 🧱 Exemple :
```python
class Observable:
    def __init__(self):
        self._observers = []

    def register(self, callback):
        self._observers.append(callback)

    def notify(self, message):
        for callback in self._observers:
            callback(message)

obs = Observable()
obs.register(lambda msg: print(f"Received: {msg}"))
obs.notify("Hello world")
```

---

## 6. **Command** (📦 Encapsulation d’action)

### 📌 Utilité :
Encapsuler une action comme un objet pour la stocker, rejouer, annuler, etc.

### 🧱 Exemple :
```python
class PrintCommand:
    def __init__(self, text: str):
        self.text = text

    def execute(self):
        print(self.text)

cmd = PrintCommand("Hello")
cmd.execute()
```

---

## 7. **Adapter** (🔌 Compatibilité d’interface)

### 📌 Utilité :
Faire en sorte que des classes avec des interfaces **incompatibles** fonctionnent ensemble.

### 🧱 Exemple :
```python
class LegacyPrinter:
    def print_text(self, text):
        print(text)

class Adapter:
    def __init__(self, adaptee: LegacyPrinter):
        self.adaptee = adaptee

    def print(self, text):
        self.adaptee.print_text(text)
```

## 🛠️ Et aussi...

| Pattern     | Utilité principale                          | Utilisation typique en Python          |
|-------------|----------------------------------------------|----------------------------------------|
| **Builder** | Construction progressive d’un objet         | `attrs`, `dataclasses`, `pydantic`     |
| **Proxy**   | Contrôle d’accès à un objet (lazy, cache…)  | Logger, accès distant, mock            |
| **Chain of Responsibility** | Passage d’une requête à travers une chaîne | Middleware (ex: FastAPI, Flask)       |
| **Template Method** | Squelette d’algorithme avec des hooks | Classes abstraites + héritage         |
