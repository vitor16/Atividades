'''Desenvolva um pequeno sistema de vendas utilizando funções.
O programa deverá apresentar o seguinte menu:
1 - Cadastrar produto
2 - Calcular subtotal
3 - Aplicar desconto
4 - Calcular pagamento
5 - Exibir resumo da compra
0 - Sair
Cada operação deverá ser desenvolvida utilizando uma função específica.
O sistema deverá permitir realizar uma compra completa, desde o cadastro do
produto até a apresentação do valor final.'''

def cadastrar_produto():
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade do produto: "))
    return {"nome": nome, "preco": preco, "quantidade": quantidade}
def calcular_subtotal(produto):
    return produto["preco"] * produto["quantidade"]
def aplicar_desconto(subtotal):
    if subtotal <= 100:
        return subtotal
    elif subtotal > 100 and subtotal <= 500:
        return subtotal * 0.90
    elif subtotal > 500:
        return subtotal * 0.85
def calcular_pagamento(valor_final):
    pagamento = float(input("Digite o valor do pagamento: "))
    troco = pagamento - valor_final
    return troco
def exibir_resumo(produto, subtotal, valor_final, troco):
    print("\nResumo da compra:")
    print(f"Produto: {produto['nome']}")
    print(f"Preço unitário: R$ {produto['preco']:.2f}")
    print(f"Quantidade: {produto['quantidade']}")
    print(f"Subtotal: R$ {subtotal:.2f}")
    print(f"Valor final com desconto: R$ {valor_final:.2f}")
    print(f"Troco: R$ {troco:.2f}")

while True:
    print("Escolha uma opção do menu:")
    print("1 - Cadastrar produto")
    print("2 - Calcular subtotal")
    print("3 - Aplicar desconto")
    print("4 - Calcular pagamento")
    print("5 - Exibir resumo da compra")
    print("0 - Sair")
    opcao = input("Digite a opção desejada: ")
    if opcao == "1":
        produto = cadastrar_produto()
    elif opcao == "2":
        subtotal = calcular_subtotal(produto)
        print(f"Subtotal: R$ {subtotal:.2f}")
    elif opcao == "3":
        valor_final = aplicar_desconto(subtotal)
        print(f"Valor final com desconto: R$ {valor_final:.2f}")
    elif opcao == "4":
        troco = calcular_pagamento(valor_final)
        print(f"Troco: R$ {troco:.2f}")
    elif opcao == "5":
        exibir_resumo(produto, subtotal, valor_final, troco)
    elif opcao == "0":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")