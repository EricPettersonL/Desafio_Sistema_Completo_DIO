# Sistema de Saque e Depósito Bancário 

Nesse segundo projeto já foram adicionadas mais regras de négocios para nosso sistema bancario do desafio de projeto do curso de Python AI Backend Developer DIO e Vivo.

## Regras de Négocios
### Deposito 
- Só valores positivos
- Todos devem ser armazenados para vizualizar no extrato
- Fazer uma função para deposito
-  Recebe argumentos por posição (positional only)
-  Retorno Saldo e extrato

### Saque
- No maximo 3 saques de 500 por dia
- Se não houver saldo, mostrar uma mensagem informando
- todos devem ser armazenados para vizualizar no extrato
- Fazer uma função para saque
- Recebe argumentos por nome (keyword only)
- Retorno Saldo e extrato 


### Extrato
- Deve mostrar todos os movimentos
- No final mostrar o saldo atual
- Fazer uma função para extrato
- Recebe argumentos por nome e posição (keyword only e positional only)

### Criar usuario(cliente do banco)
- Deve armazenar em uma lista 
- Composto por nome, data de nascimento, cpf e endereço(logradouro, numero - bairro - cidade/uf)
- Deve ser armazenado apenas os numeros do CPF
- Não podemos cadastrar 2 usuarios com o mesmo 


### Criar conta(vincular com o usuario)
- Deve armazenar em uma lista
- Composto por agencia, numero da conta e usuario
- O numero da conta e sequencial e tem que iniciar em 1
- A agencia e fixa e é 0001
- O usuario pode ter mais de uma conta, mais uma conta so pode ter um usuario    

### Execução
Para executar o programa, basta rodar o código em Python. Certifique-se de ter um ambiente Python configurado corretamente.

```bash
python desafio.py

```