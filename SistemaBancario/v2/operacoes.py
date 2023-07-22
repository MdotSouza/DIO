#FUNÇÃO PARA OPERAÇÃO DE DEPÓSITO
def depositar(saldo, valor, extrato, /):
    saldo_atual, extrato_atual = saldo, extrato
    
    if valor == "erro":
        print("Entrada inválida.")
    elif valor < 0.0:
        print("O valor não pode ser negativo.")
    else:
        saldo+= valor
        extrato+= f"DEPÓSITO(+)\tR${valor:.2f}\n"
        print("Valor depositado!")
        
        return saldo, extrato
    
    return saldo_atual, extrato_atual

#FUNÇÃO PARA OPERAÇÃO DE SAQUE
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    saldo_atual, extrato_atual, numero_saques_atual = saldo, extrato, numero_saques

    if numero_saques < limite_saques:
 
        if  valor == "erro":
            print("Entrada inválida.")
        elif valor < 0.0:
            print("O valor não pode ser negativo.")
        elif valor > limite:
            print("Valor não permitido.")
        elif valor > saldo:
            print("Saldo inferior.")
        else:
            saldo-= valor
            extrato+= f"SAQUE(-)\tR${valor:.2f}\n"
            print("Saque executado!")
            numero_saques+= 1
            return saldo, extrato, numero_saques
    else:
        print("Limite de saques diários ultrapassado.")
    
    return saldo_atual, extrato_atual, numero_saques_atual


#FUNÇÃO PARA OPERAÇÃO DE EXTRATO
def visualizarExtrato(saldo, /, *, extrato):
    if extrato == "":
        return "Não foram realizadas movimentações."
    else:
        return f"""
***************** EXTRATO *****************

Movimentações:
{extrato}                  

Saldo: R$ {saldo:.2f}"""