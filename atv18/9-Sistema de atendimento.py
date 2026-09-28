'''Desenvolva um programa para uma empresa que possua o seguinte menu:
1 - Cadastrar cliente
2 - Consultar cliente
3 - Calcular compra
4 - Sair
Crie uma função para executar cada uma das operações do sistema.
O programa deverá permanecer apresentando o menu até que o usuário escolha a
opção de saída.'''
#definindo as funções para cada operação do sistema
def cadastrar_cliente():
    nome = input("Digite o nome do cliente: ")
    cpf = input("Digite o CPF do cliente: ")
    print(f"Cliente {nome} com CPF {cpf} cadastrado com sucesso!")
def consultar_cliente():
    cpf = input("Digite o CPF do cliente que deseja consultar: ")
    print(f"Cliente com CPF {cpf} encontrado!")
def calcular_compra():
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade comprada: "))
    total = preco * quantidade
    print(f"O valor total da compra é: R$ {total:.2f}")
#programa principal
print("Bem-vindo ao sistema de atendimento da empresa!")
print("Escolha uma opção do menu:")
#loop para manter o menu ativo até que o usuário escolha sair (break) que faz while parar de executar fazendo ser False
while True:
    print("1 - Cadastrar cliente")
    print("2 - Consultar cliente")
    print("3 - Calcular compra")
    print("4 - Sair")
    opcao = input("Digite a opção desejada: ")
    if opcao == "1":
        cadastrar_cliente()
    elif opcao == "2":
        consultar_cliente()
    elif opcao == "3":
        calcular_compra()
    elif opcao == "4":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")   