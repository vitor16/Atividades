'''
Durante um inventário, o sistema compara a quantidade de equipamentos
registrada com a quantidade encontrada. Quando os valores forem diferentes,
deverá ser apresentada uma mensagem solicitando nova conferência.
• Operador original: quantidade_registrada != quantidade_encontrada
• Operador equivalente: not (quantidade_registrada ==
quantidade_encontrada)
• Tarefa: leia as quantidades registrada e encontrada e verifique se existe
divergência.
• Desafio adicional: quando houver diferença, calcule a diferença absoluta
entre os valores.
'''

# Solucao 1: != compara as quantidades diretamente.
quantidade_registrada = int(input("Quantidade registrada no sistema: "))
quantidade_encontrada = int(input("Quantidade encontrada no inventario: "))
divergencia = quantidade_registrada != quantidade_encontrada
print(f"Solucao 1: existe divergencia? {divergencia}")
if divergencia:
    print(
        "Diferenca absoluta: "
        f"{abs(quantidade_registrada - quantidade_encontrada)}."
    )

# Solucao 2: negar a igualdade produz o mesmo teste de divergencia.
divergencia_equivalente = not (
    quantidade_registrada == quantidade_encontrada
)
print(f"Solucao 2: existe divergencia? {divergencia_equivalente}")
