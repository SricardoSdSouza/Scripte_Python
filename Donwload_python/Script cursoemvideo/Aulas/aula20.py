# exemplos de funções
'''def soma (x,y):
    soma = x+y
    print(soma)
soma(4,5)
soma(8,9)
soma(2,1)'''
'''a = 4
b = 5
s = a+b
print(s)
a = 8
b = 9
s = a+b
print(s)
a = 2
b = 1
s = a+b
print(s)
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')

#soma(4,5)
# posso explicitar os parâmetros
soma(a=5, b=4)
# se eu inverter ele acompanha a inversão
soma(a=4, b=5)
soma(7, 2)'''
# empacotar parâmetros
'''def contador(*num):
    for valor in num:
        print(f'{valor},', end='')
    print("FIM!")

contador(2, 1, 7)
contador(8, 0)
contador(4, 7, 6, 2)
def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números.')

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)'''
# usando listas
'''def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos +=1

valores = [6,3,9,1,0,2,]
dobra(valores)
print(valores)'''
def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')
soma(5, 2)
soma(2, 9, 4)