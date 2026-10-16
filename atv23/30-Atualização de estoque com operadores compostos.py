'''
Uma loja possui 100 unidades de um produto. Durante o expediente, recebe 20
unidades de reposição, vende 15 unidades e, posteriormente, identifica mais 5
unidades disponíveis em outro depósito. O sistema deve atualizar o estoque a
cada movimentação.
• Operadores originais: estoque = estoque + valor e estoque = estoque - valor
• Operadores equivalentes: estoque += valor e estoque -= valor
• Tarefa: implemente as três movimentações nas duas versões, exibindo o
estoque após cada uma.
• Desafio adicional: ao final, verifique se o estoque é superior a 100 unidades
e apresente uma mensagem correspondente.
'''

# Solução 1: atualiza o estoque com atribuições completas.
estoque = 100
print(f"Solução 1 - estoque inicial: {estoque} unidades.")
estoque = estoque + 20
print(f"Após reposição: {estoque} unidades.")
estoque = estoque - 15
print(f"Após venda: {estoque} unidades.")
estoque = estoque + 5
print(f"Após localizar unidades: {estoque} unidades.")
print(f"Estoque superior a 100? {estoque > 100}")

# Solução 2: += e -= aplicam as mesmas movimentações de forma abreviada.
estoque_abreviado = 100
estoque_abreviado += 20
print(f"\nSolução 2 - após reposição: {estoque_abreviado} unidades.")
estoque_abreviado -= 15
print(f"Após venda: {estoque_abreviado} unidades.")
estoque_abreviado += 5
print(f"Após localizar unidades: {estoque_abreviado} unidades.")
if estoque_abreviado > 100:
    print("O estoque final é superior a 100 unidades.")
else:
    print("O estoque final não é superior a 100 unidades.")
