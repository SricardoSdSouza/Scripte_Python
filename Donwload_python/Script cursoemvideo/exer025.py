'''Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.'''

nome=str(input('Digite o nome de uma pessoa : ')).strip()
print('Seu nome tem silva ? {}'.format('SILVA' in nome.upper()))