# Calcula o conjunto dos subconjuntos de determinado conjunto fornecido pelo usuário.

"""
Para cada novo elemento adicionado ao conjunto original, o conjunto dos subconjuntos cresce da seguinte forma:

[] -> conjunto dos subconjuntos: [[]]
=[[]]

[1] -> conjunto dos subconjuntos: [[], [1]]
= [[]] + [[1]]

[1, 2] -> conjunto dos subconjuntos: [[], [1], [2], [1, 2]]
= [[]] + [[1]] + {[[]] + [[2]]} + {[[2]] + [[1]]}
= [[]] + [[1]] + [[2]] + [[1, 2]]

[1, 2, 3] -> conjunto dos subconjuntos: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
= [[]] + [[1]] + [[2]] + [[1, 2]] + {[[3]] + [[]]} + {[[3]] + [[1]]} + {[[3]] + [[2]]} + {[[3]] + [[1, 2]]}
= [[]] + [[1]] + [[2]] + [[1, 2]] + [[3]] + [[1, 3]] + [[2, 3]] + [[1, 2, 3]]

Ou seja, para cada novo elemento acrescentado, o novo subconjunto é igual ao anterior mais a soma do novo elemento com
cada um dos elementos do subconjunto anterior.

"""

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






