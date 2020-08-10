'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-0.'''
'''soma = 0
for c in range(1,7):
    if c % 2 == 0:
       soma += c
print('A soma dos valores é {} '.format(soma))'''
# solução do Guanabara
soma = 0
cont = 0
for c in range (1,7):
    num = int(input('Digite o {}º valor : '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você informou {} números pares e a soma dos pares foi {}'.format(cont,soma))