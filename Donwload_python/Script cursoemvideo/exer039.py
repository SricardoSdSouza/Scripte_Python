'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
-Se já passou do tempo do alistamento
Seu programa também deverá mostrar o tempo que faltou ou que passou do prazo.'''

'''from datetime import date
print('"PROGRAMA DE ALISTAMENTO MILITAR"')
ano = int(input('Digite o ano de seu nascimento : '))
ano_at = date.today().year
h_alistr = ano_at - ano

if h_alistr < 17:
    print('Ainda não esta na hora de alistar! ')
    print('Ainda faltam {} dias.'.format((18 - h_alistr)*365))
elif h_alistr >= 17 and h_alistr <= 18:
    print('Hora de se apresentar ao serviço Militar de sua cidade.')
else:
    print('Passou do tempo de se apresentar ao serviço Militar.')
    print('Já se passaram  {} dias.'.format((h_alistr - 18) * 365))'''
# Resolução do Guanabara
from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
sexo =input('Digite F para feminino e M para masculino : ')
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade,atual))
if sexo == 'F':
    print('Você não é obrigada a se alistar')
elif idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!.')
elif idade < 18:
     saldo = 18 - idade
     print('Ainda faltam {} ano(s) para o alistamento.'.format(saldo))
     ano = atual + saldo
     print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} ano(s).'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))
