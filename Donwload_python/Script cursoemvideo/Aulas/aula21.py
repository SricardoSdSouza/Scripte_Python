'''def contador(i, f, p):
    c = i
    while c <= f:
        print(f'{c}_',end='')
        c += p
    print('FIM!')

contador(0, 100, 10)'''
# Para fornecer o help da função criada usamos as doc strings, serve para outros
#programadores saberem o que a fução criada devolve, documentação do código.
'''def contador(i, f, p):
    """
      -> Faz uma contagem e mostra na tela.
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Esta função foi criada por @Ricardo 22/07/2020
    """
    c = i
    while c <= f:
        print(f'{c}_',end='')
        c += p
    print('FIM!')

contador(0, 100, 10)
help(contador)'''
'''def soma(a, b, c):
    s = a + b + c
    print(s)

soma(3, 2, 5)'''
# conceito de parâmetros opcionais
'''def soma(a, b, c=0):
    s = a + b + c
    print(s)

soma(3, 2, 5)
soma(3, 5)'''
# podemos colocar todos como parametros opcionais
'''def soma(a=0, b=0, c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o Segundo valor
    :param c: o terceiro valor
    :return: não retorna
    Função criada por @Ricardo em 22/07/2020
    """
    s = a + b + c
    print(s)

soma(3, 7, 5)
soma(3, 5)
soma(9,)
soma(b=4, a=6, c=8)
soma(a=6, c=8)
soma(a=6)'''
# declaração de variáveis globais e locais
'''def teste():
    x = 8
    print(f'Na função teste, n vale: {n}')
    print(f'Na função teste, n vale: {x}')

#programa principal
n = 2
print(f'No programa principal, n vale {n}')
# não se pode imprimir a variavel x por ser local
teste()'''
'''def teste(b):
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5
teste(a)
print(f'A fora vale {a}')'''
# se eu declarar dentro da função o a assume o valor de dentro da função
'''def teste(b):
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5
teste(a)
print(f'A fora vale {a}')'''
# passando o a interno para global
'''def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5
teste(a)
print(f'A fora vale {a}')'''
# retorno de variávei
'''def soma(a=0, b=0, c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o Segundo valor
    :param c: o terceiro valor
    :return: não retorna
    Função criada por @Ricardo em 22/07/2020
    """
    s = a + b + c
    return s

print(soma(3, 7, 5))
print(soma(3, 5))
print(soma(9))
print('**'*10)
r1 = soma(3, 7, 5)
r2 = soma(3, 5)
r3 = soma(9)
print(f'Os resultados foram {r1}, {r2}, {r3}')
# exercicio calculando fatoria
def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f
# programa principal
n = int(input('Digite um número: '))
print(f'O fatorial de {n}! é = {fatorial(n)}')
# podemos fazer assim
print('-%-'*20)
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'os resultados são {f1}, {f2} e {f3}')'''
print('-%-'*20)
def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

# Programa principal
num = int(input('Digite um número: '))
print(par(num))
if par(num):
    print('É par!')
else:
    print('Não é par!')