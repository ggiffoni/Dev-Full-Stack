#Multiplicação de Matrizes 3x3 com módulo.


import Linhas_Colunas_3x3

matriz_A = eval(input("Entre com a sua matriz A:"))
matriz_B = eval(input("Entre com a sua matriz B:"))

linha1 = Linhas_Colunas_3x3.primeira_linha_3x3(matriz_A, matriz_B)
linha2 = Linhas_Colunas_3x3.segunda_linha_3x3(matriz_A, matriz_B)
linha3 = Linhas_Colunas_3x3.terceira_linha_3x3(matriz_A, matriz_B)

print([[linha1], [linha2], [linha3]])


