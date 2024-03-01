# 
# Caixa Eletronico Python
#
#
# criado por https://github.com/guicomh

import os

x = 0

saldo_inicial = 5000.00

while x == 0:

    print("\nBanco 24 Horas\n")
    print(" 1 - SACAR ")
    print(" 2 - DEPOSITAR ")
    print(" 3 - SALDO ")
    print(" 4 - SAIR \n")
    opc = int(input("Digite a opçao desejada >_ "))
    os.system("cls")

    if (opc == 1):

        

        print(f"seu saldo atual é de {saldo_inicial} R$\n")
        sacar = float(input("Quanto você quer sacar? > "))

        saldo_inicial = saldo_inicial - sacar 

        saldo_total = saldo_inicial

        if (saldo_total < 0):

            print(f"seu saldo chegou no limite, por favor faça um deposito!")
        
        elif (saldo_total == 0):

            print(f"seu saldo é igual a {saldo_total} R$")

        else:

            print(f"você sacou {sacar} R$ e agora tem {saldo_inicial} R$")

        sair = input("\nAperte Enter para Voltar")

        os.system("cls")

    elif (opc == 2):

        

        print(f"seu saldo atual é de {saldo_inicial} R$\n")
        depositar = float(input("Quanto você quer depositar? >"))

        saldo_inicial = saldo_inicial + depositar

        print(f"você depositou {depositar} R$ e agora tem {saldo_inicial} R$")

        sair = input("\nAperte Enter para Voltar")

        os.system("cls")

    elif (opc == 3):

        

        print(f"seu saldo é {saldo_inicial} R$\n")

        sair = input("\nAperte Enter para Voltar")

        os.system("cls")

    elif (opc == 4):

        exit()

    else:

        print(" Codigo Invalido ")

        sair = input("\nAperte Enter para Voltar")

        os.system("cls")


