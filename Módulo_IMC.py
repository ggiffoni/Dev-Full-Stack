#Módulo para cálculo do IMC.

def calcula_imc(peso, altura):
    print("Digite seu peso:", peso)
    print("Digite sua altura", altura)
    imc = float(peso)/float(altura)**2
    return imc

def classifica_imc(índice):
    if índice < 18.5:
        return "Baixo peso."
    elif índice < 25:
        return "Peso adequado."
    elif índice < 30:
        return "Sobrepeso."
    else:
        return "Obeso."

