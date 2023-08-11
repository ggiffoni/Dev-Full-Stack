#Soma os números pares de uma lista utilizando uma função.

list = eval(input("Digite uma lista de números inteiros: "))

def Par(n):
    if n%2 == 0:
        return n

def soma_par (list):
    soma = 0
    for num in list:
        if Par(num):
            soma = soma + num
    return soma

print("Soma dos números pares da lista: [{}]".format(soma_par(list)))




