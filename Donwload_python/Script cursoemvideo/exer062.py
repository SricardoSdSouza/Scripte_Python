'''Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos.'''
print('\033[7mGerador de PA\033[m')
print('\033[34m==\033[m'*12)
primeiro = int(input('Informe o Primeiro Termo : '))
razao =int(input('Informe a Razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você que mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
