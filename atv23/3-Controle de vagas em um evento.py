'''
Um evento disponibilizou 15 vagas e recebeu quatro inscrições confirmadas.
Cada confirmação diminui em uma unidade a quantidade de vagas disponíveis.
• Solução 1: use vagas = vagas - 1.
• Solução 2: use vagas -= 1.
• Tarefa: mostre as vagas restantes após cada confirmação e informe se ainda
há disponibilidade.
'''

# Solução 1: subtrai uma vaga com a atribuição completa.
vagas = 15
for inscricao in range(1, 5):
    vagas = vagas - 1
    print(f"Solução 1 - após a inscrição {inscricao}: {vagas} vagas.")
print(f"Solução 1 - ainda há vagas? {vagas > 0}")

# Solução 2: -= realiza a mesma subtração de forma abreviada.
vagas_abreviadas = 15
for inscricao in range(1, 5):
    vagas_abreviadas -= 1
    print(f"Solução 2 - após a inscrição {inscricao}: {vagas_abreviadas} vagas.")
print(f"Solução 2 - ainda há vagas? {vagas_abreviadas > 0}")
