'''Crie um programa que leia um número inteiro e mostre na tela se ele é par ou impar'''

'''
n=int(input('Digite um numero: '))
num= n % 2
if num == 0:
    print('Este número é par.')
else:
    print('Este número é impar.')
'''
# Resolução do guanabara
numero = int(input('Me diga um número qualquer: '))
resultado = numero % 2
if resultado == 0:
    print('O número \033[34m{}\033[m é PAR'.format(numero))
else:
    print('O número \033[31m{}\033[m é IMPAR'.format(numero))