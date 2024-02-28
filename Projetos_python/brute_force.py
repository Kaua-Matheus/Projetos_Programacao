senha = '12345'

def testador(senha, dig=len(senha)):

    return (dig * '1' + '2')


print(testador(senha))
