from datetime import time
import time as ptime
from functools import wraps

def require_auth(func):
    """Décorateur qui vérifie si l'utilisateur est connecté."""
    def wrapper(user):
        if not user.get("authenticated", False):
            print("⛔ Accès refusé !")
            return
        return func(user)
    return wrapper

@require_auth
def show_dashboard(user):
    print(f"📊 Tableau de bord de {user['name']}")

user1 = {"name": "Alice", "authenticated": True}
user2 = {"name": "Bob", "authenticated": False}

show_dashboard(user1)  # ✅ Affiche le dashboard
show_dashboard(user2)  # ⛔ Accès refusé !

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Appel de {func.__name__} avec {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} a retourné {result}")
        return result
    return wrapper

carre = lambda v:v**2



@log_decorator
def square(v):
    return v**2

@log_decorator
def connect(user,password):
    print(user,password)


square(5)
connect("john","john")

def zeromin(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result<0:
            result = 0
        return result
    return wrapper

@zeromin
def calcul_temperature(v):
    return -273 + v**2


print(calcul_temperature(5))

# decorateur qui calcul le temps passe
def timeit(func):
    """
    Décorateur qui mesure le temps d'exécution d'une fonction.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = ptime.perf_counter()  # Démarrer le chrono
        result = func(*args, **kwargs)
        end_time = ptime.perf_counter()  # Arrêter le chrono
        elapsed_time = end_time - start_time
        print(f"⏱️ Temps d'exécution de {func.__name__}: {elapsed_time:.6f} secondes")
        return result
    return wrapper



@timeit
def duree(sec):
    ptime.sleep(sec)


duree(1)
duree(2)

def validate_types(**type_rules):
    """
    Decorator to validate function parameter types.

    :param type_rules: Expected types for specific parameters (as keyword arguments).
    :raises TypeError: If the argument does not match the expected type.
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Get function argument names
            from inspect import signature
            sig = signature(func)
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()

            # Validate each specified parameter
            for param, expected_type in type_rules.items():
                if param in bound_args.arguments:
                    value = bound_args.arguments[param]
                    if not isinstance(value, expected_type):
                        raise TypeError(
                            f"Argument '{param}' must be of type {expected_type.__name__}, "
                            f"but got {type(value).__name__} instead."
                        )

            return func(*args, **kwargs)

        return wrapper

    return decorator



@validate_types(name=str, age=int, score=float)
def create_user(name, age, score):
    print(f"User: {name}, Age: {age}, Score: {score}")

create_user("Alain",40,100.5)
create_user("Alain","40",100)

