'''Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado
e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$ 0,15 por km rodado.'''

'''
km=float(input('Informe a quantidade de km que foi percorrido : '))
dias=float(input('Por quantos dias foram utilizados pelo usuário : '))
print('O preço total pelo aluguel do carro é de R$ {}'.format(km+(km*0.15+dias*60)))
'''
#Resolução do Guanabara
dias= int(input('Quantos dias alugados?: '))
km = float(input('Quantos km rodados?: '))
pago = dias * 60 + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(pago))
