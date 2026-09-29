'''Uma empresa deseja ajudar seus clientes a estimar o valor mensal da conta de
energia elétrica.
Desenvolva um programa que solicite:
• Nome do consumidor;
• Consumo mensal em kWh;
• Tipo de instalação.
Tipos de instalação:
R - Residencial
C - Comercial
I - Industrial
Utilize as seguintes tarifas:
Instalação Até 100 kWh Acima de 100 kWh
Residencial R$ 0,60 por kWh R$ 0,75 por kWh
Comercial R$ 0,70 por kWh R$ 0,85 por kWh
Industrial R$ 0,80 por kWh R$ 0,95 por kWh
Após calcular o consumo, acrescente:

• Taxa fixa de iluminação de R$ 15,00;
• Imposto de 12% sobre o valor do consumo.
Classifique o consumo:
• Até 100 kWh: baixo;
• De 101 a 250 kWh: moderado;
• Acima de 250 kWh: elevado.
O programa deverá apresentar o valor do consumo, o imposto, a taxa fixa, o total e
a classificação.'''
#declarar variáveis
nomeConsumidor = input("Digite o nome do consumidor: ")
consumoMensal = float(input("Digite o consumo mensal em kWh: "))
#()upper serve para transformar a letra digitada em maiúscula, independente de como o usuário digitar
tipoInstalacao = input("Digite o tipo de instalação (R - Residencial, C - Comercial, I - Industrial): ").upper()
#calcular valor do consumo de acordo com o tipo de instalação e o consumo mensal
if tipoInstalacao == "R":
    if consumoMensal <= 100:
        valorConsumo = consumoMensal * 0.60
    else:
        valorConsumo = consumoMensal * 0.75
elif tipoInstalacao == "C":
    if consumoMensal <= 100:
        valorConsumo = consumoMensal * 0.70
    else:
        valorConsumo = consumoMensal * 0.85
elif tipoInstalacao == "I":
    if consumoMensal <= 100:
        valorConsumo = consumoMensal * 0.80
    else:
        valorConsumo = consumoMensal * 0.95
else:
    print("Tipo de instalação inválido.")
    exit()
    #calcular taxa fixa, imposto e total
taxaFixa = 15.00
imposto = valorConsumo * 0.12
total = valorConsumo + taxaFixa + imposto
if consumoMensal <= 100:
    classificacao = "baixo"
elif consumoMensal <= 250:
    classificacao = "moderado"
else:
    classificacao = "elevado"
    #output dos resultados
print("Resumo da Conta de Energia")
print("Nome do consumidor: ", nomeConsumidor)
print("Consumo mensal: ", consumoMensal, "kWh")
print("Valor do consumo: R$", valorConsumo)
print("Taxa fixa de iluminação: R$", taxaFixa)
print("Imposto: R$", imposto)
print("Total a pagar: R$", total)
print("Classificação do consumo: ", classificacao)
