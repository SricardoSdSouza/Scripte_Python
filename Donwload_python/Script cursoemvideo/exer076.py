'''Crie um programa que tenha uma tupla única com nomes de produtos
e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''
produtos = ('Lápis',1.75,
            'Borracha',2.00,
            'Caderno',15.90,
            'Estojo',25.00,
            'Transferidor',4.20,
            'Compasso',9.99,
            'Mochila',120.32,
            'Canetas',22.30,
            'Livro',34.90)
print('--'*20)
print(f'\033[36m{"Listagem de Preços":^40}\033[m')
print('--'*20)
for c in range(0,len(produtos)):
    if c % 2 == 0:
        print(f'{produtos[c]:.<31}',end='')
    else:
        print(f'{produtos[c]:>9.2f}')
print('##'*20)