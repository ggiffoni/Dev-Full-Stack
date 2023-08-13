#Exemplo de módulo - Colunas e Linhas 3x3

print("Módulo importado com sucesso.")

def primeira_coluna_3x3(matriz_A, matriz_B):
    m11 = matriz_A[0][0] * matriz_B[0][0] + matriz_A[0][1] * matriz_B[1][0] + matriz_A[0][2] * matriz_B[2][0]
    m21 = matriz_A[1][0] * matriz_B[0][0] + matriz_A[1][1] * matriz_B[1][0] + matriz_A[1][2] * matriz_B[2][0]
    m31 = matriz_A[2][0] * matriz_B[0][0] + matriz_A[2][1] * matriz_B[1][0] + matriz_A[2][2] * matriz_B[2][0]
    primeira = [[m11], [m21], [m31]]
    return primeira

def segunda_coluna_3x3(matriz_A, matriz_B):
    m12 = matriz_A[0][0] * matriz_B[0][1] + matriz_A[0][1] * matriz_B[1][1] + matriz_A[0][2] * matriz_B[2][1]
    m22 = matriz_A[1][0] * matriz_B[0][1] + matriz_A[1][1] * matriz_B[1][1] + matriz_A[1][2] * matriz_B[2][1]
    m32 = matriz_A[2][0] * matriz_B[0][1] + matriz_A[2][1] * matriz_B[1][1] + matriz_A[2][2] * matriz_B[2][1]
    segunda = [[m12], [m22], [m32]]
    return segunda

def terceira_coluna_3x3(matriz_A, matriz_B):
    m13 = matriz_A[0][0] * matriz_B[0][2] + matriz_A[0][1] * matriz_B[1][2] + matriz_A[0][2] * matriz_B[2][2]
    m23 = matriz_A[1][0] * matriz_B[0][2] + matriz_A[1][1] * matriz_B[1][2] + matriz_A[1][2] * matriz_B[2][2]
    m33 = matriz_A[2][0] * matriz_B[0][2] + matriz_A[2][1] * matriz_B[1][2] + matriz_A[2][2] * matriz_B[2][2]
    terceira = [[m13], [m23], [m33]]
    return terceira

def primeira_linha_3x3(matriz_A, matriz_B):
    m11 = matriz_A[0][0] * matriz_B[0][0] + matriz_A[0][1] * matriz_B[1][0] + matriz_A[0][2] * matriz_B[2][0]
    m12 = matriz_A[0][0] * matriz_B[0][1] + matriz_A[0][1] * matriz_B[1][1] + matriz_A[0][2] * matriz_B[2][1]
    m13 = matriz_A[0][0] * matriz_B[0][2] + matriz_A[0][1] * matriz_B[1][2] + matriz_A[0][2] * matriz_B[2][2]
    primeira = [[m11], [m12], [m13]]
    return primeira

def segunda_linha_3x3(matriz_A, matriz_B):
    m21 = matriz_A[1][0] * matriz_B[0][0] + matriz_A[1][1] * matriz_B[1][0] + matriz_A[1][2] * matriz_B[2][0]
    m22 = matriz_A[1][0] * matriz_B[0][1] + matriz_A[1][1] * matriz_B[1][1] + matriz_A[1][2] * matriz_B[2][1]
    m23 = matriz_A[1][0] * matriz_B[0][2] + matriz_A[1][1] * matriz_B[1][2] + matriz_A[1][2] * matriz_B[2][2]
    segunda = [[m21], [m22], [m23]]
    return segunda

def terceira_linha_3x3(matriz_A, matriz_B):
    m31 = matriz_A[2][0] * matriz_B[0][0] + matriz_A[2][1] * matriz_B[1][0] + matriz_A[2][2] * matriz_B[2][0]
    m32 = matriz_A[2][0] * matriz_B[0][1] + matriz_A[2][1] * matriz_B[1][1] + matriz_A[2][2] * matriz_B[2][1]
    m33 = matriz_A[2][0] * matriz_B[0][2] + matriz_A[2][1] * matriz_B[1][2] + matriz_A[2][2] * matriz_B[2][2]
    terceira = [[m31], [m32], [m33]]
    return terceira


