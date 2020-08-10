'''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos :MIRIM
-Até 14 anos: INFATIL
-Até 19 anos: JUNIOR
-Até 20 anos: SÊNIOR
-Acima: MASTER.'''

'''from datetime import date
print('\033[31mSEJA BEM-VINDO CONFEDERAÇÃO NACIONAL DE NATAÇÃO\033[m')
d_nascimento = int(input('Digite o ano de nascimento do atleta: '))
ano = date.today().year
categoria = ano - d_nascimento
if categoria <= 9:
    print('A categoria do Atleta é \033[1;32m"MIRIM"\033[m')
elif categoria > 9 and categoria <= 14:
    print('A categoria do atleta é \033[1;33m"INFANTIL"\033[m')
elif categoria >14 and categoria <= 19:
    print('A categoria do atleta é \033[1;34m"JUNIOR"\033[m')
elif categoria > 19 and categoria <= 25:
    print('A categoria do atleta é \033[1;35m"SÊNIOR"\033[m')
else:
    print('A categoria do atleta é \033[1;36m"MASTER"\033[m')'''
# Resolução do Guanabara
from datetime import date
atual = date.today().year
nascimento = int(input('Ano de Nascimento: '))
idade = atual - nascimento
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação: "MIRIM"')
elif idade <= 14:
    print('Classificação: "INFANTIL"')
elif idade <= 19:
    print('Classificação: "JUNIOR"')
elif idade <= 25:
    print('Classificação: "SÊNIOR"')
else:
    print('Classificação: "MASTER"')

