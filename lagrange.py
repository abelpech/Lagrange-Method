# Software Engineer: Abel Pech
# Teacher: Sergio Chimal
# Class: Simulation
# Subject: Lagrange Method Implementation

import numpy as np
from pypoly import Polynomial
import matplotlib.pyplot as mp
from pypoly import X


X = [[0, 1], [0.5, 0.8776]]

# X = [[1, -2], [3, 1], [5, 2]]

# Ejemplos https://numat.net/ejerc/interp/

# X = [[7,30], [-6,-22]]

# X = [[1,10],[-4,10],[-7,34]]

# X = [[-5,-2], [-7,-2], [4,-2], [5,9]]


grado = len(X) 
print("Grado de la Ecuacion:", grado -1 )
ecuaciones = np.array([[point[0] ** i for i in range(grado)] for point in X])
#print("Ecuaciones: ", ecuaciones)
valores = np.array([point[1] for point in X])
#print("Valores: ", values)
coeficientes = np.linalg.solve(ecuaciones, valores)
#print ("Coeficientes Ecuacion: ", list(coeficientes))
ecuacion = Polynomial(*coeficientes)
print ("Ecuacion Polinomial: ", ecuacion)

# def graph(formula, x_range):  
#     x = np.array(x_range)  
#     y = eval(formula)
#     mp.plot(x, y)  
#     mp.show()

# graph('1 - 0.2448 * x', range(-10, 10))
