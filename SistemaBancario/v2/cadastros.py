from auxiliares import gerarNumConta

#FUNÇÃO PARA CRIAR USUÁRIO
def criarCliente(nome, cpf, data_nascimento, endereco):
    return {"nome": nome,
            "cpf": cpf,
            "data_nascimento": data_nascimento,
            "endereco": endereco}

#FUNÇÃO PARA CRIAR CONTA
def criarConta(cliente):
    AGENCIA = "0001" 
    
    geradorID = gerarNumConta()
    conta = next(geradorID)
    
    contaCorrente = {"agencia": AGENCIA, "conta": conta, "cliente" : cliente}
    return contaCorrente

#FUNÇÃO PARA LISTAR USUARIOS
def listarClientes(lista_clientes):
    if lista_clientes: 
        retorno = "======= LISTA DE CLIENTES =======\n"
        for cliente in lista_clientes:
            retorno += f"""NOME:\t{cliente["nome"]}
CPF:\t{cliente["cpf"]}
DATA DE NASCIMENTO:\t{cliente["data_nascimento"]}
ENDEREÇO:\t{cliente["endereco"]}
=================================\n"""
    else:             
        retorno = "Lista de clientes vazia."
    return retorno

#FUNÇÃO PARA LISTAR CONTAS
def listarContas(lista_contas):
    if lista_contas: 
        retorno = "======= LISTA DE CONTAS =======\n"
        for conta in lista_contas:
            retorno += f"""AGÊNCIA:\t{conta["nome"]}
CONTA:\t{conta["agencia"]}
TITULAR:\t{conta["cliente"]["nome"]}
CPF DO TITULAR:\t{conta["cliente"]["cpf"]}
===============================\n"""
    else:             
        retorno = "Lista de contas vazia."
    return retorno