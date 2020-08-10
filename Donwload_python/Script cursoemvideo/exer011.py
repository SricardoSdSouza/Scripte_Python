'''Faça um programa que leia a altura e a largura de uma parede em metros.
Calcule a sua área e a quantidade de tinta necessária para pintá-la.
Sabendo que cada litro de tinta pinta uma área de 2m².'''

'''
altura = float(input('Digite o valor em metros para a altura da parede : '))
largura = float(input('Digite o valor em metros para a largura da parede : '))
area = altura * largura
print('A quantidade de tinta necessária para pintar uma parede de area {}m2,\nserá de {}l'.format(area,area/2))
'''
# resolução do Guanabara
larg=float(input('A Largura da parede é : '))
alt=float(input('A Alturada parede é : '))
area = larg*alt
tinta = area/2
print('Sua parede tem a dimensão {} x {} , e sua área tem {}m²'.format(larg,alt,area))
print('Para pintar a parede de {} m², voce precisa de {}l de tinta'.format(area,tinta))