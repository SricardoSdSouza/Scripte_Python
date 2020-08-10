'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
-A) Quantas pessoas foram cadastradas.
-B) Uma listagem com as pessoas mais pesadas.
-C) Uma listagem com as pessoas mais leves.'''
# cadastrando uma lista temporaria
temp = []
#cadastrando a lista principal
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(str(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    #apagando a lista temporaria
    temp.clear()
    resp = str(input('Desja continar? [S/N]: ')).strip().upper()[0]
    if resp in 'Nn':
        break
print('-='*30)
print(f'Os dados foram {princ}')
# não precisa de contador pois o len me da a quantidade
print(f'Ao todo vc cadastrou {len(princ)}')
print(f'O maior peso é {mai}kg. Peso de ',end='')
for p in princ:
    # a posição p[1] retorna o valor na posição
    if p[1] == mai:
        #a posição p[0] retorna o nome
        print(f'[{p[0]}]',end='')
print()
print(f'O menor peso é {men}kg. Peso de ',end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}]',end='')
print()
print('-='*30)