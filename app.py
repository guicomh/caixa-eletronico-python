from tkinter import *
from tkinter import ttk
import caixa

def sacar_dinheiro():
    caixa.sacar_dinheiro()

def depositar_dinherio():
    caixa.depositar_saldo()


janela = Tk()

janela.resizable(False, False)
janela.title('Caixa Eletronico')
janela.geometry("800x600")

botao_sacar = Button(janela, text="Sacar", command=sacar_dinheiro) . pack()

botao_depositar = Button(janela, text="Depostitar", command=depositar_dinherio) . pack()
janela.mainloop()