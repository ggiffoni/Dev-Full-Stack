#Exemplo com try, while e finally.

try:
    a = eval(input("Entre com o numerador: "))
    b = eval(input("Entre com o denominador: "))
    while b == 0:
        print("O denominador não pode ser zero!")
        b = eval(input("Entre com o denominador: "))
finally:
    print(a / b)






