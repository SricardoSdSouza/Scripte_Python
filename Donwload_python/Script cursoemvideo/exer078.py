'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista'''
'''numeros =[]
maior = menor = 0
for  c in range(1,6):
    numeros.append(int(input(f'Digite o {c}º número: ')))
print(f'Você digitou os seguintes valores :{numeros}')
print(f'O maior valor da lista é {max(numeros)} na posição = ',end='')
for pos , c in enumerate(numeros):
    maior = max(numeros)
    if c == maior:
        print(f'{pos}...',end='')
print()
print(f'O menor valor da lista é {min(numeros)} na posição = ',end='')
for pos , c in enumerate(numeros):
    menor = min(numeros)
    if c == menor:
        print(f'{pos}...',end='')
print()'''
# solução do Guanabara
listanum = []
mai = men = 0
for c in range(0,5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print('=='*30)
print(f'Voce digitou os seguintes valores : {listanum}')
print(f'O maior valor digitado foi {mai} na(s) posição(oes):',end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitadofoi {men} na(s) posição)=(ões):',end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}...')
print('Fim')