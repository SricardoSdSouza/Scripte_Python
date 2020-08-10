'''Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um
dicionário e todos os dicionários em uma lista. No final, mostre:
- Quantas pessoas foram cadastradas
-A média de idade do grupo
-Uma lista com todas as mulheres.
- Uma lista com todas as pessoas com idade acima da média'''
galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda S ou N.')
    if resp == 'N':
        break
print('\033[31m-*-\033[m'*15)
print(f'A)Foram cadastradas {len(galera)} pessoas.')
media = soma/len(galera)
print('\033[34m-*-\033[m'*15)
print(f'B)A media de idade é de {media:5.2f} anos')
print('\033[34m-*-\033[m'*15)
print('C)As mulheres Cadastradas foram  ',end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}, ', end='')
print()
print('\033[34m-*-\033[m'*15)
print('D) Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('  ',end='')
        for k , v in p.items():
            print(f'{k} = {v}; ',end='')
        print()
print('\033[34m-*-\033[m'*15)
print('     <<<< ENCERRADO >>>>')