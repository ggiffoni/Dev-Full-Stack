
def subconjuntos(numeros):
    resultado = [[]]

    for numero in numeros:
        resultado += [i + [numero] for i in resultado]
    return resultado

lista = eval(input("Entre com uma lista de números: "))

conjunto = subconjuntos(lista)

print(conjunto)






