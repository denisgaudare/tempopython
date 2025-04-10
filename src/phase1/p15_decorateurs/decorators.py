import logging
from time import time

#  print(__name__) import or direct run ????

TIME_ENABLE = True

from time import monotonic



def mon_decorateur(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        # code décorateur
        return f(*args, **kwargs)

    return wrapper

def chrono(func):
    def wrapper(*args, **kwargs):
        depart = monotonic()  # avant
        res = func(*args, **kwargs)
        print("Durée : {:.1f}ms".format((monotonic() - depart) * 1000))  # après
        return res

    return wrapper


def timeit(func):
    if not TIME_ENABLE:
        return func

    # This function shows the execution time of
    # the function object passed
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {func.__name__!r} executed in {(t2 - t1):.4f}s')
        return result

    return wrap_func


def pourcentage(func):
    def wrapper(*args, **kwargs):
        # ici on peut insérer des choses à faire avant l'appel
        res = func(*args, **kwargs)
        if res < 0:
            res = 0
        if res > 100:
            res = 100
        # ici on peut insérer des choses à faire après l'appel
        return res

    return wrapper


def memoize(f):
    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]

    return helper


def retry(max_tries):
    def decorator(func):
        def wrapper(*args, **kwargs):
            tries = 1
            while True:
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if tries >= max_tries:
                        raise
                tries += 1

        return wrapper

    return decorator


import inspect


def checkarguments(func):
    def wrapper(*args, **kwargs):
        # Get the function signature and parameter names
        signature = inspect.signature(func)
        parameters = signature.parameters

        errors = []

        # Iterate over the positional booster
        for i, arg in enumerate(args):
            param_name = list(parameters.keys())[i]
            param_type = parameters[param_name].annotation
            if not isinstance(arg, param_type):  # objet passé n'est il pas du bon type
                msg = f">>>>Argument {param_name} doit etre de type {param_type.__name__}"
                errors.append(msg)

        # Iterate over the keyword booster
        for param_name, arg in kwargs.items():
            param_type = parameters[param_name].annotation
            if not isinstance(arg, param_type):
                msg = f">>>>Argument {param_name} doit etre de type {param_type.__name__}"
                errors.append(msg)

        # Call the original function
        if len(errors):
            raise TypeError("\n".join(errors))

        return func(*args, **kwargs)

    return wrapper


def check_arguments(func):
    def wrap_func(*args, **kwargs):
        sig = inspect.signature(func)
        bound_args = sig.bind(*args, **kwargs)

        for name, value in bound_args.arguments.items():
            param_type = sig.parameters[name].annotation
            if param_type != inspect.Parameter.empty and not isinstance(value, param_type):
                raise TypeError("Parameters are not ok")

        return func(*args, **kwargs)

    return wrap_func


def verifier_types(func):
    def wrap(*args, **kwargs):
        parametres = inspect.signature(func).parameters

        erreurs = []
        for nom_arg, valeur_arg in zip(parametres.values(), args):
            if nom_arg.name in func.__annotations__ and not isinstance(valeur_arg, func.__annotations__[nom_arg.name]):
                erreurs.append((nom_arg.name, func.__annotations__[nom_arg.name], type(valeur_arg)))

        if erreurs:
            raise TypeError("\n".join(
                [f"Erreur de type pour l'argument '{nom}'. Attendu {attendu}, obtenu {obtenu}." for nom, attendu, obtenu
                 in erreurs]))

        resultat = func(*args, **kwargs)
        return resultat

    return wrap


def user_is_logged_in():
    # apres verif
    return False


def login_required(func):
    def wrapper(*args, **kwargs):
        if user_is_logged_in():
            return func(*args, **kwargs)
        else:
            raise PermissionError("Login required")

    return wrapper


# https://pypi.org/project/logdecorator/

from functools import wraps




import inspect

def check_types(func):
    sig = inspect.signature(func)
    annotations = func.__annotations__

    def wrapper(*args, **kwargs):
        bound = sig.bind(*args, **kwargs)
        bound.apply_defaults()

        for name, value in bound.arguments.items():
            expected_type = annotations.get(name)
            if expected_type and not isinstance(value, expected_type):
                raise TypeError(f"{name} n'est pas du bon type")

        return func(*args, **kwargs)

    return wrapper

#logging.basicConfig(filename="global.log")
def debuglogger(func):
    logger = logging.getLogger("debuglogger")
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler("debuglogger.log",encoding="utf-8")
    stream_handler = logging.StreamHandler()
    # Définir un format
    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    stream_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    @wraps(func)  # sans cela : on perd de la metainfo
    def wrapper(*args, **kwargs):
        logger.debug(f"Appel de {func.__name__} avec {args} {kwargs}")
        result = func(*args, **kwargs)
        logger.debug(f"{func.__name__} a retourné {result}")
        return result
    return wrapper

