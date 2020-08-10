print('Ola Mundo!')
print('\033[31mOla Mundo!')
print('\033[31;43mOla Mundo!')
print('\033[1;31;43mOla Mundo!\033[m')
print('\033[4;30;45mOla Mundo!\033[m')
print('\033[30mOla Mundo!\033[m')
print('\033[37mOla Mundo!\033[m')
print('\033[7mOla Mundo!\033[m')
print('\033[0;33;44mOla Mundo!\033[m')
print('\033[7;33;44mOla Mundo!\033[m')
a=3
b=5
print('Os valores são {} e {}'.format(a,b))
print('Os valores são \033[31m{}\033[m e {}'.format(a,b))
print('Os valores são \033[31m{}\033[m e \33[32m{} !!!'.format(a,b))
print('OS valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a,b))
nome = 'Ricardo'
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m',nome,'\033[m'))
cores = {'limpa':'\033[m',\
        'azul':'\033[34m',\
        'amarelo':'\033[33m',\
        'pretobranco':'\033[7;30m'}

print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['azul'],nome,cores['limpa']))