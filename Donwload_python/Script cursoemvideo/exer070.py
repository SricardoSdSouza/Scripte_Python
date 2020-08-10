'''Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar.
No final, mostre:
a)	Qual é o total gasto na compra
b)	Quantos produtos custam mais de R$ 1000.
c)	Qual é o nome do produto mais barato.'''
resp = 'S'
total = maior = menor = cont = 0
barato =''
print('-='*25)
print('Bem vindo ao Baratão Guanabara')
print('-='*25)
while True:
    produto = str(input('Digite o nome do produto: ')).strip()
    preco = float(input('Informe o preço do produto: R$ '))
    total += preco
    if preco >= 1000:
        maior += 1
    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    resp =' '
    while resp not in 'SN':
            resp = str(input('Quer continuar ? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
         break
print(f'O total gasto foi R$ {total} ')
print(f'e {maior} produto(s) maior(es) que R$ 1000,00.')
print(f'O {barato} é o produto mais barato.')
print('O produto mais barato é o '.format(barato))
'''total = totmil = menor = cont = 0
barato = ''
print('-=-'*25)
print('          BEM VINDO AO VAREJÃO BARATÃO')
print('-=-'*25)
while True:
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço : R$ '))
    cont +=1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1:
        menor = preço
        barato = produto
    else:
        if preço < menor:
            menor = preço
            barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total de compras foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R$ {menor:.2f}')'''