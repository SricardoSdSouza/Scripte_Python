'''Escreva um programa que leia um valor em metros e exiba convertido em centímetros e milímetros.'''

num = int(input('Digite um valor em metros : '))
n_cm = num * 100
n_mm = num * 1000
print('O',num,'Tem o valor de = {} cm, e de {} mm'.format(n_cm,n_mm))
