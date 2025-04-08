# Recharger les bibliothèques après reset de l'environnement
import nbformat as nbf

notebook = nbf.v4.new_notebook()
cells = []

# Cellule 1 - Titre
cells.append(nbf.v4.new_markdown_cell("# 🧠 Introduction à NumPy pour développeurs aguerris"))

# Cellule 2 - Benchmark
cells.append(nbf.v4.new_code_cell("""
import numpy as np
import time

lst = list(range(10_000_000))
arr = np.arange(10_000_000)

start = time.time(); [x**2 for x in lst]; print("List:", time.time() - start)
start = time.time(); arr ** 2; print("NumPy:", time.time() - start)
"""))

# Cellule 3 - Création et inspection
cells.append(nbf.v4.new_code_cell("""
a = np.zeros((2, 3))
b = np.random.randint(0, 10, size=(3, 3))

print("a =\\n", a)
print("b =\\n", b)
print("Shape de b :", b.shape)
print("Dtype de b :", b.dtype)
print("Dimensions :", b.ndim)
print("Taille totale :", b.size)
"""))

# Cellule 4 - Indexation et slicing
cells.append(nbf.v4.new_code_cell("""
a = np.arange(10)
print("Original :", a)

print("Slicing :", a[2:7])
print("Masquage :", a[a % 2 == 0])

a[a % 2 == 0] = -1
print("Modifié :", a)
"""))

# Cellule 5 - Opérations vectorisées & broadcasting
cells.append(nbf.v4.new_code_cell("""
a = np.arange(3).reshape(3, 1)
b = np.arange(4).reshape(1, 4)
print("a + b =\\n", a + b)
"""))

# Cellule 6 - Statistiques
cells.append(nbf.v4.new_code_cell("""
data = np.random.rand(5, 10)
print("Moyenne globale :", data.mean())
print("Moyenne par ligne :", data.mean(axis=1))
print("Écart-type par colonne :", data.std(axis=0))
"""))

# Cellule 7 - Reshape & manipulation
cells.append(nbf.v4.new_code_cell("""
a = np.array([[1, 2], [3, 4]])
print("Original :\\n", a)
print("Repeat ligne :\\n", np.repeat(a, 2, axis=0))
print("Flatten :", a.flatten())
"""))

# Cellule 8 - Simulation vectorisée
cells.append(nbf.v4.new_code_cell("""
np.random.seed(0)
rolls = np.random.randint(1, 7, size=(1000, 10))
sums = rolls.sum(axis=1)

import matplotlib.pyplot as plt
plt.hist(sums, bins=range(10, 61), edgecolor="black")
plt.title("Distribution de sommes de 10 dés (1000 essais)")
plt.xlabel("Somme")
plt.ylabel("Fréquence")
plt.show()
"""))

# Cellule 9 - Produit matriciel (ML)
cells.append(nbf.v4.new_code_cell("""
X = np.random.rand(100, 3)
w = np.array([0.1, 0.5, -0.2])
y_pred = X @ w
print("Prédictions :", y_pred[:5])
"""))

# Création du notebook
notebook['cells'] = cells
notebook_path = "/mnt/data/030-pandas.ipynb"

with open(notebook_path, 'w') as f:
    nbf.write(notebook, f)

notebook_path
