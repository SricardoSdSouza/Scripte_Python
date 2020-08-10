'''Crie um código em python que teste se o site Pudim está acessível pelo computador usado'''
import urllib
import urllib.request
try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('Deu erro!:( , não foi possível acessar o site no momento')
else:
    print('Tudo ok, Consegui acessar o site com Sucesso!! :)')
    #print(site.read) # acessa o conteudo do site lendo html
