'''Uma biblioteca precisa controlar os livros disponíveis para empréstimo.
Cada livro deverá possuir:
• código;
• título;
• autor;
• ano de publicação;
• quantidade disponível.
Desenvolva um programa que:
• crie uma lista chamada livros;
• cadastre 4 livros;
• utilize append() para armazenar cada livro;

• apresente todos os livros cadastrados;
• solicite um código de livro;
• procure o livro pelo código;
• apresente suas informações caso seja encontrado.
Exemplo:
Digite o código do livro: 203

Livro encontrado.

Título: Introdução à Programação
Autor: João Silva
Ano: 2025
Quantidade disponível: 3
A busca deverá ser realizada pelo código, e não pelo título.'''
#definindo a lista de livros
livros = []
# função para cadastrar livros
def cadastrar_livro():
    #código do livro, no caso, será o identificador do livro
    #none é utilizado para inicializar a variável antes do loop, none sendo um valor
    #  nulo, para que o loop possa ser executado, variavel de tipo inteiro,
    #  para que o usuário digite um número inteiro, caso contrário, 
    # será solicitado novamente

    codigo = None
    while True:
        try:
            codigo = int(input("Digite o código do livro: "))
            if any(livro["codigo"] == codigo for livro in livros):
                print("Código já cadastrado. Digite outro.")
                continue
            break
        except ValueError:
            print("Código precisa ser numérico.")
    #mesmo processo de validação para o título, autor, 
    # ano de publicação e quantidade disponível

    while True:
        titulo = input("Digite o título do livro: ")
        if titulo.strip() and not titulo.isdigit():
            break
        print("Título inválido. Digite um título válido.")

    while True:
        autor = input("Digite o autor do livro: ")
        if autor.strip() and not autor.isdigit():
            break
        print("Autor inválido. Digite um nome válido.")

    while True:
        try:
            ano_publicacao = int(input("Digite o ano de publicação: "))
            break
        except ValueError:
            print("Ano de publicação precisa ser numérico.")

    while True:
        try:
            quantidade_disponivel = int(input("Digite a quantidade disponível: "))
            break
        except ValueError:
            print("Quantidade disponível precisa ser numérica.")
#aqui, após todas as informações serem validadas, 
# o livro é armazenado na lista de livros utilizando o método append() 
# e uma mensagem de sucesso é exibida.
    livro = {
        "codigo": codigo,
        "titulo": titulo,
        "autor": autor,
        "ano_publicacao": ano_publicacao,
        "quantidade_disponivel": quantidade_disponivel
    }
    livros.append(livro)
    print("Livro cadastrado com sucesso!")
#função para consultar um livro pelo código,
# caso o livro seja encontrado, suas informações são retornadas,
def consulta_livro(codigo):
    for livro in livros:
        if livro["codigo"] == codigo:
            return livro
    return None
#função para listar todos os livros cadastrados,
def listar_livros():
    if not livros:
        print("Nenhum livro cadastrado.")
    else:
        print("\n==== Lista de livros cadastrados ====")
        #aqui, para cada livro na lista de livros, suas informações são exibidas.
        for livro in livros:
            print(f"Código: {livro['codigo']}, Título: {livro['titulo']}, Autor: {livro['autor']}, Ano: {livro['ano_publicacao']}, Quantidade disponível: {livro['quantidade_disponivel']}")

# Loop principal do programa, onde o usuário pode escolher entre cadastrar livros, listar livros, 
# buscar um livro por código ou sair do programa.
while True:
    print("====Menu de opções====")
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Buscar livro por código")
    print("4 - Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        cadastrar_livro()
    elif opcao == "2":  
        if not livros:
            print("Nenhum livro cadastrado.")
        else:
            listar_livros()
    elif opcao == "3":
        conulta_livro = int(input("Digite o código do livro: "))
        livro_encontrado = consulta_livro(conulta_livro)
        if livro_encontrado:
            print("\nLivro encontrado.")
            print(f"Título: {livro_encontrado['titulo']}")
            print(f"Autor: {livro_encontrado['autor']}")
            print(f"Ano: {livro_encontrado['ano_publicacao']}")
            print(f"Quantidade disponível: {livro_encontrado['quantidade_disponivel']}")
        else:
            print("Livro não encontrado.")
    elif opcao == "4":
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")