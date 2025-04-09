Les **décorateurs** en Python sont des fonctions qui modifient le comportement d'autres fonctions ou classes sans changer leur code source. Ils sont souvent utilisés pour :

### 1. **Ajouter des fonctionnalités sans modifier le code d’origine**
   - Exemple : journalisation des appels de fonction
   - Cas d’usage : enregistrer les entrées/sorties d’une fonction sans toucher au code.

```python
import time

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Appel de {func.__name__} avec {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} a retourné {result}")
        return result
    return wrapper

@log_decorator
def addition(a, b):
    return a + b

addition(3, 4)
```

### 2. **Gestion du temps d'exécution**
   - Exemple : mesurer la durée d’exécution d’une fonction
   - Cas d’usage : identifier les goulots d’étranglement dans le code

```python
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} exécutée en {end_time - start_time:.4f} secondes")
        return result
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(2)
    print("Fonction terminée")

slow_function()
```

### 3. **Contrôle des accès et authentification**
   - Exemple : vérifier si un utilisateur est autorisé
   - Cas d’usage : protéger certaines parties d’une application

```python
def require_authentication(func):
    def wrapper(user, *args, **kwargs):
        if not user.get("is_authenticated", False):
            print("Accès refusé !")
            return None
        return func(user, *args, **kwargs)
    return wrapper

@require_authentication
def get_sensitive_data(user):
    return "Données sensibles"

user = {"is_authenticated": True}
print(get_sensitive_data(user))

user_not_auth = {"is_authenticated": False}
print(get_sensitive_data(user_not_auth))
```

### 4. **Mémoïsation (mise en cache des résultats)**
   - Exemple : éviter de recalculer des résultats coûteux
   - Cas d’usage : accélérer des fonctions appelées fréquemment

```python
from functools import lru_cache

@lru_cache(maxsize=5)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))  # Calculé une fois
print(fibonacci(10))  # Récupéré depuis le cache
```

### 5. **Validation des entrées**
   - Exemple : vérifier que les arguments respectent certaines conditions
   - Cas d’usage : éviter les erreurs d’exécution en validant les entrées

```python
def validate_non_negative(func):
    def wrapper(x):
        if x < 0:
            raise ValueError("L'entrée doit être positive")
        return func(x)
    return wrapper

@validate_non_negative
def sqrt(x):
    return x ** 0.5

print(sqrt(9))
# print(sqrt(-1))  # Provoquera une erreur
```

---

Un décorateur paramétrable qui valide **le typage des arguments et des retours** d'une fonction peut être conçu en utilisant `inspect.signature` pour récupérer la signature de la fonction et comparer les types des arguments.

---

### **Décorateur de validation des types paramétrable**
Il accepte un dictionnaire `types` définissant les types des arguments et du retour de la fonction.

```python
import inspect

def type_checker(types):
    def decorator(func):
        sig = inspect.signature(func)  # Récupère la signature de la fonction
        
        def wrapper(*args, **kwargs):
            bound_args = sig.bind(*args, **kwargs)  # Associe les arguments aux paramètres
            bound_args.apply_defaults()

            # Vérification des types des arguments
            for param, value in bound_args.arguments.items():
                if param in types and not isinstance(value, types[param]):
                    raise TypeError(f"Argument '{param}' doit être de type {types[param].__name__}, mais {type(value).__name__} reçu")

            # Exécution de la fonction
            result = func(*args, **kwargs)

            # Vérification du type de retour
            if "return" in types and not isinstance(result, types["return"]):
                raise TypeError(f"La valeur de retour doit être de type {types['return'].__name__}, mais {type(result).__name__} reçu")

            return result
        
        return wrapper
    return decorator
```

---

### **Exemple d'utilisation**
On l'utilise en lui passant un dictionnaire de types pour valider les arguments et le retour.

```python
@type_checker({"a": int, "b": int, "return": int})
def addition(a, b):
    return a + b

print(addition(3, 5))  # OK
# print(addition(3, "5"))  # Provoquera une erreur de type
```

---

### **Cas avec plusieurs types acceptés**
On peut permettre plusieurs types en utilisant un `tuple` pour la vérification.

```python
@type_checker({"x": (int, float), "y": (int, float), "return": float})
def multiply(x, y):
    return x * y

print(multiply(3, 2.5))  # OK
# print(multiply("3", 2))  # Erreur : 'x' doit être un nombre
```

---

### **Avantages de ce décorateur :**
✅ **Paramétrable** : on peut spécifier les types à valider par fonction  
✅ **Générique** : fonctionne pour toutes les fonctions  
✅ **Vérifie aussi le type du retour**  
✅ **Prend en charge plusieurs types par paramètre (ex. `int` et `float`)**  
