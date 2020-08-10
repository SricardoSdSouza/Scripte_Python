'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO(A)
-Média entre 5.0 e 6.9: RECUPERAÇÃO
-Média 7.0 ou superior: APROVADO.'''

print('CALCULAR A MEDIA DO ALUNO')
print('===='*10)
n1 = float(input('Digitar a primeira nota do aluno : '))
print('____'*10)
n2 = float(input('Digitar a segunda nota do aluno : '))
print('===='*10)
media = (n1+n2)/2
print('Tirando {:.1f} e {:.1f}, a media do aluno é {:.1f}'.format(nota1,nota2,media))
if media < 5:
    print('O aluno com a média {}, foi \033[1;31;43mREPROVADO\033[m :('.format(media))
elif media >= 5 and media <= 6.9:
    print('O aluno com a média de {}, esta em \033[33mRECUPERAÇÃO!\033[m')
else:
    print('Aluno com média {}, foi \033[34mAPROVADO, PARABÉNS!!\033[m :)')
# Resolução do Guanabara
# igual a minha
