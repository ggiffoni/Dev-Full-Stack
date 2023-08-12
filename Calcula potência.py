# Potenciação - funções dentro de funções

def calcula_potencia(base):
    def potencia(expoente):
        return base ** expoente

    return potencia

# parte principal do programa
def main():
    base_expoente = input()
    # separa base e expoente, convertendo-os para inteiros
    expoente, base = (int(i) for i in base_expoente.split())

    # utilizando a função calcula_potencia
    potencia_de = calcula_potencia(base)
    res_potencia = potencia_de(expoente)
    print(f"{base} elevado a {expoente} = {res_potencia}")

if __name__ == "__main__":
    main()