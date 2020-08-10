'''Crie um programa que tenha uma função chamada fatorial() que receba dois parâmetros:
o primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico(opcional)
indicando se será mostrado ou não na tela o processo de cálculo do fatorial'''
def fatorial(num, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param num: O número a ser fatorado.
    :param show: (opicional) Mostrar ou não o calculo.
    :return: o valor do Fatorial de um número num.
    """
    cont = 1
    for c in range(num, 0, -1):
        if show:
            print(c,end='')
            if c > 1:
                print(' x ',end='')
            else:
                print(' = ',end='')
        cont *= c
    return cont

#programa principal
print(fatorial(5,show=True))
help(fatorial)