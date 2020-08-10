# para criar uma tupla pode ou não usar parenteses
#lanche = ('Hamburguer','pizza','Suco','Pudim')
#print(lanche)
lanche = 'Hamburguer','pizza','Suco','Pudim','batata frita' #Da no mesmo
'''print(lanche)
print(lanche[1])
print(lanche[2])
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-1:])
print(lanche[-3:])
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')
# outra forma de fazer o For
for cont in range(0,len(lanche)):
    print(lanche[cont])
print('Comi d mais!')'''
# para mostrar a posição do desejado dentro da lista
'''for cont in range(0, len(lanche)):
    print(f'Eu vou traçar {lanche[cont]} na posição {cont}')
print('Comi d mais!')'''
# funciona igual o anterior
for pos, comida in enumerate(lanche):
    print(f'Eu vou traçar {comida} na posição {pos}')
print('Comi d mais!')
# para colocar em ordem alfbética usa-se :
#lanche = ('Hamburguer','pizza','Suco','Pudim','batata frita') #Da no mesmo
#print(sorted(lanche))
'''a =(2,5,4)
b =(5,8,1,2)
c = a+b
d = b+a
print(a)
print(b)
print(c)
print(c.index(8))# mostra qual a posição que esta o 8 por ex
print(d)
print(len(c)) # ver o tamanho da variavel
print(c.count(5))# testar quantas vezes apareco o número 5 por ex
# nas tuplas podem conter dados diferentes ex
pessoa = ('Ricardo',57,'M',98.3)
print(pessoa)
# se colocar del(pessoa) a tupla será apagada'''
