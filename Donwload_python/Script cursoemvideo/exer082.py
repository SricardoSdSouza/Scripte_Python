'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso,crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados,
respectivamente. Ao final, mostre o conteúdo das três listas geradas'''
'''lernumeros = []
pares = []
impares = []
while True:
    n = (int(input('Digite um número: ')))
    lernumeros.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    resp = str(input('Deseja continuar ? [S/N]: ')).strip().upper()[0]
    if resp in 'Nn':
        break
print(f'Os números digitados foram:.. {lernumeros}')
print(f'Os números pares são:........ {pares}')
print(f'Os números ímpares são:...... {impares}')'''
#Solução do Guanabara:
num = list()
pares = list()
impares = list()
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer Continuar? [S/N]: '))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('-=-'*20)
print(f'A lista completa é = {num}')
print(f'A lista de pares é = {pares}')
print(f'A lista de ímpares é = {impares}')
print('-=-'*20)
