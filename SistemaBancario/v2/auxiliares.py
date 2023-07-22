#FUNÇÃO PARA MONTAR MENU
def criarMenu():
    TEXTO_MENU = """Selecione a opção:
1 - Criar Usuário
2 - Criar Conta
3 - Depósito
4 - Saque
5 - Visualizar Extrato
6 - Listar Usuários
7 - Listar Contas
0 - Sair
"""
    while (True):
        menu = input(TEXTO_MENU)
        if not set(menu).intersection("01234567"):
            print("Entrada inválida")
            print("*" * 42)
        elif int(menu) < 0: 
            print("Entrada inválida")
            print("*" * 42)
        else:
            break
    return int(menu)

#FUNÇÃO PARA VERIFICAR ENTRADA
def verificarEntrada(entrada):
    CARACTERES = ".0123456789"
    if not set(entrada).intersection(CARACTERES):
       return "erro"
    return float(entrada)

#FUNÇÃO PARA GERAR ID DE CONTA
def gerarNumConta():
    contador = 1
    while (True):
        yield contador
        contador += 1

def verificarCliente(cpf, lista_clientes):
    cliente = [cliente for cliente in lista_clientes if cliente["cpf"] == cpf]
    return cliente[0] if cliente else None