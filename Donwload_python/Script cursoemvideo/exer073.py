'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela
do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
- Apenas os 5 primeiros colocados.
- OS últimos 4 colocados da tabela
- Uma lista com os times em ordem Alfabética
- Em que posição na tabela esta o time da Chapecoense'''
from future.backports.email._policybase import _append_doc

brasileirao = ('Palmeiras','Flamengo','Internacional','Grêmio','São Paulo',
               'Atletico Mineiro','Athelico Paranaense','Cruzeiro','Botafogo','Santos',
               'Bahia','Fluminense','Coríntians','Chapecoense','Ceara','Vasco','Sport','América Mineiro',
               'Vitória','Paraná')
print('*='*40)
print('{:^75}'.format('BRASILEIRÃO DE 2018 - CLASSIFICAÇÃO'))
print('*='*40)
print('Os cinco primeiros colocados são :')
print(f'\033[36m{brasileirao[0:5]}\033[m')
print('=-'*40)
print('O 4 últimos colocados são:')
print(f'\033[31m{brasileirao[16:]}\033[m') # pode usar de [-4:] mesmo resultado
print('*='*40)
print('Times em ordem alfabética:')
print(sorted(brasileirao))
print('=-'*40)
print(f'O time da Chapecoense esta na {brasileirao.index("Chapecoense")+1}ª posição')
print('*='*40)

while True:
    time= str(input('Digite o nome do seu time e veja a colocação na Tabela: '))
    print(f'O {time} esta na {brasileirao.index(time)+1}ª posição')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Digite "S" para continuar ou "N" para sair: ')).strip().upper()[0]
    if resp == 'N':
        break

