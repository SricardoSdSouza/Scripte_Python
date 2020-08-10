'''Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:
inicio, fim e passo e realize a contagem. Seu programa tem que realizar três contagens através da função criada:
- a) De 1 até 10, de 1 em 1
- b) De 10 até 0, de 2 em 2
- c) uma contagem personalizada'''
from time import sleep
def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('\033[31m_=_\033[m' * 15)
    print(f'\033[36m    Contagem de {i} até {f} de {p} em {p}:\033[m')
    sleep(1.5)
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}_',end='')
            sleep(0.5)
            cont += p
        print('FIM!!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}_', end='')
            sleep(0.5)
            cont -= p
        print('FIM!!')
        print('\033[31m_=_\033[m' * 15)


# programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)