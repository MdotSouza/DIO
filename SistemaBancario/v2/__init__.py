from auxiliares import criarMenu, listarUsuarios, listarContas
from cadastros import cadastroUsuario, cadastroConta
from operacoes import deposito, saque, extrato

def main_v2():
    print("########################################")
    print("### Bem-vindo ao Sistema Bancário V2 ###")
    print("########################################")

    saldo = 0.0
    textoExtrato = ""
    contSaques = 0
    limiteSaques = 3
    limiteSaqueIndividual = 500.00
    listarUsuarios = []
    listarContas = []
    
    while (True):
        opcao = criarMenu()
        
        if opcao == 0:
            print("Encerrando programa...")
            break
        elif opcao == 1:
            cadastroUsuario()
        elif opcao == 2:
            cadastroConta()
        elif opcao == 3:
            saldo, textoExtrato = deposito(saldo, textoExtrato)
        elif opcao == 4:
            saldo, textoExtrato, contSaques = saque(saldo_atual= saldo,
                                                    extrato_atual= textoExtrato,
                                                    limite_individual= limiteSaqueIndividual,
                                                    cont_saques= contSaques,
                                                    limite_saques= limiteSaques)
        elif opcao == 5:
            print(extrato(saldo, extrato_atual= textoExtrato))
        elif opcao == 6:
            listarContas = listarUsuarios()
        elif opcao == 7:
            listarContas = listarContas()

        print("*" * 42)

main_v2()