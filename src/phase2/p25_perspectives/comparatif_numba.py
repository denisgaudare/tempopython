import time
from pprint import pprint

from numba import jit

# Fonction Python pure
def compute_python(n):
    total = 0
    for i in range(n):
        total += i**0.5
    return total

# Fonction optimisée avec Numba
@jit(nopython=True)
def compute_numba(n):
    total = 0
    for i in range(n):
        total += i**0.5
    return total

# Paramètre de test
n = 50_000_000

# Mesure du temps pour la version Python native
start_python = time.time()
result_python = compute_python(n)
end_python = time.time()
time_python = end_python - start_python

# Mesure du temps pour la version Numba (avec warm-up)
compute_numba(10)  # warm-up JIT
start_numba = time.time()
result_numba = compute_numba(n)
end_numba = time.time()
time_numba = end_numba - start_numba

res = {
    "Résultat python": result_python,
    "Résultat numba":  result_numba,
    "Temps Python natif (s)": time_python,
    "Temps Numba (s)": time_numba,
    "Gain (x fois)" : time_python / time_numba
 }
pprint(res)
