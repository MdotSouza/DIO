def main_v1():
    print("########################################")
    print("### Bem-vindo ao Sistema Bancário V1 ###")
    print("########################################")
    
    TEXTO_MENU = """Selecione a opção:
1 - Depósito
2 - Saque
3 - Extrato
0 - Sair
"""
    ERRO = "Entrada inválida"
    CARACTERES_MENU = "0123"
    CARACTERES = ".0123456789"
    TEXTO_DEP = "Digite o valor do depósito: R$"
    TEXTO_SAQ = "Digite o valor do saque: R$"
    saldo, saque, deposito = 0.0, 0.0, 0.0
    contSaques = 0
    textoExtrato = ""

    while(True):
        #Monta menu
        menu = input(TEXTO_MENU)

        #verifica a entrada
        if not set(menu).intersection(CARACTERES_MENU):
            print(ERRO)
        
        #Interrompe o processo
        elif int(menu) == 0:
            print("Encerrando programa...")
            break
        
        #Etapa de depósito
        elif int(menu) == 1:
            #Solicita valor do depósito 
            deposito = input(TEXTO_DEP).replace(",",".")
                
            #Verifica a entrada
            if not set(deposito).intersection(CARACTERES):
                print(ERRO)

            #Verifica se o valor é positivo
            elif float(deposito) < 0:
                print(ERRO)
            
            #Executa operação
            else:
                deposito = float(deposito)
                saldo+= deposito
                textoExtrato+= f"DEPÓSITO(+) .................... R${deposito:.2f}\n"
                print("Valor depositado")
        
        #Etapa de saque
        elif int(menu) == 2:
            #Solicita valor do saque 
            saque = input(TEXTO_SAQ).replace(",",".")
            
            #Verifica quantidade de saques
            if contSaques > 3:
                print("Limite de saque diário ultrapassado")

            #verifica a entrada
            elif not set(saque).intersection(CARACTERES):
                print(ERRO)

            #Verifica se o valor é positivo        
            elif float(saque) < 0.0:
                print(ERRO)

            #Verifica se o valor é permitido
            elif float(saque) > 500.0:
                print("Valor não permitido")
            
            #Verifica se existe limite para saque
            elif float(saque) > saldo:
                print("Limite ultrapassado.")
            
            #Executa operação
            else:
                saque = float(saque)
                saldo-= saque
                contSaques+= 1
                textoExtrato+= f"SAQUE(-)   ...................... R${saque:.2f}\n"
                print("Saque executado")
            
        #Etapa extrato
        elif int(menu) == 3:
            if textoExtrato == "":
                print("Não foram realizadas movimentações.")
            else:
                print(f"""
***************** EXTRATO *****************

Movimentações:
{textoExtrato}                  

Saldo: R$ {saldo:.2f}
""")
        print("*" * 42)
