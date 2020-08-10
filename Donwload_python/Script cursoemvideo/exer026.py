'''Faça um programa que leia uma frase pelo teclado e mostre:
-quantas vezes aparece a letra "A"
-em que posição ele aparece a primeira vez
-em que posição ela aparece a última vez.'''
'''
frase = str(input('Digite a frase : ')).strip()
print('A letra "a" aparece {} vezes na frase.'.format(frase.upper().count('A')))
print('A primeira letra "a" apareceu na posição {}'.format(frase.upper().find('A')+1))
print('A última letra "a" apareceu na posição {}'.format(frase.upper().rfind('A')+1))
'''
# ou assim
frase = str(input('Digite a frase : ')).strip().upper()
print('A letra "a" aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra "a" apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra "a" apareceu na posição {}'.format(frase.rfind('A')+1))