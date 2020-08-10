'''
import math
num=int(input('Digite um número: ' ))
raiz=math.sqrt(num)
print('A raiz de {},é igual a {:.3f}'.format(num,raiz))
#arredonda para cima a função ceil
print('A raiz de {}, é igual a {}'.format(num,math.ceil(raiz)))
#arredonda para baixo a função floor
print('A Raiz de {}, é igual a {}'.format(num,math.floor(raiz)))
'''
'''
# Desta forma somente a função sqrt foi importada, não precisa declarar math
from math import sqrt
num=int(input('Digite um número: ' ))
raiz=sqrt(num)
print('A raiz de {},é igual a {:.3f}'.format(num,raiz))
'''
'''
from math import sqrt,ceil,floor
num=int(input('Digite um número: ' ))
raiz=sqrt(num)
print('A raiz de {},é igual a {:.3f}'.format(num,ceil(raiz)))
print('A raiz de {}, é igual a {:.3f}'.format(num,floor(raiz)))
'''
import random
num = random.random()
print(num)
num_1=random.randint(1,20)
print(num_1)