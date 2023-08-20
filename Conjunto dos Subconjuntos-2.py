
def subconjuntos(numeros):
    resultado = [[]]

    for numero in numeros:
        resultado += [i + [numero] for i in resultado]
    return resultado

lista = [1, 2, 3]

conjunto = subconjuntos(lista)

print(conjunto)






