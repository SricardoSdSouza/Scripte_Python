'''Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário
com as seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)
Adicione também as doc_strings da função'''
def notas(*n, sit=False):
    """
    -> Função para analisar notas e situções de vários alunos.
    :param n: uma ou mais notas dos alunos(aceita várias)
    :param sit:Valor opcional, indicando se deve ou não adicionar a situação.
    :return:dicionário com várias informações sobre a situação da turma.
    Este codigo foi feito por @Ricardo em 23/07/2020.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'BOA :)'
        elif r['media'] >= 5:
            r['Situação'] = 'RAZOAVEL.'
        else:
            r['Situação'] = 'RUIM ! :('

    return r

# Programa principal
resp = notas(9, 10, 5.5, 2.5, 8.5, sit=True)
print(resp)
help(notas)