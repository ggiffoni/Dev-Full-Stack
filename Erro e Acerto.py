
try:
    x = int(input("Digite um númerro inteiro par: "))

    while x % 2 != 0:
        x = int(input("Digite um númerro inteiro par: "))
except ValueError:
    print("O número digitado não é inteiro")






