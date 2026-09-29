'''Uma loja virtual precisa calcular o valor do frete de acordo com a região, o peso do
pedido e o tipo de entrega.
Desenvolva um programa que solicite:
• Nome do cliente;
• Valor da compra;
• Peso do pedido em quilogramas;
• Região de entrega;
• Tipo de entrega.
Regiões:
1 - Região Metropolitana
2 - Interior do estado
3 - Outro estado
Valores iniciais do frete:
Região Valor inicial
Região Metropolitana R$ 12,00
Interior do estado R$ 20,00
Outro estado R$ 35,00
Regras adicionais:
• Para pedidos acima de 5 kg, acrescente R$ 3,00 por quilograma excedente;

• Entrega expressa acrescenta 50% ao valor do frete;
• Entrega comum não possui acréscimo;
• Compras acima de R$ 500,00 recebem 20% de desconto no frete.
O programa deverá apresentar:
• Valor da compra;
• Peso do pedido;
• Região;
• Tipo de entrega;
• Valor final do frete;
• Total da compra com o frete.'''
#definir variáveis
nomeCliente = input("Digite o nome do cliente: ")
valorCompra = float(input("Digite o valor da compra: "))
pesoPedido = float(input("Digite o peso do pedido em kg: "))
#definir regiões e tipos de entrega
print("Regiões de entrega:")
print("1 - Região Metropolitana")
print("2 - Interior do estado")
print("3 - Outro estado")
regiaoEntrega = int(input("Digite a região de entrega (1, 2 ou 3): "))
print("Tipos de entrega:")
print("1 - Entrega expressa")
print("2 - Entrega comum")
tipoEntrega = int(input("Digite o tipo de entrega (1 ou 2): "))
#selecionar valor do frete de acordo com a região
if regiaoEntrega == 1:
    nomeRegiao = "Região Metropolitana"
    valorFrete = 12.00
elif regiaoEntrega == 2:
    nomeRegiao = "Interior do estado"
    valorFrete = 20.00
elif regiaoEntrega == 3:
    nomeRegiao = "Outro estado"
    valorFrete = 35.00
else:
    print("Opção de entrega inválida.")
    exit()
#selecionar tipo de entrega
if tipoEntrega == 1:
    nomeTipoEntrega = "Entrega expressa"
elif tipoEntrega == 2:
    nomeTipoEntrega = "Entrega comum"
else:
    print("Opção de entrega inválida.")
    exit()
#calcular valor do frete de acordo com o peso, tipo de entrega e valor da compra
if pesoPedido > 5:
    valorFrete == (pesoPedido - 5) * 3.00
if tipoEntrega == 1:
    valorFrete *= 1.50
if valorCompra > 500:
    valorFrete *= 0.80
#mostrar resumo da compra
print("Resumo da Compra")
print("Nome do cliente: ", nomeCliente)     
print("Valor da compra: R$", valorCompra)
print("Peso do pedido:", pesoPedido, "kg")
print("Região de entrega: ", nomeRegiao)
print("Tipo de entrega: ", nomeTipoEntrega)
print("Valor final do frete: R$", valorFrete)
#total da compra com o frete
totalCompra = valorCompra + valorFrete
print("Total da compra com o frete: R$", totalCompra)