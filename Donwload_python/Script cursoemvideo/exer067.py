'''Faça um programa que mostre a tabuada de vários números,
um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.'''
#num=int(input('Digite um Número para ver sua tabuada : '))
num = c = 0
while True:
    num = int(input('Digite um Número para ver sua tabuada : '))
    print('==' * 22)
    if num < 0:
        break
    for c in range(1,11):
        print(f'{num:12} x {c} = {num*c}')
    print('==' * 22)
print('\033[7mPrograma Tabuada esta Encerrado !! OBRIGADO!!\033[m')