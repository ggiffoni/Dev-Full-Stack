#Calcula o maior número entre dois números.

n1 = eval(input("Entre com o primeiro número: "))
n2 = eval(input("Entre com o segundo número: "))

if n1 > n2:
    print("O número {} é maior do que o número {}".format(n1, n2))

elif n1 == n2:
    print("O número {} é igual ao número {}".format(n1, n2))

else:
    print("O número {} é maior do que o número {}".format(n2, n1))



