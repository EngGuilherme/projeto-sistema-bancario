
def menu():
    """Função para exibir o Menu"""
    menu = """\n
    ================ MENU ================
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNova conta
    [5]\tListar contas
    [6]\tNovo usuário
    [9]\tSair
    => """

    return input(menu)


def depositar(saldo, valor, extrato, /):
    """Função para depositar um valor na conta"""
    if valor > 0:
            saldo += valor
            valor_extrato = f'{valor:.2f}'
            extrato += (f"Depósito: R$ {valor_extrato.replace('.',',')}\n")

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, limite_saque):
    """Função para sacar um valor da conta"""
    
    if limite_saque > 0:
    
        excedeu_saldo = valor > saldo
    
        excedeu_limite = valor > limite

    
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

    return saldo, extrato, limite_saque


def exibir_extrato(saldo, /, *, extrato):
    """Função para acessar o extrato da conta"""
    saldo_extrato = f'{saldo:.2f}'
        
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo_extrato.replace('.',',')}")
    print("==========================================")



def cadastrar_usuario(usuarios):
    """Função para cadastrar novos usuários"""
    cpf = input("\nDigite o seu CPF: ")
    cpf = cpf_formatado(cpf)

    if cpf.isalnum() and len(cpf) == 11:
        
        usuario = filtrar_usuario(cpf, usuarios)

        if usuario:
                print (f"""Ja existe usuario cadastrado com o CPF {cpf[:3]}.
                    {cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}""")

        else:
            nome = input("\nDigite o seu nome: ")
            data_nascimento = input("\nDigite sua data de nascimento: ")
            estado = input("\nDigite o nome do seu estado: ")
            cidade = input("\nDigite o nome da sua cidade: ")
            rua = input("\nDigite o logradouro da sua rua: ")
            numero_casa = input("\nNumero da sua residencia: ")
            bairro = input("\nDigite o nome do seu bairro: ")
            
            endereco = (f"{rua}, {numero_casa} - {bairro} - {cidade}/{estado}")
            
            usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
            
            print("=== Usuário criado com sucesso! ===")

    else:

        print("Numero de CPF invalido!")
    
def filtrar_usuario(cpf, usuarios):
    """Função para verificar se existem usuarios já cadastrados com o mesmo CPF"""
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def cpf_formatado(cpf):
    """Função para formatar o CPF sem pontos ou tracos Ex: 12345678912 """
    cpf = cpf.strip()
    cpf = cpf.replace('.','').replace('-','')
    return cpf
   
def cadastrar_conta(agencia, numero_conta, usuarios):
    """Função para cadastrar novas contas"""
    cpf = input("Informe o CPF do usuário: ")
    cpf = cpf_formatado(cpf)
    
    if cpf.isalnum() and len(cpf) == 11:
        usuario = filtrar_usuario(cpf, usuarios)

        if usuario:
            print("\n=== Conta criada com sucesso! ===")
            return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}


    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

def listar_contas(contas):
    """Função para listar as contas cadastradas"""
    if contas:
        for conta in contas:
            linha = f"""\
                Agência:\t{conta['agencia']}
                C/C:\t\t{conta['numero_conta']}
                Titular:\t{conta['usuario']['nome']}
            """
            print("=" * 100)
            print(linha)
    else:
        print("\nAinda não existem contas cadastradas.")

def main():
    """Função para inicio do programa"""

    saldo = 0
    AGENCIA = "0001"
    LIMITE = 500
    extrato = ""
    limite_saque = 3
    usuarios = []
    contas = []
    
    while True:

        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)
        

        elif opcao == "2":
            
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato, limite_saque = sacar(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=LIMITE,
            limite_saque=limite_saque,
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)
            
        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = cadastrar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        
        elif opcao == "5":
            listar_contas(contas)

        elif opcao == "6":
            cadastrar_usuario(usuarios)

        elif opcao == "9":
            break
    
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()
