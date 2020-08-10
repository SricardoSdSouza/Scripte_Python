'''Crie um programa que leia o nome completo de uma pessoa e mostre:
 - o nome de todas as letras maiúsculas
 - o nome de todas as letras minúsculas
 - quantas letras ao todo, sem considerar os espaços
 - quantas letras tem o primeiro nome '''

nome=str(input('Digite seu nome completo = ')).strip()
separa_nome=nome.split()
print('Analisando seu nome ......')
print('Seu nome em maiúscula é = ',nome.upper())
print('Seu nome em minúscula é = ',nome.lower())
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome é \033[36m{}\033[m , e ele tem \033[31m{}\033[m letras'.format(separa_nome[0],len(separa_nome[0])))
