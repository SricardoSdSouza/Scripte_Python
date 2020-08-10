'''Aprimore o desafio anterior, mostrando no final:
-A) A soma de todos os valores pares digitados.
-B) A soma dos valores da terceira coluna.
-C) O maior valor da segunda linha.'''
matriz = [[0,0,0],[0,0,0],[0,0,0]]
par = soma = maior = 0
# para alimentar a matriz
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha},{coluna}]: '))

print('-=-'*20)
# para imprimir a matriz
for li in range(0,3):
    for co in range(0,3):
        print(f'[{matriz[li][co]:^5}]',end='')
        if matriz[li][co] % 2 == 0:
            par += matriz[li][co]
    print()
print('-=-'*20)
print(f'A soma dos números pares é = {par}.')
# somente a linha que esta variando a coluna é fixa
for li in range(0,3):
    soma += matriz[li][2]
print(f'A soma dso valores da 3º coluna é = {soma}')
for co in range(0,3):
    if co == 0 :
        maior = matriz[1][co]
    elif matriz[1][co] > maior:
        maior = matriz[1][co]
print(f'O maior valor da 2º linha é = {maior}')