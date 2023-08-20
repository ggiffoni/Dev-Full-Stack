# Calcula o conjunto dos subconjuntos de determinado conjunto fornecido pelo usuário.

# ENTRADA DE DADOS:

lista = eval(input("Entre com uma lista de números: "))


# CÁLCULOS INTERMEDIÁRIOS:

def subconjuntos(numeros):
    resultado = [[]]

    for numero in numeros:
        resultado += [i + [numero] for i in resultado]
    return resultado

# APRESENTAÇÃO DOS RESULTADOS:

conjunto = subconjuntos(lista)

print(conjunto)






