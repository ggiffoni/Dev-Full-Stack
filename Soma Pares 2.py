#Soma os números pares de uma lista utilizando estratégia de comprimento e range da lista.

lista = eval(input("Digite uma lista de números inteiros.\n"))

n = len(lista)
soma = 0

for i in range(n):
    if lista[i] % 2 == 0:
        soma = soma + lista[i]

print(f"A soma dos elementos pares da lista é {soma}")

