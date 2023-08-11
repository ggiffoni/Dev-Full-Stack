N = eval(input("Forneça número decimal N \n"))

print(f"Numero na base decimal: {N}")

print(f"Conversão para a base binária: {N%2}")

while N // 2 != 0:
    N = N // 2
    print(f"Conversão para a base binária: {N%2}")



