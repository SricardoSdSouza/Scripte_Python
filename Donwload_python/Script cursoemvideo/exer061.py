'''Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.'''
'''primeiro = int(input('Informe o Primeiro Termo : '))
razao =int(input('Informe a Razão: '))
decimo = primeiro + (10 - 1) * razao
for c in range (primeiro,decimo + razao,razao):
    print('{}'.format(c),end=' ->')
print('Acabou')'''
# Solução do Guanabara
print('\033[7mGerador de PA\033[m')
print('\033[34m==\033[m'*12)
primeiro = int(input('Informe o Primeiro Termo : '))
razao =int(input('Informe a Razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(termo),end='')
    termo = termo + razao
    cont += 1
print('Fim')