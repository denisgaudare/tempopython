# Projet Matrices 
### **Transformation et Analyse de Matrices avec NumPy**

**Objectif :**
1. Créer une matrice aléatoire.
2. Appliquer des transformations simples (transposition, multiplication).
3. Calculer des statistiques (moyenne, variance, etc.).
4. Implémenter des fonctions avancées pour des transformations plus complexes (par exemple, décomposition en valeurs singulières, recherche des valeurs propres).

### **Instructions :**

#### 1. **Création de la matrice aléatoire (Fonction simple)**
   - Créer une matrice aléatoire de dimensions (n, m) avec des entiers entre 0 et 100.
   - Utiliser `numpy.random.randint()` pour cela.
   
```python
import numpy as np

def generate_matrix(n, m):
    # TODO

# Exemple d'utilisation
matrix = generate_matrix(4, 5)
print("Matrice générée :\n", matrix)
```

#### 2. **Transposition de la matrice (Fonction simple)**
   - Implémenter une fonction pour transposer cette matrice.
   
```python
def transpose_matrix(matrix):
    return #TODO

# Exemple d'utilisation
transposed_matrix = transpose_matrix(matrix)
print("Matrice transposée :\n", transposed_matrix)
```

#### 3. **Multiplication des matrices (Fonction simple)**
   - Implémenter une fonction pour multiplier la matrice par elle-même (produit matriciel).
   
```python
def multiply_matrices(matrix1, matrix2):
    return #TODO

# Exemple d'utilisation
multiplied_matrix = multiply_matrices(matrix, transposed_matrix)
print("Matrice multipliée :\n", multiplied_matrix)
```

#### 4. **Statistiques sur la matrice (Fonction simple)**
   - Implémenter une fonction pour calculer les statistiques basiques de la matrice : moyenne, écart-type, variance, etc.
   - Utiliser les fonctions `np.mean()`, `np.std()`, `np.var()`.
   
```python
def matrix_statistics(matrix):
    # TODO
    return mean, std_dev, variance

# Exemple d'utilisation
mean, std_dev, variance = matrix_statistics(matrix)
print(f"Moyenne : {mean}, Écart-type : {std_dev}, Variance : {variance}")
```

#### 5. **Fonctions avancées (pour développeurs expérimentés)**

##### a. **Décomposition en valeurs singulières (SVD)**
   - Implémenter une fonction pour effectuer 
   - une décomposition en valeurs singulières sur la matrice.
   - Utiliser `np.linalg.???()`.
   - 
```python
def svd_decomposition(matrix):
    #TODO
    return U, S, Vt

# Exemple d'utilisation
U, S, Vt = svd_decomposition(matrix)
print(f"U :\n{U}\nS :\n{S}\nVt :\n{Vt}")
```

##### b. **Calcul des valeurs propres et vecteurs propres**
   - Implémenter une fonction pour calculer les valeurs propres et les vecteurs propres d'une matrice carrée.
   - Utiliser `np.linalg.???()`.

```python
def eigen_decomposition(matrix):
    # TODO
    return values, vectors

# Exemple d'utilisation
values, vectors = eigen_decomposition(matrix)
print(f"Valeurs propres : {values}\nVecteurs propres :\n{vectors}")
```

### **Bonus : Visualisation**
   - Ajouter une fonction pour visualiser les matrices à l'aide de `matplotlib`.
   - Afficher la matrice initiale, sa transposée, et la matrice multipliée.

```python
import matplotlib.pyplot as plt

def visualize_matrix(matrix):
    plt.imshow(matrix, cmap='viridis', interpolation='none')
    plt.colorbar()
    plt.show()

# Exemple d'utilisation
visualize_matrix(matrix)
```