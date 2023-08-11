#Calcula o fatorial de um número

def Fatorial(n):
    r = 1

    for x in range(1, n+1):
        r = r*x
    return r

p = eval(input("Entre com um número inteiro n: "))

print("O fatorial de n é: [{}]".format(Fatorial(p)))





