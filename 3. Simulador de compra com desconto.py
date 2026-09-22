'''Uma loja de equipamentos de informática deseja calcular automaticamente os
descontos concedidos aos clientes.
Desenvolva um programa que solicite:
• Nome do cliente;
• Nome do produto;
• Preço unitário;
• Quantidade comprada;
• Forma de pagamento.
As formas de pagamento serão:
1 - Pix
2 - Dinheiro
3 - Cartão de débito
4 - Cartão de crédito
Primeiro, calcule:
subtotal = preco_unitario * quantidade
Depois, aplique as seguintes regras:
• Pix: 10% de desconto;
• Dinheiro: 8% de desconto;
• Cartão de débito: 5% de desconto;

• Cartão de crédito: sem desconto.
No cartão de crédito:
• Permita informar a quantidade de parcelas;
• Se a compra for parcelada em até 3 vezes, não haverá juros;
• Se for parcelada em mais de 3 vezes, haverá acréscimo de 6%.
O programa deverá apresentar um comprovante com subtotal, desconto ou
acréscimo, valor final e forma de pagamento.'''

nomeCliente = input("Digite o nome do cliente: ")
nomeProduto = input("Digite o nome do produto: ")
precoUnitario = float(input("Digite o preço unitário do produto: "))
quantidadeComprada = int(input("Digite a quantidade comprada: "))
formaPagamento = input("Digite a forma de pagamento (Pix, Dinheiro, débito,crédito): ").strip().lower()
subtotal = precoUnitario * quantidadeComprada

if formaPagamento == "pix":
    desconto = subtotal * 0.10
    valorFinal = subtotal - desconto
elif formaPagamento == "dinheiro":
    desconto = subtotal * 0.08
    valorFinal = subtotal - desconto
elif formaPagamento == "debito":
    desconto = subtotal * 0.05
    valorFinal = subtotal - desconto
elif formaPagamento == "credito":
    parcelas = int(input("Digite a quantidade de parcelas: "))
    if parcelas <= 3:
        desconto = 0
        valorFinal = subtotal
    else:
        acrescimo = subtotal * 0.06
        valorFinal = subtotal + acrescimo
else:
    print("Forma de pagamento inválida.")
    desconto = 0
    valorFinal = subtotal

print("Comprovante de Compra")
print("Nome do cliente: ", nomeCliente)
print("Nome do produto: ", nomeProduto)
print("Preço unitário: R$ ", precoUnitario)
print("Quantidade comprada: ", quantidadeComprada)
print("Subtotal: R$ ", subtotal)
if formaPagamento == "credito" and parcelas > 3:
    print("Acréscimo: R$ ", acrescimo)
else:
    print("Desconto: R$ ", desconto)
print("Valor final: R$ ", valorFinal)
