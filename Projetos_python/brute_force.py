import string, random

alfabet = string.printable[:95]
charlength = 3

def pass_generator(tamanho, alfabeto = alfabet):
    senha = ''
    while len(senha) < tamanho:
        senha += random.choice(alfabeto)
    return senha

def testador_v1(senha = '123441'):
    quant_digMn = len(str(senha))
    val = '0' * quant_digMn
    while True:
        for c in range(quant_digMn):
            val = str(int(val) + 1)
            print(val)
            if val == str(senha):
                return print(val)
            elif len((val)) > quant_digMn:
                return None
            else:
                continue

# def testador_v2(senha, alfabeto=alfabet):


"""random_pass = pass_generator(charlength)
print(random_pass)"""

"""valores = 'abcd'
lista = [x for x in valores]
print(lista)"""


