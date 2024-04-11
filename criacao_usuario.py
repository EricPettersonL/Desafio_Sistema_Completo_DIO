    
# Criar uma função para cada regra
# Criar usuario(cliente do banco)
    # Deve armazenar em uma lista 
    # Composto por nome, data de nascimento, cpf e endereço(logradouro, numero - bairro - cidade/uf)
    # Deve ser armazenado apenas os numeros do CPF
    # Não podemos cadastrar 2 usuarios com o mesmo 
lista = []    
def criar_usuario():
    
    
    nome = input("Nome: ")
    data_nasc = input("Data de nascimento: ")
    cpf = input("CPF: ")
    endereco = input("Endereço: ")
    
    lista.append([nome, data_nasc, cpf, endereco])
    
    return print(lista)
    
    
if __name__ == "__main__":
    criar_usuario()


    
    

# Criar conta(vincular com o usuario)
    #Deve armazenar em uma lista
    #Composto por agencia, numero da conta e usuario
    #O numero da conta e sequencial e tem que iniciar em 1
    #A agencia e fixa e é 0001
    # O usuario pode ter mais de uma conta, mais uma conta so pode ter um usuario    