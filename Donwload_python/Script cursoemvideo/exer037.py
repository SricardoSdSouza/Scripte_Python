'''Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base da conversão:
-1 para binário
-2 para octal
-3 para hexadecimal.'''

'''num = int(input('Digite um Nº qualquer em decimal: '))
n_binario = bin(num)
n_octal = oct(num)
n_hexadecimal = hex(num)
print('O Número decimal {} em Binário é \033[31m{}\033[m'.format(num,n_binario))
print('O Número decimal {} em Octal é \033[32m{}\033[m'.format(num,n_octal))
print('O Número decimal {} em Hexadecimal é \033[33m{}\033m'.format(num,n_hexadecimal))
# Tirando os operadores de identificação fica
print('O Número decimal {} em Binário é \033[31m{}\033[m'.format(num,n_binario[2:]))
print('O Número decimal {} em Octal é \033[32m{}\033[m'.format(num,n_octal[2:]))
print('O Número decimal {} em Hexadecimal é \033[33m{}\033m'.format(num,n_hexadecimal[2:]))'''
# Resolução do Guanabara
num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
opcao = int(input('Sua opção : '))
if opcao == 1:
    print('O número {} convertido para BINÁRIO é igual a {}'.format(num,bin(num)[2:]))
elif opcao == 2:
    print('O número {} convertido para OCTAL é igual a {}'.format(num,oct(num)[2:]))
elif opcao == 3:
    print('O número {} convertido em EXADECIMAL é igual a {}'.format(num,hex(num)[2:]))
else:
    print('Opção inválida, tente novamente.')

