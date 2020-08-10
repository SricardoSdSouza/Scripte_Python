'''Refaça o desafio 35 dos triângulos acrescentando o recurso de mostrar que tipo de triângulo será formado:
- Equilátero: Todos os lados iguais
-Isósceles: dois lados iguais
-Escaleno: Todos os lados diferentes.'''

'''print('\033[1m====\033[m'*10)
print('\033[1;34mAnalisador de Triângulos\033[m')
print('\033[1m====\033[m'*10)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triângulo!\033[32m :)\033[m.')
    if  r1 == r2 != r3 or r2 == r3 != r1 or r1 == r3 != r2:
        print('Este triangulo é \033[31m"ISÓSCELES"\033[m')
    elif r1 == r2 == r3:
        print('Este triângulo é \033[31m"EQUILÁTERO"\033[m')
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print('Este triângulo é \033[31m"ESCALENO"\033[m')
else:
    print('Os segmentos acima não podem formar um triângulo \033[31m:(\033[m.')'''
#Resolução do Guanabara
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triângulo!',end='')
    if r1 == r2 == r3:
        print('"EQUILÁTERO"')
    elif r1 != r2 != r3 != r1:
        print('"ESCALENO"')
    else:
        print('"ISÓSCELES"')
else:
    print('Os segmentos acima não podem formar um triângulo.')