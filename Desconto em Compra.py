N = eval(input("Quantas unidades o cliente está comprando?\n"))

Pu = 10

if N <= 10:
    Total = Pu * N

elif N <= 20:
    Total = (Pu * N) * (1 - 0.1)
else:
    Total = (Pu * N) * (1 - 0.2)

print(f"Total a ser pago: {Total}")

