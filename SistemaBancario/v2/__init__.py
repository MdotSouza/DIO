import os
import sys
sys.path.insert(0, os.getcwd())
from SistemaBancario.v2.operacoes import depositar, sacar, visualizarExtrato
from SistemaBancario.v2.auxiliares import criarMenu, verificarEntrada, verificarCliente
from SistemaBancario.v2.cadastros import criarCliente, criarConta, listarClientes, listarContas


def main_v2():
    print("########################################")
    print("### Bem-vindo ao Sistema Bancário V2 ###")
    print("########################################")

    LIMITE_SAQUES = 3
    LIMITE = 500.00

    saldo = 0.0
    extrato = ""
    numeroSaques = 0

    clientes = []
    contas = []
    
    while (True):
        opcao = criarMenu()
        
        if opcao == 0:
            print("Encerrando programa...")
            break
        
        elif opcao == 1:
            cpf = input("Informe o CPF (somente números): ").replace(".","").replace("-","")
            cliente = verificarCliente(cpf, clientes)
            if cliente:
                print("Cliente já cadastrado.")
            else:
                nome = input("Informe o nome: ")
                dataNascimento = input("Informe a data de nascimemnto(dd-mm-aaaa): ")
                endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/uf): ")
                
                clientes.append(criarCliente(nome, cpf, dataNascimento, endereco))
                print("Cliente criado com sucesso!")

        elif opcao == 2:
            cpf = input("Informe o CPF do cliente (somente números): ").replace(".","").replace("-","")
            cliente = verificarCliente(cpf, clientes)

            if not cliente:
                print("Cliente não encontrado.")
            else:
                contas.append(criarConta(cliente))
                print("Conta criada com sucesso!")
        
        elif opcao == 3:
            deposito = input("Digite o valor do depósito: R$").replace(",",".")
            deposito = verificarEntrada(deposito)
            saldo, extrato = depositar(saldo, deposito, extrato)
        
        elif opcao == 4:
            saque = input("Digite o valor do saque: R$").replace(",",".")
            saque =  verificarEntrada(saque)      
            saldo, extrato, numeroSaques = sacar(saldo= saldo,
                                                 valor= saque,
                                                 extrato= extrato,
                                                 limite= LIMITE,
                                                 numero_saques= numeroSaques,
                                                 limite_saques= LIMITE_SAQUES)
        
        elif opcao == 5:
            consulta = visualizarExtrato(saldo, extrato= extrato)
            print(consulta)
        elif opcao == 6:
            consulta = listarClientes(clientes)
            print(consulta)
        elif opcao == 7:
            consulta = listarContas(contas)
            print(consulta)
            
        print("*" * 42)