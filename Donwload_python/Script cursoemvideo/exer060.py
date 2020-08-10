'''Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex: 5! =5x4x3x2x1 = 120'''
'''fatorial = 1
n = int(input('Informe o número que será fatorado: '))
f = n
while f > 1:
    fatorial = fatorial * f
    f = f -1
print('O Fatorial de {} é = {}.'.format(n,fatorial))'''
# Resolução do Guanabara
'''from math import factorial
n= int(input('Digite um número para calcular seu Fatorial: '))
f = factorial(n)
print('O Fatorial de {} é {}'.format(n,f))'''
n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n),end='')
while c > 0:
    print('{} '.format(c),end='')
    print('x 'if c > 1 else '=',end='')
    f = f * c
    c -= 1
print(' {}'.format(f))
