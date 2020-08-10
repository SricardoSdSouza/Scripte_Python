'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o
valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal,
 sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.'''

'''print('\033[36mOla!,seja muito bem vindo!\033[m')
v_casa = float(input('Digite o valor da casa que deja o empréstimo: R$'))
s_comprador = float(input('Digite seu salario para aprovação do emprestimo: R$ '))
anos = int(input('Em quantos anos deseja pagá-la? : '))
prestacao = v_casa/anos
n=s_comprador*30/100
if prestacao <= s_comprador * 30/100:
    print('\033[32mPara a casa no valor de R${}\033[m, sua prestação será de {:.2f}'.format(v_casa,prestacao))
else:
    print('\033[7m"NEGADO" o seu salário de R${}, não será suficiente para pagar as prestações de R${}\033[m'.format(s_comprador,prestacao))'''
# Resolução do Guanabara
casa = float(input('Valor da Casa : R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa/(anos*12)
minimo = salario *30/100
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}'.format(casa,anos,prestacao))
if prestacao <= minimo:
    print('Emprestimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')