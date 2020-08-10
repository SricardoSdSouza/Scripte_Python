'''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
Programa deverá escrever na tela se o usuário venceu ou perdeu.'''
'''
import random
n = random.randint(0,5)
print('Consegue adivinhar o número que o computador pensou?')
num = int(input('Adivinhe o número : '))
if n == num:
    print('Parabéns  :) você adivinhou !!!, você é bom heim!!')
else:
    print('Tente de novo, você esta sem sorte! :(')
'''
# Solução do Guanabara
from random import randint
from time import sleep
computador =randint(0,5) # faz o computador escolher um numero aleatorio
print('=*='*20)
print('\033[36mVou pensar em um número entre 0 e 5, Tente adivinhar....\033[m')
print('=*='*20)
jogador = int(input('Em que número pensei? = '))#jogador tenta adivinhar
print('\033[34mPROCESSANDO .....\033[m')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer "\033[33myou win"\033[m')
else:
    print('GANHEI! Eu pensei no número \033[31m{}\033[m e não no {}'.format(computador,jogador))
