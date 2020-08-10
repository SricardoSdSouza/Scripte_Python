num = [2,5,9,1]
print(num)
print('substituindo o 9 pelo 3')
num[2] = 3
print(num)
print('incluindo o 7')
num.append(7)
print(num)
print('Incluindo um número na lsita na posição 2 por ex')
num.insert(2,0)
print(num)
print('Usando o sort()')
num.sort()
print(num)
print('Usando o reverse=True')
num.sort(reverse=True)
print(num)
print('Contando quantos elementos tem na lista')
print(f'Essa lista tem {len(num)} elementos.')
print('para eliminar o ultimo valor da lista usa pop()')
num.pop()
print(num)
print('para eliminar o ultimo valor da lista usa pop ou coloca o indice pop(2)')
num.pop(2)
print(num)
print('O comando remove, elimina o elemento na primeira ocorrência ex,')
num.insert(3,2)
print(num)
print('Usando o remove elemento 2')
num.remove(2)
print(num)
print('Se mandar remover um número que não existe da erro então usa a funçao if')
if 4 in num:
    num.remove(4)
else:
    print('Não existe o número 4')

print('-=-'*20)
# Mais alguns exemplos:
print('\033[31mNovo exemplo\033[m')
valores = list()
#valores = [] pode usar assim ou como declarado acima
valores.append(5)
valores.append(9)
valores.append(4)
print(valores)
for v in valores:
    print(f'{v}...')
print('Para escrever na mesma linha')
for v in valores:
    print(f'{v}...',end='')
print('\n-=-'*20)
print('\nSe quiser usar as chaves ou indices:')
for c,v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Chegamos ao final da lista.')
print('-=-'*20)
print('Pode colocar um valor na lista pelo teclado ex:')
nvalores = []
'''for cont in range(0,5):
    nvalores.append(int(input('Digite um valor: ')))
for c,v in enumerate(nvalores):
    print(f'Na posição {c} encontrei o valor {v}!')'''
print('-=-'*20)
print('Novo exemplo usando lista')
a = [2,3,4,7]
b = a
print(f'A lista A: {a}')
print(f'A lista B: {b}')
print('-=-'*20)
# o Python iguala as listas se eu atribuir na lista b a lista a receber o mesmo valor
print('Atribuindo valor na lista veja que atribuindo na b a lista a recebe tambem')
a = [2,3,4,7]
b = a
b[2] = 8
print(f'A lista A: {a}')
print(f'A lista B: {b}')
print('-=-'*20)
print('Para que não aconteça isso pode atribuir somente os elementos da lista a')
a = [2,3,4,7]
b = a[:]
b[2] = 8
print(f'A lista A: {a}')
print(f'A lista B: {b}')