'''
# primeiro exemplo
nome = str(input('Qual é seu nome? '))
if nome == 'Ricardo':
    print('Que nome lindo você tem :))
else:
    print('Seu nome é tão normal.')
print('Prazer em te conhecer {},bom dia'.format(nome))
'''
# segundo exemplo
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
# podemos usaar uma condição simplificada
print('PARABENS'if m >= 6 else 'ESTUDE MAIS!')
if m >= 6.0:
    print('Sua nota foi boa parabéns !!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!.')