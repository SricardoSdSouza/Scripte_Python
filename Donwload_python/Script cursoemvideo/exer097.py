'''Faça um programa que tenha uma função chamada escreva(), que recebe um texto qualquer
como parâmetro e mostre uma mensagem com o tamanho adaptável'''
def escreva(msg):
    tam = len(msg)+4
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)

#Programa principal
escreva('Gustavo Guanabara')
escreva('oi')
escreva('Curso em video de Python')