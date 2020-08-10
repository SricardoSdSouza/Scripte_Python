# exemplificando um while
'''cont = 1
while cont <= 10:
    print(cont,'->',end='')
    cont += 1
print('Acabou')'''
# para evitar o loop infinito usa-se o comando break
'''n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
#print('A soma vale {}'.format(s))
print(f'A soma vale {s}') # usando f strings'''
# outro exemplo
nome ='Jose'
idade = 21
salario = 987.35
print(f'O {nome} tem {idade} anos.') # funciona do python 3+
print('O {} tem {} anos.'.format(nome,idade))# funciona do python 3
print('O %s tem %d anos' % (nome,idade)) # do python 2
print(f'O {nome} tem {idade} e ganha R${salario:.2f}')
# usando formatação
print(f'O {nome:20} tem {idade} e ganha R${salario:.2f}')
print(f'O {nome:-^20} tem {idade} e ganha R${salario:.2f}')# centralizado
print(f'O {nome:->20} tem {idade} e ganha R${salario:.2f}')
print(f'O {nome:-<20} tem {idade} e ganha R${salario:.2f}')