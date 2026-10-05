'''Uma empresa deseja armazenar os pedidos realizados pelos clientes.
Cada pedido deverá possuir:
• número do pedido;
• nome do cliente;
• produto;
• quantidade;
• valor unitário;
• situação.
Exemplo:
pedido = {
"numero": 1001,
"cliente": "Mariana",
"produto": "Mouse",
"quantidade": 2,
"valor_unitario": 45.00,
"situacao": "Em preparação"
}
Desenvolva um programa que:
• cadastre 5 pedidos;
• utilize uma lista para armazená-los;
• utilize append();
• calcule o valor total de cada pedido;
• apresente todos os pedidos;
• solicite o número de um pedido;
• localize o pedido pelo número;
• apresente todas as informações do pedido encontrado.
O número do pedido deverá ser utilizado como identificador.'''


#lista de pedidos
clientes = []

#função para cadastrar pedidos
def cAd_ped():
    #loop for para cadastrar 5 pedidos
    for i in range(5):
        #dicionário para armazenar as informações do pedido {}
        pedido = {}
        #como i começa em 0, adiciona-se +1 para exibir o número do pedido corretamente
        pedido["numero"] = int(input(f"Digite o número do pedido {i+1}: "))
        pedido["cliente"] = input(f"Digite o nome do cliente do pedido {i+1}: ")
        pedido["produto"] = input(f"Digite o produto do pedido {i+1}: ")
        pedido["quantidade"] = int(input(f"Digite a quantidade do produto do pedido {i+1}: "))
        pedido["valor_unitario"] = float(input(f"Digite o valor unitário do produto do pedido {i+1}: "))
        pedido["situacao"] = input(f"Digite a situação do pedido {i+1}: ")
        clientes.append(pedido)

#mostrar os pedidos cadastrados
def apresentar_ped():
    #se o pedido  estiver vazio, exibe mensagem de erro e retorna
    if not clientes:
        print("Nenhum pedido cadastrado. Cadastre os pedidos primeiro.")
        return
    print("\n=== Pedidos Cadastrados ===")
    for pedido in clientes:
        valor_total = pedido["quantidade"] * pedido["valor_unitario"]
        print(f"Número do Pedido: {pedido['numero']}, Cliente: {pedido['cliente']}, Produto: {pedido['produto']}, Quantidade: {pedido['quantidade']}, Valor Unitário: {pedido['valor_unitario']:.2f}, Valor Total: {valor_total:.2f}, Situação: {pedido['situacao']}")

#função para localizar pedido pelo número
def localizar_ped():
    #novamente, se o pedido estiver vazio, exibe mensagem de erro e retorna
    if not clientes:
        print("Nenhum pedido cadastrado. Cadastre os pedidos primeiro.")
        return
    numero_pedido = int(input("Digite o número do pedido que deseja localizar: "))
    #percorre a lista de pedidos e verifica se o número do pedido digitado pelo usuário corresponde a algum pedido cadastrado
    for pedido in clientes:
        if pedido["numero"] == numero_pedido:
            valor_total = pedido["quantidade"] * pedido["valor_unitario"]
            print(f"\n=== Pedido Localizado ===")
            print(f"Número do Pedido: {pedido['numero']}, Cliente: {pedido['cliente']}, Produto: {pedido['produto']}, Quantidade: {pedido['quantidade']}, Valor Unitário: {pedido['valor_unitario']:.2f}, Valor Total: {valor_total:.2f}, Situação: {pedido['situacao']}")
            return
    print("Pedido não encontrado.")
#loop principal
while True:
    print("\n=== Sistema de Controle de Pedidos ===")
    print("1. Cadastrar pedidos")
    print("2. Apresentar pedidos")
    print("3. Localizar pedido por número")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cAd_ped()
    elif opcao == "2":
        apresentar_ped()
    elif opcao == "3":
        localizar_ped()
    elif opcao == "4":
        print("Saindo do sistema...")
        exit()
    else:
        print("Opção inválida. Tente novamente.")