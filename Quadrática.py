#Calcula as raízes de uma equação de segundo grau na forma ax^2 + bx + c = 0.

a = eval(input("Entre com o coeficiente 'a'\n"))
b = eval(input("Entre com o coeficiente 'b'\n"))
c = eval(input("Entre com o coeficiente 'c'\n"))

def quad():
    delta = b**2 - 4 * a * c
    if delta < 0:
        return "Não há raízes reais."
    else:
        x1 = (-b + delta**0.5) / (2 * a)
        x2 = (-b - delta ** 0.5) / (2 * a)
        print(f"As raízes são {x1:3.3} e {x2:3.3}")

print(quad())

