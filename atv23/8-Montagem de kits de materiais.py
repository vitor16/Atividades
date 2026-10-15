'''
Uma escola recebeu 53 materiais para montar kits com quatro unidades cada. O
sistema precisa calcular quantos kits completos podem ser montados e quantos
materiais sobrarão.
• Operador original: quantidade = quantidade // divisor
• Operador equivalente: quantidade //= divisor
• Tarefa: utilize a divisão inteira para calcular os kits completos e o operador
% para calcular as sobras.
• Desafio adicional: confirme se a soma dos materiais utilizados nos kits
com as sobras corresponde ao total recebido.
'''
materiais=materiais2=53
kits = materiais // 4
print("Com ",materiais," materiais é possível fazer ",kits," kits")
print("desafio:")
print("com esses materiais somados temos: ",kits*4," e sobra ",materiais2-kits*4,"pois é necessário 4 por kit")

enter = input("Aperte ENTER para continuar para o método 2(quantidade //= divisor)")

kits *=  4
kits += 1
kits //= 4

print("Com", materiais," Materiais é possível fazer ",kits," kits")
print("desafio:")
print("com esses materiais somados temos: ",kits*4," e sobra ",materiais2-kits*4,"pois é necessário 4 por kit")