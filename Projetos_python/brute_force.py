import string, random, time, sys

alfabet = string.printable[:94]
charlength = 3

def pass_generator(tamanho, alfabeto = alfabet):
    senha = ''
    while len(senha) < tamanho:
        senha += random.choice(alfabeto)
    return senha

# Primeiros PassBreakers criados

def testador_v1(senha = '123441'):
    """

    :param senha: A senha é valor teste a ser descoberto
    :return:  O retorno é a senha caso encontrada
    """
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


a = '*$&-'
b = 'abcde'

def product(L, L2, QD=1, C=1):
    lista = []
    """
    :param L: Esse parametro é a lista da qual iremos fazer as combinações
    :param QD: Esse é o limite de combinações
    :param C: Esse valor é o controle e deve sempre ser igual a 1
    :return: Retorna uma lista com os testes

    Precisa de melhorias na saída return, de modo a podermos testar cada diferente combinação,
    sem a dobra de valor.
    """
    while True:
        for X in L:
            for Y in L2:
                lista.append(X + Y)
                #time.sleep(0.5)
                if lista[-1] == senha:
                    print(senha)
                    print(lista[-1])
                    sys.exit()
        if C < QD:
            C += 1
            lista = product(lista, b, QD, C)
        return lista


valor = 7
senha = pass_generator(valor, b)
product(b,b, QD=valor-1)

def tool(lista_1, lista_2, convert=False):
    senha = pass_generator(2, lista_1)
    """
    :param convert: É o conversor que irá transformar os caracteres em string
    :param lista_1: Conjunto de valores A dos quais serão combinados com B
    :param lista_2: Conjunto de valores B dos quais serão combinados com A
    :return: Retorna uma lista com todas as possíveis combinações entre o conjunto A e B
    """

    try:
        if convert:
            lista_2, lista_1 = str(lista_2), str(lista_1)
        else:
            valores = []
            possibilidades = len(lista_1) * len(lista_2)

            for v1 in lista_1:
                for v2 in lista_2:
                    valores.append(v1 + v2)
                    if checagem_pass(senha, valores[-1]):
                        return f"A senha é {senha}, e foi achado {valores[-1]}"

            # print(f"A quantidade de possibilidades é {possibilidades};")

            return valores
    except SyntaxError:
        print(SyntaxError, f"Não foi possível utilizar os valores por erros de syntax")
        return None
def checagem_pass(senha, valor):
    if senha == valor:
        return True

# print(tool(alfabet, alfabet))


def breaker():
    """

    :return: Retorna a senha, ou falha, entregando erro de memoria ou não achando a senha
    """

    senha = pass_generator(8, alfabet)
    lista = [x for x in alfabet]
    final = tool(tool(tool(lista, lista), tool(lista, lista)), tool(tool(lista, lista), tool(lista, lista)))
    # final = tool(tool(lista, lista), tool(lista, lista))
    for valor in final:
        if valor == senha:
            print(f"Quebramos a senha {senha} e achamos {valor}")
            return valor
    print("Não foi possível quebrar a senha! ")
    print(f"A senha era {senha}")
    return None
