from numba import njit
import numpy as np
import time

N = 100
iterations = 1000

@njit
def diffuse(T, iterations):
    for _ in range(iterations):
        T_new = T.copy()
        for i in range(1, N-1):
            for j in range(1, N-1):
                T_new[i, j] = 0.25 * (T[i+1, j] + T[i-1, j] + T[i, j+1] + T[i, j-1])
        T[:] = T_new
    return T

# Grille initiale
T = np.zeros((N, N))
T[N//2 - 5:N//2 + 5, N//2 - 5:N//2 + 5] = 100.0

start = time.time()
T = diffuse(T, iterations)
end = time.time()
print(f"🚀 Numba : {end - start:.3f} s")
