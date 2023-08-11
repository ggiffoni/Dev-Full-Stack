#Exemplo Multiplicação de Matrizes.

from numpy import array

matriz_A = array([[2, 4, 3], [2, 2, 1], [2, 3, 1]], dtype=int)

matriz_B = array([[1], [2], [4]], dtype=int)

m11 = matriz_A[0][0] * matriz_B[0][0] + matriz_A[0][1] * matriz_B[1][0] + matriz_A[0][2] * matriz_B[2][0]

m21 = matriz_A[1][0] * matriz_B[0][0] + matriz_A[1][1] * matriz_B[1][0] + matriz_A[1][2] * matriz_B[2][0]

m31 = matriz_A[2][0] * matriz_B[0][0] + matriz_A[2][1] * matriz_B[1][0] + matriz_A[2][2] * matriz_B[2][0]

matriz_AB = array([[m11], [m21], [m31]], dtype=int)

print(matriz_AB)


