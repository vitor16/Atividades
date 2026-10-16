'''
Cinco colegas dividem igualmente uma despesa de R$ 675,00 e cada participante
recebe um desconto individual de R$ 15,00 sobre sua parte.
• Solução 1: divida o valor total com valor = valor / divisor.
• Solução 2: use valor /= divisor.
• Tarefa: apresente o valor por pessoa antes e depois do desconto.
• Desafio adicional: mostre o total pago pelo grupo após os descontos.
'''

# Solução 1: calcula a parte de cada pessoa e subtrai o desconto.
parte = 675.00 / 5
parte_com_desconto = parte - 15.00
print(f"Solução 1 - valor por pessoa antes do desconto: R$ {parte:.2f}")
print(f"Solução 1 - valor por pessoa após o desconto: R$ {parte_com_desconto:.2f}")
print(f"Total pago pelo grupo: R$ {parte_com_desconto * 5:.2f}")

# Solução 2: divide e desconta atualizando o valor com operadores compostos.
parte_abreviada = 675.00
parte_abreviada /= 5
print(f"\nSolução 2 - valor por pessoa antes do desconto: R$ {parte_abreviada:.2f}")
parte_abreviada -= 15.00
print(f"Solução 2 - valor por pessoa após o desconto: R$ {parte_abreviada:.2f}")
print(f"Total pago pelo grupo: R$ {parte_abreviada * 5:.2f}")
