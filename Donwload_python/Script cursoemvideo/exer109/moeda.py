def aumentar(preco=0, taxa=0, formato=False):
    """
    -> Função que retorna o valor monetario formatado
    :param preco: valor a ser formatado
    :param taxa: percentual a ser adicionado
    :param formato: formata a moeda
    :return: se falso não formata se true formata
    """
    res = preco + (preco * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa/100)
    return res if formato is False else moeda(res)


def dobro(preco=0, formato=False):
    res = preco * 2
    return res if not formato else moeda(res)


def metade(preco=0, formato=False):
    res = preco / 2
    return res if not formato else moeda(res)


def moeda(preco = 0, moeda = 'R$'):
    """
    -> Função que troca o ponto pela virgula
    :param preco: unidade em reais
    :param moeda: parâmetro que será convertido em R$00,00
    :return: devolve formatado o preço passado
    """
    return f'{moeda}{preco:>6.2f}'.replace('.',',')
