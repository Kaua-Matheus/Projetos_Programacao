primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
          53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]


"""def primos_mersenne(max):
    for c in range(max):
        print(pow(2, primos[c]) - 1)


def checa():
    for c in range(2, 2026):
        if 2047 % c == 0:
            print(2047 / c, c)
            print(2047 % c)
            break

"""
# primos_mersenne(20)


def primos_mersenne(max):
    for c in range(max):
        valor = checa(pow(2, primos[c]) - 1)
        print(valor)


def checa(valor):
    for c in range(2, valor - 1):
        if valor % c == 0:
            return 0



primos_mersenne(20)
