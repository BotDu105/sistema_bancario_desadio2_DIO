import textwrap

def menu():
    menu = """\n
    ======= Menu =======

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Criar Usuário
    [5] Criar Conta
    [6] Listar Contas
    [0] Sair

    ====================

    => """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    if  valor <= 0:
            print("Valor inválido! Por favor tente novamente.")
        
    elif valor >= 1:
        saldo += valor
        extrato += f"\nDepósito: R$ {valor:.2f}\n"
        print("\nDepósito realizado com sucesso!\n\n")

    else:
            print("""\n     ### ERRO ### 
Digite um valor válido!\n""")
            
    return saldo, extrato
            

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        valor_invalido = valor <= 0
        excedeu_saques = numero_saques >= limite_saques

        if excedeu_saques:
            print(f"\nLimite de saques diarios alcançado!\n")
        
        elif excedeu_limite:
            print("\nValor de saque maior que o limite, digite outro valor!\n")
            
        elif valor_invalido:
            print("\nValor inválido! Digite um valor positivo.\n")

        elif excedeu_saldo:
            print("\n Valor maior que o saldo da disponivel!")

        else:
            saldo -= valor
            extrato += f"Saque:     R$ {valor:.2f}\n"
            numero_saques +=1
            print(f"\nSaque realizado com sucesso!\n\n")
        return saldo, extrato, numero_saques       


def exibir_extrato(saldo, /, *, extrato):
        print("\n------Extrato------")
        print("Não foram realizadas movimentações hoje.\n" if not extrato else extrato)
        print(f"Saldo atual: R${saldo:.2f}")
        print("--------------------\n\n")


def criar_usuario(usuarios):
    cpf = input("Digite seu CPF(números apenas): ")
    usuario = filtrar_usuario(cpf,usuarios)

    if usuario:
        print("\n CPF já utilizado!")
        return
    
    nome = input("Digite seu nome completo: ")
    data_nascimento = input("Digite sua data de nascimento(dd-mm-aaaa): ")
    endereco = input("Digite seu endereco (logradouro, número, bairro, cidade, sigla do estado): \n")

    usuarios.append({"nome": nome,"data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("-----Usuário cadastrado!-----")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite seu CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n -----Conta criada!-----\n")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    else:
         print("\n !!! Usuário não cadastrado,realize o cadastro !!! \n")



def listar_contas(contas):
    for conta in contas:
        linha = f"""\
Agência: {conta['agencia']}
C/C: {conta['numero_conta']}
Titular: {conta['usuario']['nome']}"""
        print("=" * 50)
        print(linha)


def main():
    valor = 0
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            print("\n---Depósito---\n")
            valor = float(input("Digite o valor que deseja depositar: R$"))
            saldo, extrato = depositar(saldo, valor, extrato)
            
        elif opcao == "2":
            print("\n---Saque---\n")
            print(f"Seu saldo é de R${valor: .2f}\n")
            valor = float(input("""Digite o valor que deseja sacar:
=> R$ """))
            saldo, extrato, numero_saques = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUES,
                )
            

        elif opcao == "3":
            exibir_extrato(saldo, extrato = extrato)
        
        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "6":
            listar_contas(contas)


        elif opcao == "0":
            print("\nSistema encerrado, tenha um ótimo dia.\n")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()
