'''O mesmo professor de desafio anterior que sortear a ordem de apresentação de trabalhos
dos alunos, faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.'''
#import random
from random import shuffle
n1 = str(input('Digite o Primeiro aluno : '))
n2 = str(input('Digite o Segundo aluno : '))
n3 = str(input('Digite o Terceiro aluno : '))
n4 = str(input('Digite o Quarto aluno : '))
lista = [n1,n2,n3,n4]
shuffle(lista)
print('A ordem de apresentação será : ')
print(lista)