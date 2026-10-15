'''
Cinco colegas contrataram um serviço por R$ 675,00 e decidiram dividir
igualmente a despesa. Em seguida, cada participante recebeu um desconto
individual de R$ 15,00 sobre sua parte.
• Operador original: valor = valor / divisor
• Operador equivalente: valor /= divisor
• Tarefa: calcule o valor por participante e aplique o desconto individual.
• Desafio adicional: mostre o valor antes e depois do desconto.
'''

servico = 675
c1=c2=c3=c4=c5=0

print("o serviço custa R$ ", servico)
print("mas eles quiseram pagar ele( o serviço ), separadamente")

servico /= 5
c1=c2=c3=c4=c5=servico
total = c1+c2+c3+c4+c5

print("ficou R$ ",c1," para cada")
print(" ou seja")
print("Primeiro participante: R$", c1)
print("Segundo participante: R$", c2)
print("Terceiro participante: R$", c3)
print("Quarto participante: R$", c4)
print("Quinto participante: R$", c5)
print()
print("total: ", total )

c1=c2=c3=c4=c5 = c1=c2=c3=c4=c5-15
total = c1+c2+c3+c4+c5

print()
print("ficou R$ ",c1," para cada depois do desconto de R$ 15")
print(" ou seja")
print("Primeiro participante: R$", c1)
print("Segundo participante: R$", c2)
print("Terceiro participante: R$", c3)
print("Quarto participante: R$", c4)
print("Quinto participante: R$", c5)
print()
print("total: ", total )