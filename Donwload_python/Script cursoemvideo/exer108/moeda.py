def aumentar(preco = 0, taxa = 0):
    res = preco + (preco * taxa/100)
    return res


def diminuir(preco = 0, taxa = 0):
    res = preco - (preco * taxa/100)
    return res


def dobro(preco=0):
    res = preco * 2
    return res


def metade(preco=0):
    res = preco / 2
    return res


def moeda(preco = 0, moeda = 'R$'):
    """
    -> Função que troca o ponto pela virgula
    :param preco: unidade em reais
    :param moeda: parâmetro que será convertido em R$00,00
    :return: devolve formatado o preço passado
    """
    return f'{moeda}{preco:>6.2f}'.replace('.',',')
