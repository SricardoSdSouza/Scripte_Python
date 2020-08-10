'''Crie um programa onde o usuário possa digitar sete valores numéricos e
cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente.'''
numeros = []
num = 0
pares = []
impares = []
for c in range(0,7):
    num =int(input(f'Digite o {c+1}º número = '))
    if num % 2 == 0:
        pares.append(num)
    else:
         impares.append(num)
numeros.append(pares[:])
numeros.append(impares[:])
print(numeros)
print(f'OS valores pares são {sorted(numeros[0])}')
print(f'OS valores ímpares são {sorted(numeros[1])}')
# Resolução do Guanabara:
num = [[],[]]
valor = 0
for c in range(1,8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-=-'*20)
print(f'Todos os valores: {num}')
# pode usar o sort para ordenar
#num[0].sort()
#num[1].sort()
#ou usar dentro do print como abaixo
print(f'OS valores pares digitados foram: {sorted(num[0])}')
print(f'OS valores [impares digitados foram: {sorted(num[1])}')