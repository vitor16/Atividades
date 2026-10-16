'''
Durante uma conferência, o sistema compara a quantidade encontrada no depósito
com a quantidade registrada. Se os valores forem diferentes, informa que existe
uma divergência.

• Operador original: quantidade1 != quantidade2
• Operador equivalente: not (quantidade1 == quantidade2)
• Tarefa: leia as duas quantidades e informe se existe divergência.
• Desafio adicional: se houver divergência, apresente a diferença absoluta
entre as quantidades.
'''

# Solucao 1: != identifica diretamente quantidades diferentes.
quantidade1 = int(input("Quantidade encontrada no deposito: "))
quantidade2 = int(input("Quantidade registrada no sistema: "))
divergencia = quantidade1 != quantidade2
print(f"Solucao 1: existe divergencia? {divergencia}")
if divergencia:
    print(f"Diferenca entre as quantidades: {abs(quantidade1 - quantidade2)}.")

# Solucao 2: a negacao da igualdade equivale a !=.
divergencia_equivalente = not (quantidade1 == quantidade2)
print(f"Solucao 2: existe divergencia? {divergencia_equivalente}")
