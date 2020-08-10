from exer115.lib.interface import *
from exer115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'
if arquivoExiste(arq):
    print('Arquivo encontrado com sucesso!')
else:
    print('Arquivo não encontrado!')
    criarArquivo(arq)


cabeçalho('Sistema Arquivo v1.0')
while True:
    resposta = menu(['Ver Pessoas Cadastradas','Cadastrar nova Pessoas','Sair do Sistema'])
    if resposta == 1:
        #Opção de listar o conteúdo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        #Cadastrar uma nova pessoa.
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade =leiaInt('Informe a Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('\033[7mSaindo do Sistema.... até logo\033[m')
        break
    else:
        print('\033[31mERRO!: Digite uma opção válida!\033[m')
    sleep(1.5)