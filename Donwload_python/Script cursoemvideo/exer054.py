'''Crie em programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade
e quantas já são maiores. Maior idade 21 anos'''
'''from datetime import date
d=0
cont_maior = 0
cont_menor = 0
date = date.today().year
for c in range(1,8):
    datanascimento = int(input('Informe o ano do {}º nascimento: '.format(c)))
    d +=c
    atual = date
    if atual - datanascimento <= 21:
        cont_menor += 1
    else:
        cont_maior += 1
if cont_maior == 1:
    print('{} pessoa atingiu a maior idade e {} pessoas não atingiram a maior idade.'.format(cont_maior,cont_menor))
elif cont_menor == 1:
     print('{} pessoas não atingiram a maior idade e {} Atigiram a maior idade.'.format(cont_menor, cont_maior))
print('{} pessoas atingiram a maior idade\n {} pessoas ainda não atingiram a maior idade'.format(cont_maior,cont_menor))'''
# Solução do Guanabara
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1,8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu?: '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade .'.format(totmaior))
print('E tambem {} pessoas menores de idade'.format(totmenor))