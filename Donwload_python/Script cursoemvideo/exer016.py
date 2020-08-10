'''Crie um programa que leia um número real qualquer pelo teclado
e mostre na tela a sua porção inteira. Ex: 6.127   --   O número 6.127 tem a parte inteira 6.'''

'''
num = float(input('Digite um número qualquer : '))
n=int(num)
print('O valor digitado foi {}, e sua porção inteira é {}'.format(num,n))
'''
# Resolução do Guanabara
'''
#como so precisou da função trunc, não precisa importar toda a biblioteca math
import math
num = float(input('Digite um valor : '))
print('O valor digitado foi {} e a sua proção inteira é {}'.format(num,math.trunc(num)))
'''
'''from math import trunc
num = float(input('Digite um valor : '))
print('O valor digitado foi {} e a sua proção inteira é {}'.format(num,trunc(num)))'''

num = float(input('Digite um valor : '))
print('O valor foi {} e sua porção inteira é {}'.format(num,int(num)))
