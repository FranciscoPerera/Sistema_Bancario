import os
from time import sleep
from colorama import init, Fore

# Inicializa suporte a cores no terminal
init(autoreset=True)

# ESTADO DO SISTEMA
saldo = 0
limite = 500
extrato = ""

numero_saques = 0
LIMITE_SAQUES = 3

# Limpa o terminal
def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

# Cria separador no terminal
def linha():
    print("=" * 50)

# Exibe titulo com separadores
def titulo(texto):
    linha()
    print(texto.center(50))
    linha()

# FUNÇÃO: DEPÓSITO
def depositar(valor, saldo, extrato):
    # Realiza depósito na conta e registra no extrato

    limpar_tela()
    titulo("DEPÓSITO")

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"

        print(Fore.GREEN + "\nDepósito realizado com sucesso!")
    else:
        print(Fore.RED + "\nValor inválido!")

    sleep(2)
    return saldo, extrato


# FUNÇÃO: SAQUE

def sacar(valor, saldo, extrato, limite, numero_saques, limite_saques):
    # Realiza saque respeitando regras

    limpar_tela()
    titulo("SAQUE")

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print(Fore.RED + "\nSaldo insuficiente!")
    elif excedeu_limite:
        print(Fore.RED + "\nValor acima do limite permitido!")
    elif excedeu_saques:
        print(Fore.RED + "\nLimite diário de saques atingido!")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(Fore.GREEN + "\nSaque realizado com sucesso!")
    else:
        print(Fore.RED + "\nValor inválido!")

    sleep(2)
    return saldo, extrato, numero_saques


# FUNÇÃO: EXTRATO
def mostrar_extrato(saldo, extrato):
    # Exibe todas as movimentações da conta 

    limpar_tela()
    titulo("EXTRATO")

    if not extrato:
        print(Fore.RED + "\nNenhuma movimentação encontrada.")
    else:
        print(extrato)

    linha()
    print(f"Saldo atual: R$ {saldo:.2f}")
    linha()

    input("\nPressione ENTER para voltar...")

# MENU PRINCIPAL
while True:
    limpar_tela()
    titulo("BANCO PYTHON")
    print("""
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
    """)
    linha()
    opcao = input("Escolha uma opção: ")

    # OPÇÃO: DEPÓSITO
    if opcao == "1":
        try:
            valor = float(input("Valor do depósito: "))
            saldo, extrato = depositar(valor, saldo, extrato)
        except ValueError:
            print(Fore.RED + "\nValor inválido!")
            sleep(2)

    # OPÇÃO: SAQUE
    elif opcao == "2":
        try:
            valor = float(input("Valor do saque: "))

            saldo, extrato, numero_saques = sacar(
                valor,
                saldo,
                extrato,
                limite,
                numero_saques,
                LIMITE_SAQUES
            )
        except ValueError:
            print(Fore.RED + "\nValor inválido!")
            sleep(2)

    # OPÇÃO: EXTRATO
    elif opcao == "3":
        mostrar_extrato(saldo, extrato)

    # OPÇÃO: SAIR
    elif opcao == "4":
        limpar_tela()
        linha()
        print(Fore.GREEN + "Obrigado por usar o banco!")
        linha()
        break
    
    # OPÇÃO INVÁLIDA
    else:
        print(Fore.RED + "\nOpção inválida!")
        sleep(2)