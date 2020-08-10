'''Crie um programa que tenha uma tupla totalmente preenchida com uma
contagem por extensão, de zero até vinte.
Seu programa deverá ler um número pelo teclado
(entre 0 e 20) e mostra-lo por extenso.'''

nomes = ('Zero','Um','Dois','Três','Quatro',
         'Cinco','Seis','Sete','Oito','Nove','Dez',
         'Onze','Doze','Treze','Catorze','Quinze',
         'Dezessesis','Dezessete','Dezoito','Dezenove','Vinte')
'''while True:
        num = int(input(' Digite um número entre (0 e 20): '))
        if 0 <= num <= 20:
            break
        else:
            print('Tente Novamente!',end='')
print(f'Voce digitou o número {nomes[num]}')'''
while True:
        num = int(input(' Digite um número entre (0 e 20): '))
        if 0 <= num <= 20:
            print(f'Voce digitou o número {nomes[num]}')
        else:
            print('Tente Novamente!',end='')
        resp = ' '
        while resp not in 'SN':
             resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if resp == 'N':
             break
#print(f'Voce digitou o número {nomes[num]}')
