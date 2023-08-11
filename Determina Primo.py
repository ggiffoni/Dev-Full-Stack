# Determina se um número é primo.

n = eval(input("Entre com um número inteiro: "))

def primo(n):
    "Determina se o número fornecido é ou não primo."
    if n < 2:
        return False
    i = n // 2
    while (i > 1):
        if (n % i == 0):
            return False
        i = i - 1
    return True

def resprimo():
    if primo(n) == True:
        return "O número é primo"
    else:
        return "O número não é primo"

print(help(primo))
print(resprimo())









