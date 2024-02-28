primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
          53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]


def crivo(max):
    lista_primos = []
    lista_naoprimos = []
    primo = False
    for numero in range(2, max + 1):
        for valor in primos:
            if pow(valor, 2) <= numero:
                if numero % valor == 0:
                    primo = False
                    lista_naoprimos.append(numero)
                    break
                else:
                    primo = True
                    pass
            else:
                lista_primos.append(numero)
                primo = False
                break
        if primo:
            lista_primos.append(numero)
        primo = False

    # print(lista_naoprimos)
    # print(lista_primos)
    return lista_primos


def printa(max):
    lista = ''
    lista_primos = crivo(max)
    for c in range(1, max + 1):
        if c == 1:
            lista += f"{'':<6}"
        if c % 10 == 0:
            lista += "\n"
        if c in lista_primos:
            lista += f'\033[31m{str(c):<5}\033[m'
        else:
            lista += f"{str(c):<5}"

    print(lista)


def primos_(max):
    lista = ''
    lista_primos = crivo(max)
    for key, valor in enumerate(lista_primos):
        if key + 1 == 1:
            lista += f"{'':<6}"
        if key % 10 == 0:
            lista += "\n"
        lista += f"\033[31m{valor:<6}\033[m"

    print(lista)


# crivo(100)
# printa(100)
primos_(100)
