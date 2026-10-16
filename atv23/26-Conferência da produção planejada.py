'''
Um sistema de controle de qualidade verifica se a quantidade produzida
corresponde à quantidade planejada. Se os valores forem iguais, a produção está
de acordo com o planejamento; caso contrário, será necessário verificar a
diferença.
• Operador original: produzido == planejado
• Operador equivalente: not (produzido != planejado)
• Tarefa: leia as quantidades planejada e produzida e informe se os valores
são iguais.
• Desafio adicional: quando forem diferentes, informe se a produção ficou
acima ou abaixo do planejado.
'''

# Solução 1: == verifica diretamente se as quantidades são iguais.
planejado = int(input("Quantidade planejada: "))
produzido = int(input("Quantidade produzida: "))
producao_igual = produzido == planejado
print(f"Solução 1: a produção corresponde ao planejado? {producao_igual}")

# Solução 2: negar a desigualdade equivale a comparar com ==.
producao_equivalente = not (produzido != planejado)
print(f"Solução 2: a produção corresponde ao planejado? {producao_equivalente}")

# Se os totais forem diferentes, indica o sentido da diferença.
if produzido > planejado:
    print(f"Produção acima do planejado em {produzido - planejado} unidades.")
elif produzido < planejado:
    print(f"Produção abaixo do planejado em {planejado - produzido} unidades.")
else:
    print("A produção ficou exatamente conforme o planejado.")
