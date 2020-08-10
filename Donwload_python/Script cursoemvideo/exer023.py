'''Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados:
ex:
	Digite um número = 1834
	unidade = 4
	dezena = 3
	centena = 8
	milhar = 1 '''

'''
#Como não foi feito repetições não funciona para numeros menores que 4 ou seja se digitar 123 da erro
num = int(input('Informe um número = '))
n = str(num)
print('Analizando o número {}'.format(num))
print('Unidades : {}'.format(n[3]))
print('Dezenas : {}'.format(n[2]))
print('Centenas : {}'.format(n[1]))
print('Milar :'.format(n[0]))
'''
# Fazendo de forma matemática
num = int(input('Informe um número = '))
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Tem {} unidades'.format(unidade))
print('Tem {} dezenas'.format(dezena))
print('Tem {} centenas'.format(centena))
print('Tem {} milhar'.format(milhar))