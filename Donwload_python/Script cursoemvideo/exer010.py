'''Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
e mostre quantos dólares ela pode comprar. Considerar o dólar U$1,00 a R$ 3,27.'''

qdin = float(input('Quer saber quantos dolares vc pode comprar?,\nDigite quantos Reais tem na carteira :R$ '))
d=float(input('Qual o valor do Dolar hoje? :U$ '))
dolar=d
print('Com R${} , voce pode comprar : U${:.2f}'.format(qdin,qdin/dolar))