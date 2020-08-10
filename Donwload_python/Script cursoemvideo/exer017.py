'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
de um triângulo retângulo e mostre o comprimento da hipotenusa.'''

'''from math import sqrt
c_op= float(input('Digite o valor do cateto : '))
c_ad= float(input('Digite o valor do outro cateto: '))
a= sqrt(c_op**2 + c_ad**2)
hip= a
#print('A hipotenusa vale : ',hip,'m.')
print('O valor da Hipotenusa é {:.2f}m ,\n para um cateto adjacente {}m e cateto oposto de {}m'.format(a,c_ad,c_op))'''
'''
# Resolução do Guanabara
# essa resolução é sem importar biblioteca
co=float(input('Comprimento do cateto oposto: '))
ca=float(input('Comprimento do cateto adjacente : '))
hi =(co**2 + ca**2)**1/2
print('A hipotenusa vai medir {:.2f}'.format(hi))'''

# importanto toda a bilblioteca
#import math
# Importando somente a biblioteca hypot
from math import hypot
co=float(input('Comprimento do cateto oposto: '))
ca=float(input('Comprimento do cateto adjacente : '))
hi= hypot(co,ca)
print('A Hipotenusa vai medir {:.2f}'.format(hi))