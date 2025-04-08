import time
import matplotlib.pyplot as plt

# Paramètres
N = 100
iterations = 1000

# Grille initiale (liste de listes)
T = [[0.0 for _ in range(N)] for _ in range(N)]

# Chauffer le centre
for i in range(N//2 - 5, N//2 + 5):
    for j in range(N//2 - 5, N//2 + 5):
        T[i][j] = 100.0

# Fonction de copie de grille
def copy_grid(grid):
    return [row[:] for row in grid]

start = time.time()

# Diffusion (Python pur)
for _ in range(iterations):
    T_new = copy_grid(T)
    for i in range(1, N-1):
        for j in range(1, N-1):
            T_new[i][j] = 0.25 * (T[i+1][j] + T[i-1][j] + T[i][j+1] + T[i][j-1])
    T = T_new

end = time.time()
print(f"⏱ Python pur : {end - start:.3f} s")

# Affichage
plt.imshow(T, cmap="hot", interpolation="nearest")
plt.title("Python pur")
plt.colorbar()
plt.show()
