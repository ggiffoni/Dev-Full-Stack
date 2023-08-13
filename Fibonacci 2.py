#Novo código para encontrar o enézimo número de Fibonacci.

def fibo2(n):
    if n < 2:
        return n
    else:
        return fibo2(n - 2) + fibo2(n - 1)


if __name__ == "__main__":
    print(fibo2(10))
    print(fibo2(20))
