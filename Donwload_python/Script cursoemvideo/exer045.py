'''Crie um programa que faça o computador jogar JOKEMPÔ com você.'''

from random import randint
from time import sleep
itens = ('Pedra','Papel','Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('\033[34m{:=^30}\033[m'.format('JO'))
sleep(1)
print('\033[35m{:=^40}\033[m'.format('KEN'))
sleep(1)
print('\033[36m{:=^50}\033[m'.format('PO!!!'))
print('-='*11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador Jogou {}'.format(itens[jogador]))
print('-='*11)
if computador == 0: # o computador jogou PEDRA
    if jogador == 0 :
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')

elif computador == 1: # o computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2: # o computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')
