'''Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
-O primeiro valor é maior
-O segundo valor é maior
-Não existe valor maior, os dois são iguais.
'''

print('Bom dia!')
n1 = int(input('Digite o primeiro número : '))
n2 = int(input('Digite o segundo número : '))
if n1 > n2:
    print('O Número {} é maior que o Número {}'.format(n1,n2))
    print('\033[36mO Número {} é menor que o menor {}\033[m'.format(n2,n1))
elif n2 > n1:
    print('O Número {} é maior que o Número {}'.format(n2,n1))
    print('\033[36mO Número {} é menor que o Número {}\033[m'.format(n1, n2))
else:
    print('\033[7mOs Números são iguais.\033[m')
# Resolução do Guanabara
'''mesma resolução'''