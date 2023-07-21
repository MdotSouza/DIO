from auxiliares import verificarEntrada

#OPERAÇÃO DEPOSITAR
def depositar(saldo, valor, extrato, /):
    saldo+= valor
    extrato+= f"DEPÓSITO(+) .................... R${valor:.2f}\n"
    print("Valor depositado!")

    return saldo, extrato

#OPERAÇÃO SACAR
def sacar(saldo, valor, extrato, numero_saques):
    saldo-= valor
    extrato+= f"SAQUE(-)   ..................... R${valor:.2f}\n"
    print("Saque executado!")
    numero_saques+= 1

    return saldo, extrato, numero_saques

#VISUALIZAR EXTRATO
def visualizarExtrato(saldo, /,  extrato):
    if extrato == "":
        return "Não foram realizadas movimentações."
    else:
        return f"""
***************** EXTRATO *****************

Movimentações:
{extrato}                  

Saldo: R$ {saldo:.2f}
"""

#FUNÇÃO PARA OPERAÇÃO DE DEPÓSITO
def deposito(saldo_atual, extrato_atual):
    deposito = input("Digite o valor do depósito: R$").replace(",",".")
    deposito = verificarEntrada(deposito)
    if deposito == "erro":
        print("Entrada inválida.")
    elif deposito < 0.0:
        print("O valor não pode ser negativo.")
    else:
        return depositar(saldo_atual, deposito, extrato_atual)
    
    return saldo_atual, extrato_atual

#FUNÇÃO PARA OPERAÇÃO DE SAQUE
def saque(saldo_atual, extrato_atual, limite_individual, cont_saques, limite_saques):
    
    if cont_saques < limite_saques:
        saque = input("Digite o valor do saque: R$").replace(",",".")
        saque =  verificarEntrada(saque)       
        if  saque == "erro":
            print("Entrada inválida.")
        elif saque < 0.0:
            print("O valor não pode ser negativo.")
        elif saque > limite_individual:
            print("Valor não permitido.")
        elif saque > saldo_atual:
            print("Saldo inferior.")
        else:
            return sacar(saldo= saldo_atual,  valor= saque, extrato= extrato_atual, numero_saques= cont_saques)
    else:
        print("Limite de saques diários ultrapassado.")
    
    return saldo_atual, extrato_atual, cont_saques

#FUNÇÃO PARA OPERAÇÃO DE EXTRATO
def extrato(saldo_atual, extrato_atual):
    return visualizarExtrato(saldo_atual, extrato= extrato_atual)