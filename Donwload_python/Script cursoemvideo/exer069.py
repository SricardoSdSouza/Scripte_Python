'''Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário que ou não continuar. No final, mostre:
a)	Quantas pessoas tem mais de 18 anos
b)	Quantos homens foram cadastrados
c)	Quantas mulheres tem menos de 20 anos.'''
'''maior = h = m = 0
resp = 'S'
while resp in 'Ss':
    sexo = str(input('Informe o sexo [M/F]: ')).strip().upper()[0]
    while sexo not in 'MF:
        sexo = str(input('Digiteo sexo [M/F]: ')).strip().upper()[0]
    idade = int(input('Informe a idade: '))
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        h += 1
    if sexo == 'F':
        if idade < 20:
            m += 1
    resp = str(input('Quer continuar ? [S/N]: ')).strip().upper()[0]
    while resp not in 'SN':
        if resp != 'S' or resp != 'N':
           resp = str(input('Quer continuar ? [S/N]: ')).strip().upper()[0]
print(f'Foram {maior} maiores de 18 anos, Foram {h} homens e {m} mulheres menores de 20 anos.')'''
# Solução do Guanbara
tot18 = totH =totM20 = 0
while True:
    idade = int(input('Digite Idade : '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} homen(s) cadastrados.')
print(f'E temos {totM20} mulher(es) com menos de 20 anos.')