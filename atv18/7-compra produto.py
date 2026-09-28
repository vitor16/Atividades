'''Crie uma função chamada calcular_total() que receba o preço de um produto e a
quantidade comprada.
A função deverá calcular o valor total da compra e retornar o resultado.
No programa principal, solicite o nome do produto, o preço e a quantidade.'''

# definir função calcular_total() que recebe o preço e a quantidade do produto e retorna o valor total da compra
def calcular_total(precoProd, quantidadeProd):
    return precoProd * quantidadeProd

nomeProd = input("Digite o nome do produto: ")
precoProd = int(input("Digite o preço do produto: "))
quantidadeProd = int(input("Digite a quantidade comprada: "))

print (f"o produto {nomeProd} custará {calcular_total(precoProd, quantidadeProd):.2f} reais")