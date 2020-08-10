'''Faça um programa que leia um ano qualquer e mostre se ele é bissexto.'''

'''ano = int(input('Digite um ano qualquer: '))
if ano % 400 == 0 and ano % 4 == 0 and ano % 100 != 0:
    print('Ano {} Bissexto.'.format(ano))
else:
    print('Este ano {} não é Bissexto'.format(ano))'''
# Rosolução do Guanabara
'''ano = int(input('Que ano quer analisar? '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} não é BISSEXTO'.format(ano))'''
# pegando o ano atual em que se esta
from datetime import date
ano = int(input('Que ano quer analisar? coloque zero para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} não é BISSEXTO'.format(ano))