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

estoque = []


def cadastrar_produto():
    codigo = None
    while True:
        try:
            codigo = int(input("Digite o código do produto: "))
            if any(produto["codigo"] == codigo for produto in estoque):
                print("Código já cadastrado. Digite outro.")
                continue
            break
        except ValueError:
            print("Código precisa ser numérico.")

    while True:
        nome = input("Digite o nome do produto: ")
        if nome.strip() and not nome.isdigit():
            break
        print("Nome inválido. Digite um nome válido.")

    while True:
        categoria = input("Digite a categoria do produto: ")
        if categoria.strip() and not categoria.isdigit():
            break
        print("Categoria inválida. Digite um nome válido.")

    while True:
        try:
            quantidade = int(input("Digite a quantidade atual: "))
            break
        except ValueError:
            print("Quantidade precisa ser numérica.")

    while True:
        try:
            quantidade_minima = int(input("Digite a quantidade mínima: "))
            break
        except ValueError:
            print("Quantidade mínima precisa ser numérica.")

    while True:
        try:
            preco = float(input("Digite o preço do produto: "))
            break
        except ValueError:
            print("Preço precisa ser numérico.")

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


def cadastrar_estoque():
    while len(estoque) < 5:
        print("\n==== Cadastro de produto ====")
        cadastrar_produto()

    print("\nEstoque completo: 5 produtos cadastrados.")


def mostrar_estoque():
    if not estoque:
        print("Nenhum produto cadastrado.")
        return

    print("\n==== Produtos cadastrados ====")
    for produto in estoque:
        print(f"Código: {produto['codigo']}")
        print(f"Nome: {produto['nome']}")
        print(f"Categoria: {produto['categoria']}")
        print(f"Quantidade atual: {produto['quantidade']}")
        print(f"Quantidade mínima: {produto['quantidade_minima']}")
        print(f"Preço: R$ {produto['preco']:.2f}")
        print("-" * 30)


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
    