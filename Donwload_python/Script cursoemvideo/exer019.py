'''Um professor que sortear um de seus alunos para apagar o quadro,
faça um programa que ajude ele, lendo o nome deles e escreve o nome do escolhido.'''
import random
# Pode importar somente a função que vai usar
from random import choice
n1 = str(input('Primeiro Aluno: '))
n2 = str(input('Segundo Aluno: '))
n3 = str(input('Terceiro Aluno: '))
n4 = str(input('Quarto Aluno: '))
lista =[n1,n2,n3,n4]
escolhido = choice(lista)
print('O Aluno escolhido foi {}'.format(escolhido))