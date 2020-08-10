def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO!\"{entrada}\" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)


def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor

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


# programa principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')