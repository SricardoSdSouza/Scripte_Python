'''Crie um programa onde o usuário possa digitar vários valores numéricos
e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados em ordem crescente'''
vlista = []
while True:
    n = (int(input('Digite um número: ')))
    #Testa se o número digitado esta dentro da lista
    if n not in vlista:
        vlista.append(n)
        print('Valor adicionado com sucesso!!')
    else:
        print('Este número ja foi incluido!, tente outro.')
    resp = str(input('Deseja continuar ? [S/N]: ')).strip().upper()[0]
    if resp in 'Nn':
        break
print('=='*30)
print(f'Os números ordenados são {sorted(vlista)}')