#Exemplo de Interface Gráfica - Módulo tkinter.

import tkinter

def funcClicar():
    print("Botão pressionado")

janelaPrincipal = tkinter.Tk()
texto = tkinter.Label(master = janelaPrincipal, text = "Minha janela exibida")
texto.pack()

pic = tkinter.PhotoImage(file="peixe.gif")
logo = tkinter.Label(master = janelaPrincipal, image = pic)
logo.pack()

botao = tkinter.Button(master = janelaPrincipal, text = 'Clique', command = funcClicar)
botao.pack()

janelaPrincipal.mainloop()