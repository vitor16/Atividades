'''
Uma carteira digital possui saldo inicial de R$ 500,00. O usuário realiza uma
compra de R$ 125,00 e outra de R$ 89,00. O programa deve descontar os valores e
apresentar o saldo restante após cada transação.
• Operador original: saldo = saldo - valor
• Operador equivalente: saldo -= valor
• Tarefa: inicie saldo com 500 e realize os dois descontos.

• Desafio adicional: verifique se o saldo restante seria suficiente para uma
terceira compra de R$ 200,00.
'''

# Solucao 1: atualiza o saldo escrevendo a subtracao completa.
saldo = 500.00
print(f"Saldo inicial: R$ {saldo:.2f}")
saldo = saldo - 125.00
print(f"Depois da primeira compra: R$ {saldo:.2f}")
saldo = saldo - 89.00
print(f"Depois da segunda compra: R$ {saldo:.2f}")

# Solucao 2: o operador -= faz a mesma subtracao de forma abreviada.
saldo_abreviado = 500.00
saldo_abreviado -= 125.00
print(f"\nSolucao abreviada - apos a primeira compra: R$ {saldo_abreviado:.2f}")
saldo_abreviado -= 89.00
print(f"Solucao abreviada - apos a segunda compra: R$ {saldo_abreviado:.2f}")

# O desafio verifica se ainda e possivel pagar uma terceira compra de R$ 200.
if saldo_abreviado >= 200.00:
    print(f"Saldo suficiente. Restariam R$ {saldo_abreviado - 200.00:.2f}.")
else:
    print("Saldo insuficiente para a terceira compra de R$ 200,00.")
