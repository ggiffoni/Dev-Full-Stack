#Calcula o IMC apresentando uma interface gráfica ao usuário.

import tkinter
from tkinter import Button, Entry, Label, messagebox, PhotoImage
import Módulo_IMC

def acao():
    print("Botão pressionado!")
    índice = Módulo_IMC.calcula_imc(peso=peso.get(), altura=altura.get())
    classificação = Módulo_IMC.classifica_imc(índice)
    msg = messagebox.showinfo("Classificação", classificação)

principal = tkinter.Tk()

#CÓDIGO DA INTERFACE:

#Logo:

imagem = PhotoImage(file="peixe.gif")
logo = Label(principal, image=imagem)
logo.image = imagem
logo.grid(row=0, column=0, rowspan=2)

#Etiqueta e caixa de entrada de altura:

etiqueta_altura = Label(principal, text="Altura: ")
etiqueta_altura.grid(row=0, column=1)

altura = Entry(principal)
altura.grid(row=0, column=2)

#Etiqueta e caixa de entrada de peso:

etiqueta_peso = Label(principal, text="Peso: ")
etiqueta_peso.grid(row=1, column=1)

peso = Entry(principal)
peso.grid(row=1, column=2)

#Botão para calcular:

botão = Button(principal, text="calcular", command=acao)
botão.grid(row=2, column=2)

#Fim do programa:

principal.mainloop()