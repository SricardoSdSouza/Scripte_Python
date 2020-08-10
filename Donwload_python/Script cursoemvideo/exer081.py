'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
-Quantos números foram digitados.
-A lista de valores, ordenada de forma decrescente.
-Se o valor 5 foi digitado e está ou não na lista'''
numeros = []
while True:
    n = (int(input('Digite um número: ')))
    numeros.append(n)
    resp = str(input('Deseja continuar ? [S/N]: ')).strip().upper()[0]
    if resp in 'Nn':
        break
if 5 in numeros:
    print('-=-'*20)
    print(f'O numero 5 foi digitado e está na posição: {numeros.index(5)}')
else:
    print('-=-'*20)
    print('O número 5 não esta na lista!')
print('-=-'*20)
print(f'Foram digitados {len(numeros)} números na lista.')
#numeros.sort(reverse= True)
print('-=-'*20)
print(f'OS números digitados foram {numeros.sort(reverse = True)} em ordem crescente são {numeros}.')
print('***'*20)
