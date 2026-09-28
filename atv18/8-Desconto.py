'''Crie uma função chamada calcular_desconto() que receba o valor de uma
compra.
Considere:
• Até R$ 100,00: sem desconto;
• Acima de R$ 100,00: 10% de desconto;
• Acima de R$ 500,00: 15% de desconto.
A função deverá calcular e retornar o valor final da compra.'''
#definindo a função calcular_desconto
def calcular_desconto(compra):
    if compra <= 100:
        return compra
    elif compra > 100 and compra <= 500:
        return compra * 0.10
    elif compra > 500:
        return compra * 0.15

compra = float(input("Digite o valor da compra: "))

valorFinal = compra - calcular_desconto(compra) 

print(f"O valor final da compra com desconto é: R$ {valorFinal:.2f}")

