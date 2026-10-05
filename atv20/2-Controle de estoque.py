'''Uma empresa precisa desenvolver um pequeno sistema para controlar seu
estoque.
Para cada produto, o sistema deverá armazenar:
• código do produto;
• nome;
• categoria;
• quantidade atual;
• quantidade mínima;
• preço.
Exemplo:
produto = {
"codigo": 101,
"nome": "Teclado",
"categoria": "Periféricos",
"quantidade": 15,
"quantidade_minima": 5,
"preco": 120.00
}
Desenvolva um programa que:

• crie uma lista vazia chamada estoque;
• permita cadastrar 5 produtos;
• solicite todas as informações ao usuário;
• utilize append() para armazenar cada produto;
• percorra os produtos cadastrados;
• apresente os dados de cada produto;
• informe quais produtos estão abaixo ou iguais à quantidade mínima.
Exemplo de resultado:
PRODUTOS QUE NECESSITAM DE REPOSIÇÃO

Código: 103
Produto: Mouse
Quantidade atual: 3
Quantidade mínima: 5
O código deverá ser utilizado como identificador do produto.'''


#definir a lista de produtos
estoque = []

#função para cadastrar produtos
def cadastrar_produto():
    codigo = None
    while True:
        try:
            # Solicitar o código do produto e verificar se já existe no estoque
            codigo = int(input("Digite o código do produto: "))
            if any(produto["codigo"] == codigo for produto in estoque):
                print("Código já cadastrado. Digite outro.")
                #se o código já existir, solicitar outro código
                continue
            break
        except ValueError:
            print("Código precisa ser numérico.")
#loop para solicitar o nome do produto, garantindo que não seja vazio ou numérico
    while True:
        nome = input("Digite o nome do produto: ")
        if nome.strip() and not nome.isdigit():
            break
        print("Nome inválido. Digite um nome válido.")
#loop para solicitar a categoria do produto, garantindo que não seja vazio ou numérico
    while True:
        categoria = input("Digite a categoria do produto: ")
        if categoria.strip() and not categoria.isdigit():
            break
        print("Categoria inválida. Digite um nome válido.")
#loop para solicitar a quantidade atual do produto, garantindo que seja numérico
    while True:
        try:
            quantidade = int(input("Digite a quantidade atual: "))
            break
        except ValueError:
            print("Quantidade precisa ser numérica.")
#loop para solicitar a quantidade mínima do produto, garantindo que seja numérico
    while True:
        try:
            quantidade_minima = int(input("Digite a quantidade mínima: "))
            break
        except ValueError:
            print("Quantidade mínima precisa ser numérica.")
#loop para solicitar o preço do produto, garantindo que seja numérico
    while True:
        try:
            preco = float(input("Digite o preço do produto: "))
            break
        except ValueError:
            print("Preço precisa ser numérico.")
# Criar o dicionário do produto e adicioná-lo à lista de estoque
    produto = {
        "codigo": codigo,
        "nome": nome,
        "categoria": categoria,
        "quantidade": quantidade,
        "quantidade_minima": quantidade_minima,
        "preco": preco,
    }
    estoque.append(produto)
    print("Produto cadastrado com sucesso!")

#função para mostrar o estoque de produtos cadastrados

def mostrar_estoque():
    if not estoque:
        print("Nenhum produto cadastrado.")
        return
#descobri que \n é usado para pular uma linha, então usei ele para separar a apresentação dos produtos ao inves de print()

    print("\n==== Produtos cadastrados ====")
    for produto in estoque:
        print(f"Código: {produto['codigo']}")
        print(f"Nome: {produto['nome']}")
        print(f"Categoria: {produto['categoria']}")
        print(f"Quantidade atual: {produto['quantidade']}")
        print(f"Quantidade mínima: {produto['quantidade_minima']}")
        print(f"Preço: R$ {produto['preco']:.2f}")
        print("-" * 30)
#função para cadastrar produtos até que o estoque esteja completo (5 produtos)
def cadastrar_estoque():
    while len(estoque) < 5:
        cadastrar_produto()
        if len(estoque) < 5:
            print(f"Você cadastrou {len(estoque)} produto(s). Faltam {5 - len(estoque)} para completar o estoque.")
        else:
            print("Estoque completo. Não é possível cadastrar mais produtos.")
#função para verificar quais produtos estão abaixo ou igual à quantidade mínima
def produtos_abaixo_ou_igual_minimo():
    print("\n==== PRODUTOS QUE NECESSITAM DE REPOSIÇÃO ====\n")
    encontrado = False

    for produto in estoque:
        if produto["quantidade"] <= produto["quantidade_minima"]:
            print(f"Código: {produto['codigo']}")
            print(f"Produto: {produto['nome']}")
            print(f"Quantidade atual: {produto['quantidade']}")
            print(f"Quantidade mínima: {produto['quantidade_minima']}")
            print("-" * 30)
            encontrado = True

    if not encontrado:
        print("Nenhum produto está abaixo ou igual à quantidade mínima.")

# Loop principal do programa
while True:
    print("\n======== Menu Principal ========")
    print("1 - Cadastrar produtos")
    print("2 - Mostrar estoque")
    print("3 - Ver produtos abaixo da quantidade mínima")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        if len(estoque) >= 5:
            print("O estoque já está completo.")
        else:
            cadastrar_estoque()
    elif opcao == "2":
        mostrar_estoque()
    elif opcao == "3":
        if not estoque:
            print("Cadastre produtos antes de verificar a reposição.")
        else:
            produtos_abaixo_ou_igual_minimo()
    elif opcao == "0":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Digite uma opção do menu.")
    