from pprint import pprint

import numpy as np

# Un tableau 3x3
arr1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Un vecteur de taille 3
arr2 = np.array([10, 20, 30])

# Broadcasting : addition du vecteur à chaque ligne de la matrice
result = arr1 + arr2
pprint(result)