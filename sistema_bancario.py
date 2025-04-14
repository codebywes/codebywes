
menu = '''

******** \033[32mMENU DE TRANSAÇÕES\033[m ********

            1 - Depositar
            2 - Sacar
            3 - Extrato
            0 - Sair

******* \033[32mSelecione a opção desejada\033[m ********

'''


saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUES = 3

while True:
    opcao = int(input(menu))

    if opcao == 1:
        valor = float(input("Digite o valor que você deseja depositar:"))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Valor inválido para depósito.")

    elif opcao == 2:
        valor = float(input("Digite o valor que deseja sacar:"))
        if valor > limite:
            print("Valor excede o limite por saque R$ 500.00 ")
        elif valor > saldo:
            print("Você não tem saldo suficiente, consulte seu saldo.")
        elif numero_saque >= LIMITE_SAQUES:
            print("Número máximo de saques atingido no dia de hoje.")
        elif valor > 0:
            saldo -= valor 
            extrato += f"Saque: RS {valor:.2f}\n"
            numero_saque += 1
            print("Saque realizado com sucesso!")
        else: 
            print("Valor inválido para saque.")
        
    elif opcao == 3:
        print("******** EXTRATO ********")
        print(extrato if extrato else "Não foram realizadas movimentações.")
        print(f"\nSaldo atual: R$ {saldo:.2f}")

    elif opcao == 0:
        print("Saindo...")
        break
    else: 
        print("opção invalida, tente novamente.")

print("\033[32mObrigado por usar nosso sistema. Até logo!\033[m")
        