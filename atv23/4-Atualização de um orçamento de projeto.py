'''
Um projeto tem orçamento inicial de R$ 2.500,00 e recebe R$ 750,00 para
equipamentos e R$ 300,00 para materiais de consumo.
• Solução 1: use orcamento = orcamento + valor.
• Solução 2: use orcamento += valor.
• Tarefa: apresente o orçamento após cada acréscimo e o aumento total.
'''

# Solução 1: soma cada acréscimo usando a atribuição completa.
orcamento = 2500.00
print(f"Solução 1 - orçamento inicial: R$ {orcamento:.2f}")
orcamento = orcamento + 750.00
print(f"Após equipamentos: R$ {orcamento:.2f}")
orcamento = orcamento + 300.00
print(f"Após materiais: R$ {orcamento:.2f}")
print(f"Aumento total: R$ {orcamento - 2500.00:.2f}")

# Solução 2: += atualiza o orçamento somando cada acréscimo.
orcamento_abreviado = 2500.00
orcamento_abreviado += 750.00
print(f"\nSolução 2 - após equipamentos: R$ {orcamento_abreviado:.2f}")
orcamento_abreviado += 300.00
print(f"Após materiais: R$ {orcamento_abreviado:.2f}")
print(f"Aumento total: R$ {orcamento_abreviado - 2500.00:.2f}")
