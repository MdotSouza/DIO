# Importanto a função do arquivo calculadora/__init__.py
import os
import sys
sys.path.insert(0, os.getcwd())
from SistemaBancario.v1 import main_v1
from SistemaBancario.v2 import main_v2

while(True):
    #Monta menu
    menu = input("""******* SISTEMA BANCÁRIO *******
Selecione a versão do sistema:
1 - V1
2 - V2
0 - Sair
""")

    #verifica a entrada e executa a opção
    if not set(menu).intersection("012"):
        print("Entrada inválida.")
    elif int(menu) < 0:
        print("Entrada inválida")
    elif int(menu) == 1:
        main_v1()
    elif int(menu) == 2:
        main_v2()
    else:
        break

    print("*" * 42)
        