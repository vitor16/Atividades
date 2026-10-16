'''
Uma gráfica produz 35 etiquetas por lote. Para atender a uma encomenda, precisa
produzir quatro lotes e, posteriormente, duplicar a quantidade calculada para
atender a outra solicitação equivalente.
• Operador original: total = total * fator
• Operador equivalente: total *= fator
• Tarefa: inicie total com 35, multiplique por 4 e depois por 2.
• Desafio adicional: apresente o resultado após cada multiplicação e a
quantidade final.
'''


# Solucao 1: multiplicacao tradicional, total = total * fator.
total = 35
print(f"Quantidade inicial: {total} etiquetas")
total = total * 4
print(f"Depois de produzir quatro lotes: {total} etiquetas")
total = total * 2
print(f"Depois de duplicar a producao: {total} etiquetas")

# Solucao 2: *= multiplica e atualiza a variavel em uma unica operacao.
total_abreviado = 35
total_abreviado *= 4
print(f"\nSolucao abreviada - apos multiplicar por 4: {total_abreviado}")
total_abreviado *= 2
print(f"Solucao abreviada - quantidade final: {total_abreviado} etiquetas")
