'''Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''
from time import sleep
n1 = int(input('Informe o Primeiro Valor: '))
n2 = int(input('Informe o Segundo Valor: '))
opcao = 0
maior = 0
while opcao != 5:
    print('''Estas são as opções:
    [1] para somar
    [2] para multiplicar
    [3] para número maior
    [4] novos números
    [5] sair do program''')
    opcao = int(input('>>>Informe qual é a sua opção: '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma de {} + {} = {}.'.format(n1,n2,soma))
    elif opcao == 2:
        produto = n1 * n2
        print('A multiplicação entre {} x {} é = {}.'.format(n1,n2,produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        elif n2 > n1:
            maior = n2
        else:
            print('Numeros são iguais!não tem maior.')
            maior = n1
        print('Entre {} e {} o maior valor é {}'.format(n1,n2,maior))
    elif opcao == 4:
        maior = 0
        print('Informe os números novamente')
        n1 = int(input('Informe o Primeiro Valor: '))
        n2 = int(input('Informe o Segundo Valor: '))
    elif opcao == 5:
        print('\033[36mFinalizando o programa.....\033[m')
    else:
        print('Opção inválida!, Escolha uma opção válida.')
    print('=-='*12)
    sleep(2)
print('\033[7mFim do Programa! Volte sempre!.\033[m')

