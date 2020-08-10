'''Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo'''

print('==#=='*15)
print('\033[1;34mAnalisador de Triângulos\033[m')
print('==#=='*15)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triângulo!\033[32m :)\033[m.')
else:
    print('Os segmentos acima não podem formar um triângulo \033[31m:(\033[m.')