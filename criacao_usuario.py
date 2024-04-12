    
# Criar uma função para cada regra

def menu():
    print("\n1 - Depositar")
    print("2 - Saque")
    print("3 - Extrato")
    print("4 - Criar usuario")
    print("5 - Criar conta")
    print("6 - Listar conta")
    print("7 - Sair\n")
    op = int(input())
    return op

# Deposito 
    # só valores positivos
    # todos devem ser armazenados para vizualizar no extrato
    # Fazer uma função para deposito
        # Recebe argumentos por posição (positional only)
        # retorno Saldo e extrato

def depositar(valor, saldo, extrato):
    
    if valor > 0:
        saldo += valor
        extrato += f"\nDeposito: R${valor:.2f}\n"
        print(f"\nDeposito de R${valor:.2f} realizado com sucesso.\n")
        
    
    else:
        print("\nValor inválido para depósito.\n")
    
    return saldo, extrato
    
# Saque
    # No maximo 3 saques de 500 por dia
    # Se não houver saldo, mostrar uma mensagem informando
    # todos devem ser armazenados para vizualizar no extrato
    # Fazer uma função para saque
        # Recebe argumentos por nome (keyword only)
        # Retorno Saldo e extrato    

def saque(*,sacar, saldo, limite, extrato, numero_saques, LIMITE_SAQUES):
    
    if numero_saques > LIMITE_SAQUES:
        print("\nLimite de saques excedido.\n")
        
    else:
            
        if sacar > limite:
            print("\nLimite de saque de R$500,00 excedido.\n")
            

        elif sacar > 0:
            if sacar <= saldo:
                saldo -= sacar
                extrato += f"\nSaque: R${sacar:.2f}\n"
                numero_saques += 1
                print(f"\nSaque de R${sacar:.2f} realizado com sucesso.\n")

            else:
                print("\nSaldo insuficiente.")
            
        else:
            print("\nOperação inválida, tente novamente.")
            

    return saldo, extrato, numero_saques



# Extrato
    # deve mostrar todos os movimentos
    # e no final mostrar o saldo atual
    # Fazer uma função para extrato
        # Recebe argumentos por nome e posição (keyword only e positional only)
        
def extrato_total(saldo,/,*, extrato):
    print("\n=========== Extrato ===========")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R${saldo:.2f}")
    print("==============================")


# Criar usuario(cliente do banco)
    # Deve armazenar em uma lista 
    # Composto por nome, data de nascimento, cpf e endereço(logradouro, numero - bairro - cidade/uf)
    # Deve ser armazenado apenas os numeros do CPF
    # Não podemos cadastrar 2 usuarios com o mesmo 
    
def filtrar_cpf(cpf_formatado, lista_de_clientes):
    for i in lista_de_clientes:
        if i["CPF"] == cpf_formatado:
            return i


def criar_usuario(lista_de_clientes):
    
    cpf = input("CPF: ")
    cpf_formatado = cpf.replace(".", "").replace("-", "")
    usuario = filtrar_cpf(cpf_formatado, lista_de_clientes)
    
    if usuario:
        print("\nCPF ja existente\n")
        return
    
    nome = input("Nome: ")
    data_nascimento = input("Data de nascimento (DD/MM/AAAA): ")
    endereco = input("Endereço (Rua, numero - bairro - Cidade/UF): ")
    
    lista_de_clientes.append({"Nome": nome, "Data de nascimento": data_nascimento, "CPF": cpf_formatado, "Endereço": endereco})
    
    print("\nUsuario criado com sucesso!")

# Criar conta(vincular com o usuario)
    #Deve armazenar em uma lista
    #Composto por agencia, numero da conta e usuario
    #O numero da conta e sequencial e tem que iniciar em 1
    #A agencia e fixa e é 0001
    # O usuario pode ter mais de uma conta, mais uma conta so pode ter um usuario    
    
def criar_conta(agencia, numero_conta, lista_de_clientes):
    cpf = input("CPF: ")
    cpf_formatado = cpf.replace(".", "").replace("-", "")
    cliente = filtrar_cpf(cpf_formatado, lista_de_clientes)
    
    if cliente:
        print("\nConta criada com sucesso!\n")
        return {"agencia": agencia, "numero_conta": numero_conta, "cliente": cliente}
    
    else:
        print("\nUsuario não encontrado\n")


def listar_contas(contas):
    for i in contas:
        print(f"\nAgencia: {i['agencia']}\nNumero da conta: {i['numero_conta']}\n Nome: {i['cliente']['Nome']}\n")

def logica_principal():
    
    saldo = 0
    extrato = ""
    LIMITE = 500
    AGENCIA = "0001"
    limite_saques = 3
    numero_saques = 0
    lista_de_clientes = []
    lista_contas = []
    numero_conta = 1
    
    
    while True:
        op = menu()
        
        if op == 1:
            valor =float(input("Digite o valor que deseja depositar: "))
            saldo, extrato = depositar(valor, saldo, extrato)
            
            
        elif op == 2:
            sacar = float(input("Quanto deseja sacar? "))
            saldo, extrato, numero_saques = saque(sacar=sacar,saldo=saldo, limite=LIMITE, extrato=extrato, numero_saques=numero_saques, LIMITE_SAQUES=limite_saques)
            
        elif op == 3:
            extrato_total(saldo, extrato=extrato)
            
        elif op == 4:
            
            criar_usuario(lista_de_clientes=lista_de_clientes)

        elif op == 5:
            
            conta = criar_conta(agencia=AGENCIA, numero_conta=numero_conta, lista_de_clientes=lista_de_clientes)
            
            if conta:
                lista_contas.append(conta)
                numero_conta += 1
            
        elif op == 6:
            
            listar_contas(contas=lista_contas)
            
        elif op == 7:
            break
        else:
            print("Opção inválida")
            
if __name__ == "__main__":
    logica_principal()


