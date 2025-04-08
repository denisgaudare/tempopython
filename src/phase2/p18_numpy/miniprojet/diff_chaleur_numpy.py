import numpy as np
import time
import matplotlib.pyplot as plt

# Paramètres
N = 100
iterations = 1000

# Grille initiale (NumPy)
T = np.zeros((N, N))
T[N//2 - 5:N//2 + 5, N//2 - 5:N//2 + 5] = 100.0

start = time.time()

# Diffusion (NumPy)
for _ in range(iterations):
    T[1:-1, 1:-1] = 0.25 * (
            T[2:, 1:-1] + T[:-2, 1:-1] + T[1:-1, 2:] + T[1:-1, :-2]
    )

end = time.time()
print(f"⚡ NumPy : {end - start:.3f} s")

# Affichage
plt.imshow(T, cmap="hot", interpolation="nearest")
plt.title("NumPy")
plt.colorbar()
plt.show()
