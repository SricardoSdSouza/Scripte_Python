'''Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.'''

import math
num =int(input('Digite um número : '))
n=num
d = num*2
t = num*3
r = math.sqrt(num)
print('O dobro de {} vale ={} , o triplo de {} vale = {} e a raiz de {} vale = {:.3f}'.format(n,d,n,t,n,r))
print('Raiz quadrado é =',num**0.5)