'''
nome = input('Qual é o eu nome ? = ')
print('Prazer em te conhecer {}!'.format(nome))
print('Prazer em te conhecer {:20}!'.format(nome))
#alinha a direita
print('Prazer em te conhecer {:>20}!'.format(nome))
#alinha a esquerda
print('Prazer em te conhecer {:<20}!'.format(nome))
#centralizado
print('Prazer em te conhecer {:^20}!'.format(nome))
print('Prazer em te conhecer {:=^20}!'.format(nome))
print('='*43)
'''
n1 = int(input('Um valor: '))
n2= int(input('Outro valor: '))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2

print('A soma vale = {} '.format(s))
print('A multiplicação vale = {} '.format(m))
print('A divisão vale ={} '.format(d))
print('O valor da divisão inteira = {}'.format(di))
print('O valor da exponenciação = {}'.format(e))
print('='*53)
print('A soma é = {} , o produto é = {} ,e a divisão é = {:.2f}'.format(s,m,d),end=' ')
print('A divisão inteira = {} = , e a potência é = {}'.format(di,e))
print('A soma é = {} , o produto é = {} ,e a divisão é = {:.2f}'.format(s,m,d))
print('A divisão inteira = {} = , e a potência é = {}'.format(di,e))