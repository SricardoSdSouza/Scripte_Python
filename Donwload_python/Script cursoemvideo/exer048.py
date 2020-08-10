'''Faça um programa que calcule a soma entre todos os números impares que
são múltiplos de três e que se encontram no intervalo de 1 até 500.'''
'''n = 0
for c in range(1,501,2):
    if c % 3 == 0:
        n = c + n
print('A soma é {}'.format(n))'''
# Solução do Guanabara
soma = 0
cont = 0
for c in range(1,501,2):
    if c % 3 == 0:
        cont += 1
        soma = soma + c
print('A soma de todos os {}, números solicitados é {}'.format(cont,soma))