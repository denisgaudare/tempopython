# Recharger les bibliothèques après reset de l'environnement

# 01 Introduction à NumPy pour développeurs ++
import numpy as np
import time

matrix = np.array([[1, 2, 3], [4, 5, 6]])

# Moyenne de chaque ligne
means = np.apply_along_axis(np.mean, axis=1, arr=matrix)
print(means)  # [2. 5.]

from commontools.consoles import pause

# 02 - Benchmark

start = time.time()
lst = list(range(10_000_000))
[x**2 for x in lst]
print("List:", time.time() - start)

pause()

start = time.time()
arr = np.arange(10_000_000,dtype=np.uint32)
arr ** 2
print("NumPy:", time.time() - start)

pause()

# Création de deux matrices 1000x1000
start = time.time()
A = np.random.rand(10000, 10000)
B = np.random.rand(10000, 10000)
# Multiplication des matrices
C = np.dot(A, B)
print("NumPy:", time.time() - start)

pause()

# 03 - Création et inspection
a = np.zeros((2, 3))
b = np.random.randint(0, 10, size=(3, 3))

print("a =\\n", a)
print("b =\\n", b)
print("Shape de b :", b.shape)
print("Dtype de b :", b.dtype)
print("Dimensions :", b.ndim)
print("Taille totale :", b.size)

# 04 - Indexation et slicing
a = np.arange(10)
print("Original :", a)

print("Slicing :", a[2:7])
print("Masquage :", a[a % 2 == 0])

a[a % 2 == 0] = -1
print("Modifié :", a)

# 05 - Opérations vectorisées & broadcasting
a = np.arange(3).reshape(3, 1)
b = np.arange(4).reshape(1, 4)
print("a + b =\\n", a + b)

# 06 - Statistiques
data = np.random.rand(5, 10)
print("Moyenne globale :", data.mean())
print("Moyenne par ligne :", data.mean(axis=1))
print("Écart-type par colonne :", data.std(axis=0))

# 07 - Reshape & manipulation
a = np.array([[1, 2], [3, 4]])
print("Original :\\n", a)
print("Repeat ligne :\\n", np.repeat(a, 2, axis=0))
print("Flatten :", a.flatten())

# 08 - Simulation vectorisée
np.random.seed(0)
rolls = np.random.randint(1, 7, size=(1000, 10))
sums = rolls.sum(axis=1)

import matplotlib.pyplot as plt

plt.hist(sums, bins=range(10, 61), edgecolor="black")
plt.title("Distribution de sommes de 10 dés (1000 essais)")
plt.xlabel("Somme")
plt.ylabel("Fréquence")
plt.savefig("histo.png")

# 09 - Produit matriciel (ML)
X = np.random.rand(100, 3)
w = np.array([0.1, 0.5, -0.2])
y_pred = X @ w
print("Prédictions :", y_pred[:5])