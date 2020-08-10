'''Adicione ao módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(),
que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui'''
from exer112.utilidadescev import moeda
from exer112.utilidadescev import dado

p = dado.leiaDinheiro('Digite o preço: R$ ')
# 20 parametro do aumento e 12 da redução podem ser alterados
moeda.resumo(p, 30, 22)