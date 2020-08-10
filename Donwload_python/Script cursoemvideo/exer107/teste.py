'''Crie um módulo chamado moeda.py que tenha as funções incorporadas, aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções'''
'''import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de R$ {p} é = {moeda.metade(p)}')
print(f'O dobro de R$ {p} é = {moeda.dobro(p)}')
print(f'Aumentar 10%, temos R$ {moeda.aumentar(p, 10):.2f}')'''

''''# posso importar os itens do modulo moeda

from moeda import metade, dobro, aumentar

p = float(input('Digite o preço: R$ '))
print(f'A metade de R$ {p} é = {metade(p)}')
print(f'O dobro de R$ {p} é = {dobro(p)}')
print(f'Aumentar 10%, temos R$ {aumentar(p, 10):.2f}')'''

# outra maneira é fazer referencia a pasta de onde esta o modulo

from exer107 import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de R$ {p} é = {moeda.metade(p)}')
print(f'O dobro de R$ {p} é = {moeda.dobro(p)}')
print(f'Aumentar 10%, temos R$ {moeda.aumentar(p, 10):.2f}')