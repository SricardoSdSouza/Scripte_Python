'''Faça um programa que leia um número inteiro qualquer e mostre na tela sua tabuada.'''

'''
numero = int(input('Digite um Número para ver sua tabuada : '))
n=numero

print('A tabuada da multiplicação')
print('=='*20)
print('=',n,'* 1   ={:3}'.format(n*1))
print('=',n,'* 2   = ',n*2)
print('=',n,'* 3   = ',n*3)
print('=',n,'* 4   = ',n*4)
print('=',n,'* 5   = ',n*5)
print('=',n,'* 6   = ',n*6)
print('=',n,'* 7   = ',n*7)
print('=',n,'* 8   = ',n*8)
print('=',n,'* 9   = ',n*9)
print('=',n,'* 10  = ',n*10)
print('=='*20)
'''
# solução do guanabara
num=int(input('Digite um Número para ver sua tabuada : '))
print('=='*20)
print('{} x {:2} = {}'.format(num,1,num*1))
print('{} x {:2} = {}'.format(num,2,num*2))
print('{} x {:2} = {}'.format(num,3,num*3))
print('{} x {:2} = {}'.format(num,4,num*4))
print('{} x {:2} = {}'.format(num,5,num*5))
print('{} x {:2} = {}'.format(num,6,num*6))
print('{} x {:2} = {}'.format(num,7,num*7))
print('{} x {:2} = {}'.format(num,8,num*8))
print('{} x {:2} = {}'.format(num,9,num*9))
print('{} x {} = {}'.format(num,10,num*10))
print('=='*20)
