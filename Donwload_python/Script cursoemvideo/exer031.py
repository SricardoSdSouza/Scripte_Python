'''Desenvolva um programa que pergunte a distância de uma viagem em km.
Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200 km e R$0,45 para viagens mais longas'''

'''
# minha resolução
distancia = float(input('Digite a distância percorrida em sua viagem: '))
if distancia <= 200:
    print('O preço da sua viagem é de :',distancia*0.50)
else:
    print('O preço de sua viagem é de: ',distancia*0.45)
'''
# Resolução do Guanabara
'''distancia = float(input('Qual é a distância da sua viagem? '))
print('Você esta prestes a começar uma viagem de {}Km.'.format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))'''
# forma simplificada acho confusa mas reduz o codigo

distancia = float(input('Qual é a distância da sua viagem? '))
print('Você esta prestes a começar uma viagem de {}Km.'.format(distancia))
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))