Les **décorateurs** en Python sont très flexibles et peuvent être utilisés dans de nombreux cas. Voici d'autres cas d'utilisation courants :

---

## **6. Gestion des exceptions (try/except automatique)**
### *Cas d’usage* : éviter de répéter les blocs `try/except` pour gérer les erreurs

```python
def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Erreur dans {func.__name__}: {e}")
            return None  # On peut aussi lever une exception personnalisée
    return wrapper

@exception_handler
def divide(a, b):
    return a / b

print(divide(10, 2))  # OK
print(divide(10, 0))  # Capture et affiche l'erreur
```

---

## **7. Répéter une fonction en cas d’échec (retry)**
### *Cas d’usage* : tenter plusieurs fois une opération en cas d’échec (utile pour des appels réseau)

```python
import time
import random

def retry(attempts=3, delay=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Échec {i+1}/{attempts} : {e}")
                    time.sleep(delay)
            print("Opération échouée après plusieurs tentatives.")
            return None
        return wrapper
    return decorator

@retry(attempts=5, delay=2)
def unstable_function():
    if random.random() < 0.7:  # 70% de chances d’échouer
        raise ValueError("Problème aléatoire")
    return "Succès !"

print(unstable_function())
```

---

## **8. Singleton (assurer qu'une classe n’a qu’une seule instance)**
### *Cas d’usage* : assurer qu’une classe a une unique instance (ex. base de données, configuration)

```python
def singleton(cls):
    instances = {}
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper

@singleton
class Database:
    def __init__(self):
        print("Connexion à la base de données...")

db1 = Database()
db2 = Database()

print(db1 is db2)  # True : même instance
```

---

## **9. Modification automatique des résultats (ex. mise en majuscule)**
### *Cas d’usage* : transformer les résultats d’une fonction

```python
def uppercase_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper() if isinstance(result, str) else result
    return wrapper

@uppercase_result
def greet(name):
    return f"Bonjour, {name}"

print(greet("Alice"))  # "BONJOUR, ALICE"
```

---

## **10. Enregistrement des appels de fonction (audit log)**
### *Cas d’usage* : suivre les appels et arguments pour des logs ou du debug

```python
def audit_log(func):
    def wrapper(*args, **kwargs):
        print(f"Appel de {func.__name__} avec {args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@audit_log
def calculer(a, b):
    return a * b

print(calculer(3, 4))  # Affiche l’appel avant d’exécuter la fonction
```

---

## **11. Vérification des permissions**
### *Cas d’usage* : restreindre l'accès à certaines fonctionnalités en fonction des rôles utilisateurs

```python
def require_role(role):
    def decorator(func):
        def wrapper(user, *args, **kwargs):
            if user.get("role") != role:
                raise PermissionError(f"Accès refusé : {user.get('role')} ne peut pas exécuter {func.__name__}")
            return func(user, *args, **kwargs)
        return wrapper
    return decorator

@require_role("admin")
def supprimer_fichier(user, fichier):
    print(f"{fichier} supprimé !")

admin = {"role": "admin"}
user = {"role": "user"}

supprimer_fichier(admin, "data.txt")  # OK
# supprimer_fichier(user, "data.txt")  # Provoque une erreur d'accès
```

---

## **12. Exécuter une fonction en arrière-plan (threading)**
### *Cas d’usage* : lancer des tâches en arrière-plan sans bloquer l'exécution principale

```python
import threading

def run_in_thread(func):
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=func, args=args, kwargs=kwargs)
        thread.start()
        return thread  # On peut récupérer le thread si besoin
    return wrapper

@run_in_thread
def process_data():
    print("Traitement en arrière-plan...")
    time.sleep(3)
    print("Traitement terminé !")

process_data()
print("Le programme continue pendant le traitement en arrière-plan")
```

---

### **Conclusion**
Les décorateurs sont extrêmement **puissants** et permettent :
✅ D'ajouter des fonctionnalités sans modifier le code d’origine  
✅ De factoriser du code répétitif  
✅ D’améliorer la lisibilité et la maintenance  

