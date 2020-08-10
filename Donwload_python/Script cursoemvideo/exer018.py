'''Faça um programa que leia um ângulo qualquer e mostre na tela o valor seno, cosseno e tangente desse ângulo.'''
'''
import math
angulo=float(input('Digite um angulo qualquer: '))
sen=math.sin(angulo)
cos=math.cos(angulo)
tang=math.tan(angulo)
print('Para o ângulo {}° , seu seno é {:.2f}° , o cosceno é {:.2f}° , e a tangente é {:.2f}°'.format(angulo,sen,cos,tang))
'''
# Resolução do Guanabara
#import math
#angulo = float(input('Digite o ângulo que desejar : '))
#s = math.sin(math.radians(angulo))
#c = math.cos(math.radians(angulo))
#t = math.tan(math.radians(angulo))
#print('Para o angulo {}°,\n o seno é {:.2f}°,\n o cosceno é {:.2f}° \ne a tangente {:.2f}°'.format(angulo,s,c,t))
# pode importar somente o que precisa
from math import radians,sin,cos,tan
angulo = float(input('Digite o ângulo que desejar : '))
s = sin(radians(angulo))
c = cos(radians(angulo))
t = tan(radians(angulo))
print('Para o angulo {}°,\n o seno é {:.2f}°,\n o cosceno é {:.2f}° \ne a tangente {:.2f}°'.format(angulo,s,c,t))