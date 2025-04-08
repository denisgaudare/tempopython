import numpy as np
def check_prime(number):
    if number == 1:
        print(number, "is not a prime number")
    elif number > 1:
       # check for factors
       for i in range(2,number):
           if (number % i) == 0:
               print(number,"is not a prime number")
               print(i,"times",number//i,"is",number)
               break
       else:
           print(number,"is a prime number")

    # if the input number is less than or equal to 1, it is not prime
    else:
       print(number,"is not a prime number")

import numpy as np
def fibonacci_matrix(n):
    def matrix_power(matrix, power):
        return np.linalg.matrix_power(matrix, power)

    if n == 0:
        return 0
    matrix = np.array([[1, 1], [1, 0]])
    result = matrix_power(matrix, n - 1)
    return result[0][0]


# https://www.datacamp.com/fr/tutorial/fibonacci-sequence-python
