'''3º Criar um escript python que leia dois numeros e tente mostrar a soma
entre eles.'''
primeiro = int(input("Digite o Primeiro número : "))
segundo = int(input("Digite o Segundo número : "))
s=primeiro+segundo

print("A soma é =",primeiro+segundo)
print('A soma é = {}'.format(s))
print('A soma entre',primeiro,'e',segundo,'é = ',s)
# outra forma de usar o format
print('A soma entre {} e {} vale {}'.format(primeiro,segundo,s))
# se usar o primeiro print não preciso da variável s
# se usar o segundo print preciso da variável s