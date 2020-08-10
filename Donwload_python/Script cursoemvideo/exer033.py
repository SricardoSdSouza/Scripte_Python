'''Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'''

'''num1=int(input('Escreva o primeiro número: '))
num2=int(input('Escreva o segundo número: '))
num3=int(input('Escreva o terceiro número: '))
if num1 > num2 and num1 > num3:
    print('O número {}, é o maior'.format(num1))
elif num2 > num1 and num2 > num3:
    print('O número {}, é o maior'.format(num2))
elif num3 > num1 and num3 > num2:
    print('O número {}, é o maior'.format(num3))
if num1 < num2 and num1 < num3:
    print('O número {}, é o menor'.format(num1))
elif num2 < num3 and num2 < num1:
    print('O número {}, é o menor'.format(num2))
elif num3 < num1 and num3 < num2:
    print('O número {}, é o menor'.format(num3))
else:
    print('Os números são iguais!')'''
# Resolução do Guanabara
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
#verificando quem é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
# vrificando quem é o menor
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('O maior valor digitado foi {}'.format(maior))
print('O menor valor digitado foi {}'.format(menor))
