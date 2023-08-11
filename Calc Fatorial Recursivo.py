#Fatorial recursivo.

def fat_recursivo(n):
    if ((n == 0) or (n == 1)):
        return 1
    return n*fat_recursivo(n-1)

p = eval(input("Digite número inteiro n: "))

print("O fatorial de n é: [{}]".format(fat_recursivo(p)))









