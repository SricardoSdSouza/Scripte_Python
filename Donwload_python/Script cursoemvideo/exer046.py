'''Faça um programa que mostre na tela uma contagem regressiva para
o estouro de fogos de artifício, indo de 10 até 0, com pausa de um segundo entre elas.'''
'''from time import sleep
for c in range(10,0,-1):
    print(c)
    sleep(1)
print('\033[31mBUM!!!!!!!!!\033[m, iniciado os fogos de artifício')'''

# Solução do Guanabara
from time import sleep
for c in range(10,-1,-1):
    print(c)
    sleep(1)
print('\033[31mBUM!!!!!!!!!\033[m, iniciado os fogos de artifício')