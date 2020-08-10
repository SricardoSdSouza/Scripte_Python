'''Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.'''

'''
preco=float(input('Qual o preço do produto desejado : R$ '))
desc = float(input('Digite o desconto em percentual para este produto: '))
p_desc = preco*(desc/100)
n_preco = preco-p_desc
print('Que bom!!! reduziu o preço de R$ {} , agora vc vai pagar somente R$ {:.2f}'.format(preco,n_preco))
#print('Que bom baixou o preço de {} , para {}'.format(preco,preco-(preco*desc/100))
'''
#Resolução do Guanabara
preco=float(input('Qual é o preço do produto? R$ '))
novo = preco-(preco*5/100)
print('O produto que custava R${} , na promoção com desconto vai custar R${:.2f}'.format(preco,novo))