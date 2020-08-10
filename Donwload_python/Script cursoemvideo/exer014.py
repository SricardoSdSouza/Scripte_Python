'''Escreva um programa que converta uma temperatura digitada em °C e converta para °F.'''

'''
temperaturafahrenheit = 86.0
tempcelsius = (temperaturafahrenheit - 32)*5/9
print("a temperatura em celsius e",tempcelsius)
'''
#Resolução do Guanabara
c=float(input('Informe a temperatura em graus ºC : '))
f=((9 * c/5) + 32)
print('A temperatura de {}ºC corresponde a {} ºF'.format(c,f))