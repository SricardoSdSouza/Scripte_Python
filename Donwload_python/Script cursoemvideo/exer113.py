'''Reescreva a Função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação
de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade'''
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO!: Por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! : Por facvor digite um número real.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mUsuário preferiu não digitar um número.\033[m')
            return 0
        else:
            return n


num1 = leiaInt('Digite um número Inteiro: ')
num2 = leiaFloat('Digite um número Real: ')
print(f'O valor inteiro digitado foi {num1} e o valor real digitado foi {num2}')