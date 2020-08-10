'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final, mostre:
- Quantas vezes apareceu o valor 9.
- Em que posição foi digitado o primeiro valor 3.
- Quais foram os números pares.'''
#print(c.count(5))# testar quantas vezes apareco o número 5 por ex
#print(c.index(8))# mostra qual a posição que esta o 8 por ex

numero = (int(input('Digite o 1º número: ')),
          int(input('Digite o 2º número: ')),
          int(input('Digite o 3º número: ')),
          int(input('Digite 0 4º número: ')))
print(f'Você digitou estes  {numero}')
print(f'O número 9 apareceu  {numero.count(9)} vezes')
if 3 in numero:
    print(f'O número 3 apareceu na {numero.index(3)+1}º posição')
else:
    print('O número 3 não foi digitado!')
print('Os valores pares digitados foram ',end='')
for n in numero:
    if n % 2 == 0:
        print(n,' -',end='')
