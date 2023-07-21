#FUNÇÃO PARA CRIAR USUÁRIO
def criarUsuario(nome, dataNascimento, cpf, endereço):
    cpf = cpf.replace(".","").replace("-","")

    user = {"nome": nome,
            "dataNascimento": dataNascimento,
            "cpf": cpf,
            "endereco": endereço}
    return user

#FUNÇÃO PARA GERAR ID DE CONTA
def gerarNumConta():
    contador = 1
    while (True):
        yield contador
        contador += 1
        
#FUNÇÃO PARA CRIAR CONTA
def criarConta():
    agencia = "0001"
    
    geradorID = gerarNumConta()
    conta = next(geradorID)
    
    contaCorrente = {"agencia": agencia, "conta": conta}
    return contaCorrente


def cadastroUsuario():
    criarUsuario()

def cadastroConta():
    criarConta()