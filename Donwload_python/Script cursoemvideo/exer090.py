'''Faça um programa que leia nome a média de um aluno, guardando também a situação (aprovado ou reprovado)
em um dicionário. No final, mostre o conteúdo da estrutura na tela.'''
boletin ={}
boletin['nome']  = str(input('Nome: '))
boletin['media'] = float(input(f'Media de {boletin["nome"]}: '))
if boletin['media'] >= 7:
    boletin['Situação'] = 'Aprovado'
elif boletin['media'] > 5 and boletin['media'] < 7:
    boletin['Situação'] = 'Recuperação'
else:
    boletin['situação'] = 'Reprovado'
print('-=-'*20)
for c,v in boletin.items():
    print(f' -> {c} é = a {v}')
print('-=-'*20)


#print(f'O {boletin.items("nome")} teve a média {boletin.items("media")} e sua situação é {boletin.items("Situação")}')
