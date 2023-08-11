from numpy import array

matriz_A = eval(input("Entre com a sua matriz A:"))
matriz_B = eval(input("Entre com a sua matriz B:"))

#Primeira coluna:

m11 = matriz_A[0][0] * matriz_B[0][0] + matriz_A[0][1] * matriz_B[1][0] + matriz_A[0][2] * matriz_B[2][0]
m21 = matriz_A[1][0] * matriz_B[0][0] + matriz_A[1][1] * matriz_B[1][0] + matriz_A[1][2] * matriz_B[2][0]
m31 = matriz_A[2][0] * matriz_B[0][0] + matriz_A[2][1] * matriz_B[1][0] + matriz_A[2][2] * matriz_B[2][0]

#Segunda coluna:

m12 = matriz_A[0][0] * matriz_B[0][1] + matriz_A[0][1] * matriz_B[1][1] + matriz_A[0][2] * matriz_B[2][1]
m22 = matriz_A[1][0] * matriz_B[0][1] + matriz_A[1][1] * matriz_B[1][1] + matriz_A[1][2] * matriz_B[2][1]
m32 = matriz_A[2][0] * matriz_B[0][1] + matriz_A[2][1] * matriz_B[1][1] + matriz_A[2][2] * matriz_B[2][1]

#Terceira coluna:

m13 = matriz_A[0][0] * matriz_B[0][2] + matriz_A[0][1] * matriz_B[1][2] + matriz_A[0][2] * matriz_B[2][2]
m23 = matriz_A[1][0] * matriz_B[0][2] + matriz_A[1][1] * matriz_B[1][2] + matriz_A[1][2] * matriz_B[2][2]
m33 = matriz_A[2][0] * matriz_B[0][2] + matriz_A[2][1] * matriz_B[1][2] + matriz_A[2][2] * matriz_B[2][2]


matriz_AB = array([[m11, m12, m13], [m21, m22, m23], [m31, m32, m33]], dtype=int)

print(matriz_AB)
