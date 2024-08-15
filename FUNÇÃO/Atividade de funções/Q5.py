def cliente(nome, endereço, CPF):
    dic = {}
    print("dados salvos!")

def funcionario(nome, salario, cargo, CPF):
    print("dados salvos")

def home():
    print("-"*15)
    opcao = int(input("Digite 1 para cadastrar cliente ou 2 para cadastrar funcionario: "))
    print("-"*15)
    if opcao == 1:
        nome = input("Digite o nome do cliente: ")
        endereço = input("Digite o endereço: ")
        cpf_cliente = input("Digite o CPF: ")
        cliente(nome, endereço, cpf_cliente)
    elif opcao == 2:
        nome = input("Digite o nome do cliente: ")
        salario = input("Digite o salario: ")
        cargo = input("Digite o cargo: ")
        cpf_funcionario = input("Digite o CPF: "),
    else:
        print("Opção inválida")
        
home()
    