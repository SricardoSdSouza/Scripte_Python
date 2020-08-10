'''Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno
retangular(largura e comprimento) e mostre a área do terreno'''
def area(l,c):
    dimensao = l * c
    print('\033[34m-*-\033[m' * 15)
    print(f'Para uma metragem de {c} m x {l} m')
    print(f'As Dimensões do Terreno são {dimensao:.3f} m².')
    print('\033[34m-*-\033[m' * 15)
    
# Programa principal
print('\033[7m  --> CALCULANDO A ÁREA DE UM TERRENO <--\033[m')
largura = float(input('Digite a Largura do Terreno (m): '))
comprimento = float(input('Digite o Comprimento do Terreno (m): '))
area(largura,comprimento)
# Solução do Guanabara
'''def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg} x {comp} é de {a}m²')

# Programa principal
print('Controle de Terrenos')
print('-'*20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)'''

