def opcoes():
    menu= """
    Escolha a opção:
        [1] Depósito
        [2] Saque
        [3] Extrato
        [4] Cadastrar Usuário
        [5] Listar Contas
        [6] Criar Conta 
        [7] Pesquisar Cliente
        [8] Sair
    => """
    return input(menu)

def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R${valor:.2f}\n"
        print(f"O saldo agora é: R${saldo:.2f}")
    else:
        print("Valor digitado inválido")
    return saldo, extrato

def saque(*, saldo, valor, extrato, limite, numero_de_saques, limite_saque):
    
    if valor > saldo:
        print("Saldo insuficiente")
    elif valor > limite:
        print("Ultrapassou o limite permitido")
    elif numero_de_saques >= limite_saque:
        print("O limite de saques diários já foi atingido")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R${valor:.2f}\n"
        numero_de_saques += 1
        print(f"O saldo agora é: R${saldo:.2f}")
    else:
        print("Valor digitado inválido")
    return saldo, extrato,numero_de_saques

def mostar_extrato(saldo, /, *, extrato):
    print(" EXTRATO ".center(28, "#"))
    print("Não tivemos movimentações" if not extrato else extrato)
    print(f"Saldo: R${saldo:.2f}")
    print("".center(28, "#"))

def verificar_usuario(cpf, usuarios):
    verifica = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return verifica[0] if verifica else None

def cadastrar_usuario(usuarios):
    cpf = input("Digite o CPF: ")
    cliente = verificar_usuario(cpf, usuarios)
    if cliente:
        print("CPF já cadastrado")
        return
    
    nome = input("Digite o nome: ")
    data_nasc = input("Digite a data de nascimento: ")
    endereco = input("Digite seu logradouro, bairro e a sigla da cidade: ")
    
    usuarios.append({'cpf': cpf, 'nome': nome, 'nascimento': data_nasc, 'endereco': endereco})
    print(f"Bem-vindo(a), Sr.(a) {nome}!")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite o CPF: ")
    cliente = verificar_usuario(cpf, usuarios)
    if cliente:
        print("CPF encontrado")
        print("Conta criada com sucesso!")
        return({'agencia': agencia, 'numero da conta': numero_conta, 'usuario': cliente})
    else:
        print("Cliente não encontrado")

def listar_contas(contas):
    for conta in contas:
        print(f"""
Agência: {conta['agencia']}
Conta: {conta['numero da conta']}
Nome: {conta['usuario']['nome']}
""")

def buscar_cliente(usuarios):
    cpf = input("Digite o CPF do cliente: ")
    cliente = verificar_usuario(cpf, usuarios)
    if cliente:
        print("Cliente encontrado!")
        print(f"""
Nome: {cliente['nome']}
Data de nascimento: {cliente['nascimento']}
Endereço: {cliente['endereco']}
""")
    else:
        print("Cliente não encontrado")

def main():
    saldo = 0
    limite_saque = 500
    extrato = ""
    LIMITE_SAQUE = 3
    numero_de_saques = 0
    AGENCIA = "0001"
    usuarios = []
    contas = []

    while True:
        opcao = opcoes()

        if opcao == '1':
            valor = int(input("Digite o valor a ser depositado: "))
            saldo, extrato = deposito(saldo, valor, extrato)
        elif opcao == '2':
            valor = int(input("Digite o valor do saque: "))
            saldo, extrato,numero_de_saques = saque(saldo=saldo, valor=valor, extrato=extrato, limite=limite_saque, numero_de_saques=numero_de_saques, limite_saque=LIMITE_SAQUE)
        elif opcao == '3':
            mostar_extrato(saldo, extrato=extrato)
        elif opcao == '4':
            cadastrar_usuario(usuarios)
        elif opcao == '5':
            listar_contas(contas)
        elif opcao == '6':
            numero_conta = len(contas) + 1
            conta_cliente=criar_conta(AGENCIA, numero_conta, usuarios)
            contas.append(conta_cliente)
        elif opcao == '7':
            buscar_cliente(usuarios)
        elif opcao == '8':
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida!")
            
            
main()
