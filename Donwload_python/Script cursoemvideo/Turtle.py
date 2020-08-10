import turtle
import PySimpleGUI as sg
class Telapython:

 def _init_(self):
    #layout
    layout = [[sg.Text('Nome'),sg.input()],
    [sg.Text('idade'),sg.input()],[sg.Button('Enviar Dados')]]
    #janela
    janela = sg.Window("Dados do Usuario").layout(layout)
    #extrair dados
    self.button, self.values = janela.Read()

 def Iniciar(self):
    print (self.values)
    tela = Telapython()
    tela.Iniciar()
    galho = turtle.turtles()
    galho.left(50)
    galho.speed(150)

 def cria(i):
    if i < 10:
        return
    else:
        galho.forward(i)
        galho.left(30)
        cria(3 * i/4)
        galho.right(60)
        cria(3 * i/4)
        galho.left(30)
        galho.backward(i)


cria(100)
turtle.done()