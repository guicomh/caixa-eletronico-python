
saldo_inicial = 0

def sacar_dinheiro():

    saldo_inicial = 500.00

    print(f"seu saldo inicial é {saldo_inicial}")

    sacar = float(input("Quanto você quer sacar? > "))

    saldo_inicial = saldo_inicial - sacar

    print(f"você sacou {sacar} R$ e agora tem {saldo_inicial} R$")

    return 

def depositar_saldo():

    saldo_inicial = 500.00

    print(f"seu saldo atual é de {saldo_inicial} R$\n")

    depositar = float(input("Quanto você quer depositar? >"))

    saldo_inicial = saldo_inicial + depositar

    print(f"você depositou {depositar} R$ e agora tem {saldo_inicial} R$")

    return 

