'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos),
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''
palavras = ('carro','lampada','caneta','amor','python',
            'casa','banana','amora','ioio','capivara')
print('-=-'*10)
for palavra in palavras:
    print(f'\nNa palavra \033[34m{palavra.upper()}\033[m temos: ',end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra,end=' ')

