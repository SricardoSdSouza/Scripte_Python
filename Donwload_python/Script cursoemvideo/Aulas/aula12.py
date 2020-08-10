nome = str(input('Digite um nome: '))

if nome == 'Ricardo':
    print('Que nome lindo você tem!!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print ('Seu nome é bem popular no Brasil')
elif nome in 'Ana Claúdia Jéssica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal.')
print('Tem um excelente dia {}'.format(nome))