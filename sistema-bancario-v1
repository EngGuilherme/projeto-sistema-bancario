menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[9] Sair

=> """

saldo = 0
LIMITE = 500
extrato = ""
limite_saque = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            valor_extrato = f'{valor:.2f}'
            extrato += (f"Depósito: R$ {valor_extrato.replace('.',',')}\n")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "2":
        if limite_saque > 0:

            valor = float(input("Informe o valor do saque: "))

            excedeu_saldo = valor > saldo

            excedeu_limite = valor > LIMITE

            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")

            elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite.")
            
            elif valor > 0:
                saldo -= valor
                saque_extrato = f'{valor:.2f}'
                extrato += (f"Saque: R$ {saque_extrato.replace('.',',')}\n")
                limite_saque -= 1

            else:
                print("Operação falhou! O valor informado é inválido.")

        else:
            print("Operação falhou! Número máximo de saques excedido.")

    elif opcao == "3":
        saldo_extrato = f'{saldo:.2f}'
        
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo_extrato.replace('.',',')}")
        print("==========================================")

    elif opcao == "9":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
