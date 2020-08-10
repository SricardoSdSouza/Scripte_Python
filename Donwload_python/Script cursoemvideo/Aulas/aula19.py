'''filme = {'nome':'Star Wars','ano':1977,'autor':'Gerge Lucas'}
print(filme)
for k,v in filme.items():
    print(f'O {k} é {v} ')
print('-=-'*30)
pessoas = {'nome':'Gustavo','Sexo':'M','Idade':22}
print(pessoas)
print(pessoas['nome'])
print(pessoas ['Sexo'])
print(pessoas ['Idade'])
print('-=-'*30)
print(f'O {pessoas["nome"]} tem {pessoas["Idade"]}anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print('-=-'*20)
pessoas = {'nome':'Gustavo','Sexo':'M','Idade':22}
for k in pessoas.keys():
    print(k)
print('-=-'*20)
for v in pessoas.values():
    print(v)
print('-=-'*20)
for i in pessoas.items():
    print(i,end='')
print()
print('-=-'*20)
for k , v in pessoas.items():
    print(f'{k} = {v}')
print()
print('-=-'*20)
#Apagando um valor de pessoas
pessoas = {'nome':'Gustavo','Sexo':'M','Idade':22}
del pessoas['Sexo']
for k , v in pessoas.items():
    print(f'{k} = {v}')
pessoas = {'nome':'Gustavo','Sexo':'M','Idade':22}
pessoas['nome'] = 'Leandro'
for k , v in pessoas.items():
    print(f'{k} = {v}')
# Adicionando um elemento
pessoas = {'nome':'Gustavo','Sexo':'M','Idade':22}
pessoas['peso'] = 98.5
for k , v in pessoas.items():
    print(f'{k} = {v}')
# Colocando um dicionario dentro de uma lista
brasil = []
estado1 = {'UF':'Rio de Janeiro','Sigla':'RJ'}
estado2 = {'UF':'São Paulo','Sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)
#print(estado1)
#print(estado2)
#print(brasil)
print(brasil[0])
print(brasil[1])
print(brasil[0]['UF'])
print(brasil[1]['Sigla'])'''
# fazendo dicionario dentro de uma lista
estado = dict()
brasil = list()
'''for c in range(0,3):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['Sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    print(e)
#print(brasil)'''
for c in range(0,3):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['Sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
'''for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem o valor {v}.')'''
# Pode usar assim tambem
for e in brasil:
    for v in e.values():
        print(v,end=' ')
    print()