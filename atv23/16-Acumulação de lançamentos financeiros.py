'''
Um sistema financeiro registra um saldo inicial de R$ 1.200,00. Durante o dia,
recebe três lançamentos de R$ 150,00, R$ 275,00 e R$ 90,00. O saldo deve ser
atualizado após cada recebimento.
• Operador original: total = total + valor
• Operador equivalente: total += valor
• Tarefa: some os três lançamentos ao saldo inicial.
• Desafio adicional: apresente o saldo após cada lançamento e o total
acumulado ao final.
'''

# Solucao 1: soma cada lancamento com total = total + valor.
total = 1200.00
for lancamento in (150.00, 275.00, 90.00):
    total = total + lancamento
    print(f"Solucao 1 - saldo apos lancamento: R$ {total:.2f}")
print(f"Solucao 1 - saldo final: R$ {total:.2f}")

# Solucao 2: += realiza a mesma soma atualizando o saldo diretamente.
total_abreviado = 1200.00
for lancamento in (150.00, 275.00, 90.00):
    total_abreviado += lancamento
    print(f"Solucao 2 - saldo apos lancamento: R$ {total_abreviado:.2f}")
print(f"Solucao 2 - saldo final: R$ {total_abreviado:.2f}")
