'''Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.'''

'''
salario=float(input('Digite o seu salário atual : R$ '))
p_aumento=float(input('digite o percentual de aumento que será dado : '))
aumento = p_aumento/100
n_salario = salario + (salario*aumento)
print('Se salario de R$ {}, deve um aumento de {:.1f}% e passou para R$ {:.2f}'.format(salario,p_aumento,n_salario))
'''
#Resolução do Guanabara
salario = float(input('Qual é o salário do funcionário? R$ '))
novo =salario + (salario * 15/100)
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R$ {:.2f}'.format(salario,novo))