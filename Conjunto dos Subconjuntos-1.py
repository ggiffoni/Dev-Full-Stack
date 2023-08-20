#Imprime o conjunto dos subconjuntos de um conjunto digitado pelo usuário.

def subconjuntos(numeros):
    return subconjuntos_recursivo([], numeros)

def subconjuntos_recursivo(atual, conjunto):
    if conjunto:
        return subconjuntos_recursivo(atual, conjunto[1:]) + subconjuntos_recursivo(atual + [conjunto[0]], conjunto[1:])
    return [atual]

numeros = [1, 2, 3, 4]
resultado = subconjuntos(numeros)

print(resultado)