def mult_matizes(A, B):
    nLinhasA = len(A)
    nColunasA = len(A[0])
    nColunasB = len(B[0])

    M = []

    for linha in range(nLinhasA):
        M.append([])
        for coluna in range(nColunasB):
            M[linha].append(0)
            for k in range(nColunasA):
                M[linha][coluna] += A[linha][k]*B[k][coluna]
    return M


A = [[2, 4, 3], [2, 2, 1], [2, 3, 1]]
B = [[1, 2, 4], [2, 2, 1], [2, 3, 1]]


print(mult_matizes(A, B))