import tkinter as tk
from tkinter import messagebox

saldo_inicial = 500.00

# Função para sacar dinheiro
def sacar_dinheiro():
    global saldo_inicial
    
    # Verifica se há saldo suficiente para o saque
    if saldo_inicial <= 0:
        messagebox.showerror("Erro", "Saldo insuficiente")
        return
    
    # Exibe o saldo antes do saque
    messagebox.showinfo("Saldo", f"Saldo antes do saque: {saldo_inicial} R$")
    
    # Captura o valor do saque
    saque = float(input("Quanto você quer sacar? > "))
    
    # Verifica se o valor do saque é maior do que o saldo
    if saque > saldo_inicial:
        messagebox.showerror("Erro", "Saldo insuficiente")
        return

    # Calcula o novo saldo após o saque
    saldo_inicial -= saque
    
    # Exibe o saldo após o saque
    messagebox.showinfo("Saldo", f"Saldo após o saque: {saldo_inicial} R$")

# Função para depositar dinheiro
def depositar_saldo():
    global saldo_inicial
    
    # Exibe o saldo antes do depósito
    messagebox.showinfo("Saldo", f"Saldo antes do depósito: {saldo_inicial} R$")
    
    # Captura o valor do depósito
    deposito = float(input("Quanto você quer depositar? > "))
    
    # Calcula o novo saldo após o depósito
    saldo_inicial += deposito
    
    # Exibe o saldo após o depósito
    messagebox.showinfo("Saldo", f"Saldo após o depósito: {saldo_inicial} R$")

# Cria a interface gráfica com Tkinter
def criar_interface():
    root = tk.Tk()
    root.title("ATM")
    
    # Cria botão para saque
    btn_sacar = tk.Button(root, text="Sacar", command=sacar_dinheiro)
    btn_sacar.pack(pady=10)
    
    # Cria botão para depósito
    btn_depositar = tk.Button(root, text="Depositar", command=depositar_saldo)
    btn_depositar.pack(pady=10)
    
    # Inicia o loop principal da interface gráfica
    root.mainloop()

# Inicia a interface
criar_interface()