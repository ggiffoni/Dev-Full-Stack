#Calcula o menor elemento de uma lista.

lista = eval(input("Digite uma lista de números.\n"))

def menor_lista(lista):
    minimo = lista[0]
    for elemento in lista:
        if elemento < minimo:
            minimo = elemento
    return minimo

print ("O menor elemento da lista é: {}".format(menor_lista(lista)))






