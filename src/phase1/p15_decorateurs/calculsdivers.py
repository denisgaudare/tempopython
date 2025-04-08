import time
from typing import Optional

from phase1.p15_decorateurs.decorators import chrono, memoize


def limiteur(func): #construit
    def wrapper(*val1, **val2):
        res = func(*val1, **val2) # n'importe quoi est possible
        if res<0:
            res = 0
        return res

    return wrapper


def startstop(func): #construit
    def wrapper(*val1, **val2):
        print("START")
        func(*val1, **val2) # n'importe quoi est possible
        print("END")

    return wrapper

@startstop
def foo():
    time.sleep(1)


def change_temperature(a, b):
    return a+b


@startstop
def multi(*val):
    print(val)

# -------------
multi(1,2,3,4,5,8)
foo()


print(change_temperature(5, 5))
print(change_temperature(4, -5))

# ESPIONNAGE : chrono, log, affichage
# MODIFIE LE RESULTAT, EMPECHE EXECUTION
# VERIFIE LES PARAMS PASSES EN ARGUMENTS
# DETOURNER VERS UNE AUTRE SORTIE
# TRY/EXCEPT, LIMITE LES DEGATS


@memoize
def fibo(n):
    if n<2:
        return n
    return fibo(n-1) + fibo(n-2)

print(fibo(120))

@typechecker
def averifi(a:Optional[int,float], b:str):
    pass