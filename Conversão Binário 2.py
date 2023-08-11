D = eval(input("Forneça número decimal N \n"))

Q = 1
lista = []

print(f"Número na base decimal: {D}")

while Q >= 1:
    R = D%2
    lista.insert(0, R)
    Q = D // 2
    D = Q

B = ''.join([str(item) for item in lista])

print(f"Conversão para a base binária: {B}")



