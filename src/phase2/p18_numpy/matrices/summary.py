import numpy as np

def generate_matrix(n, m):
    return np.random.randint(0, 100, size=(n, m))

# Exemple d'utilisation
matrix = generate_matrix(5, 5) # carrée pour EIG
print(f"Matrice {matrix.shape}générée :\n", matrix)

def transpose_matrix(matrix):
    return matrix.T

transposed_matrix = transpose_matrix(matrix)
print("Matrice transposée :\n", transposed_matrix)

def multiply_matrices(matrix1, matrix2):
    return np.dot(matrix1, matrix2)
    #  matmul ou @ pour multi matricielle (__matmul__)

# Exemple d'utilisation
multiplied_matrix = multiply_matrices(matrix, transposed_matrix)
print("Matrice multipliée :\n", multiplied_matrix)

def matrix_statistics(matrix):
    mean = np.mean(matrix)
    std_dev = np.std(matrix)
    variance = np.var(matrix)
    return mean, std_dev, variance

# Exemple d'utilisation
mean, std_dev, variance = matrix_statistics(matrix)
print(f"Moyenne : {mean}, Écart-type : {std_dev}, Variance : {variance}")

#### 5. **Fonctions avancées (pour développeurs expérimentés)**

##### a. **Décomposition en valeurs singulières (SVD)**
def svd_decomposition(matrix):
    U, S, Vt = np.linalg.svd(matrix)
    return U, S, Vt

# Exemple d'utilisation
U, S, Vt = svd_decomposition(matrix)
print(f"U  aka matrice orthogonale :\n{U}")
print(f"S  aka vals singulieres :\n{S}\nVt :\n{Vt}")
print(f"Vt aka transposee ortho:\n{Vt}")

##### b. **Calcul des valeurs propres et vecteurs propres**

def eigen_decomposition(matrix):
    values, vectors = np.linalg.eig(matrix)
    return values, vectors

# Exemple d'utilisation
values, vectors = eigen_decomposition(matrix)
print(f"Valeurs propres : {values}\nVecteurs propres :\n{vectors}")

### **Bonus : Visualisation**

import matplotlib.pyplot as plt

def visualize_matrix(matrix):
    plt.imshow(matrix, cmap='viridis', interpolation='none')
    plt.colorbar()
    plt.show()

# Exemple d'utilisation
visualize_matrix(matrix)
