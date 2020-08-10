teste  =list()
teste.append('Gustavo')
teste.append(40)
galera = list()
#criando uma lista dentro de outra lista
#galera.append(teste)
galera.append(teste[:])
print(teste)
print(galera)
# se alterar a lista teste a lista galera acompanha
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
# a lista galera vai duplicar o que estava na lista teste, para evitar tem que fazer uma cópia
print(galera)
# criando outra estrutura
galera1 = [['João',19],['Ana',33],['Joaquin',13],['Maria',45]]
print(galera1)
# mostra tudo do índice zero
print(galera1[0])
# mostra somente o índice zero na posição zero
print(galera1[0][0])
print(galera1[2][1])
for p in galera1:
    print(p)
for p in galera1:
    print(p[0])
for p in galera1:
    print(p[1])
for p in galera1:
    print(f'{p[0]} tem {p[1]} amos de idade.')
# Criando uma lista secundaria
galera2 = list()
dado = []
totalMaior = totalMenor = 0
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera2.append(dado[:])
    dado.clear()
for p in galera2:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totalMaior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totalMenor += 1

print(f'Temos {totalMaior} maiores e {totalMenor} menores de idade.')
print(galera2)