#Exemplo com while, try, break, except e ValueError.

while True:
    try:
        x = int(input("Digite um número: "))
        break
    except ValueError:
        print("Entre com um número válido.")



