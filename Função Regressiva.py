#Código com erro.

x = eval(input("Forneça número decimal inteiro x \n"))

def regressiva(x):

    if x <= 0:
        print("Acabou")
    else:
        regressiva(x-1)
        print (f"A sequência é {regressiva(x)}")

print (f"A sequência é {regressiva(x)}")