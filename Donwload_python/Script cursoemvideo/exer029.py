'''Escreva um programa que leia a velocidade de um carro se ele ultrapassar 80km/h,
mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada km acima do limite.'''

'''
velocidade = float(input('Digite a velocidade atual do veículo : '))
if velocidade <= 80:
    print('Parabéns você esta dentro da velocidade permitida')
else:
    v=(velocidade - 80)* 7
    print('A velocidade foi de {}'.format(velocidade))
    print('Você ultrapassou a velocidade permitida,\nvai pagar uma multa de R${:.2f}'.format(v))
'''
# Resolução do Guanabara
velocidade = float(input('Qual é a velocidade atual do carro ? '))
if velocidade > 80:
    print('\033[31mMULTADO!\033[m Você excedeu o limite permitido que é de 80km/h')
    multa=(velocidade - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com cuidado e segurança!')