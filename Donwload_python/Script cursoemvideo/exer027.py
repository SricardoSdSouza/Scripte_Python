'''Faça um programa que leia o nome completo de uma pessoa mostrando em seguida o primeiro e o último nome separadamente
ex: Ana Maria de Souza
	primeiro nome = Ana
	Último nome = Souza.'''

nome = str(input('Digite seu nome completo : ')).strip()
n = nome.split()
print('Muito Prazer em te conhecer ! ')
print('O primeiro nome é {} '.format(n[0]))
print('Seu o último nome é {}'.format(n[len(n)-1]))