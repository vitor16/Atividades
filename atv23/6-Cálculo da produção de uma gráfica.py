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


total = 35

print("Seu total de etiquetas é: ",total)

total *= 4

print("método 1(total *= 4):  ",total)

total /= 4
total = total * 4
print("método 2(total = total * 4):  ", total)

