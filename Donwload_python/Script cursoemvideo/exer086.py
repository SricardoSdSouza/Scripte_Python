'''Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.'''
matriz = [[0,0,0],[0,0,0],[0,0,0]]
# para alimentar a matriz
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha},{coluna}]: '))
print(matriz)
print('-=-'*20)
# para imprimir a matriz
for li in range(0,3):
    for co in range(0,3):
        print(f'[{matriz[li][co]:^5}]',end='')
    print()