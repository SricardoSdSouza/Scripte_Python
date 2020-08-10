# cadastrando uma lista temporaria
temp = []
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
    if p[1] == mai:
        print(f'[{p[0]}]',end='')
print()
print(f'O menor peso é {men}kg. Peso de ',end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}]',end='')
print()
print('-='*30)
