'''Uma companhia de abastecimento deseja calcular o valor mensal da conta de
água conforme o consumo do imóvel.
Desenvolva um programa que solicite:
• Nome do consumidor;
• Consumo de água em metros cúbicos;
• Tipo de imóvel.
Tipos:
1 - Residencial
2 - Comercial
Para imóveis residenciais:

Consumo Tarifa
Até 10 m3 R$ 2,00 por m3
De 11 a 20 m3 R$ 3,00 por m3
Acima de 20 m3 R$ 4,50 por m3
Para imóveis comerciais:
Consumo Tarifa
Até 10 m3 R$ 3,50 por m3
De 11 a 20 m3 R$ 5,00 por m3
Acima de 20 m3 R$ 7,00 por m3
Regras adicionais:
• Acrescente uma taxa fixa de serviço de R$ 12,00;
• Se o consumo ultrapassar 30 m3, acrescente uma multa de 10%;
• Classifique o consumo como baixo, moderado ou elevado;
• Não aceite consumo negativo.
O programa deverá apresentar o consumo registrado, a tarifa utilizada, a taxa de
serviço, a multa e o valor total da conta.
Todas as propostas trabalham entrada, saída, cálculos, operadores relacionais e
lógicos, além de diferentes combinações de if, elif e else, sem exigir a criação de
funções.'''
#definir variáveis
nomeConsumidor = input("Digite o nome do consumidor: ")
consumoAgua = float(input("Digite o consumo de água em metros cúbicos: "))
tipoImovel = int(input("Digite o tipo de imóvel (1 - Residencial, 2 - Comercial): "))
#verificar se o consumo é negativo
if consumoAgua < 0:
    print("Consumo inválido. O consumo não pode ser negativo.")
    exit()
#calcular tarifa de acordo com o tipo de imóvel e o consumo
if tipoImovel == 1:
    if consumoAgua <= 10:
        tarifa = 2.00
    elif consumoAgua <= 20:
        tarifa = 3.00
    else:
        tarifa = 4.50
elif tipoImovel == 2:
    if consumoAgua <= 10:
        tarifa = 3.50
    elif consumoAgua <= 20:
        tarifa = 5.00
    else:
        tarifa = 7.00
else:
    print("Tipo de imóvel inválido.")
    exit()
#calcular valor da conta
valorConta = consumoAgua * tarifa
taxaServico = 12.00
multa = 0
if consumoAgua > 30:
    multa = valorConta * 0.10
valorTotal = valorConta + taxaServico + multa
#classificar consumo
if consumoAgua <= 10:
    classificacao = "baixo"
elif consumoAgua <= 20:
    classificacao = "moderado"
else:
    classificacao = "elevado"
#mostrar resumo da conta
print("Resumo da Conta de Água")
print("Nome do consumidor: ", nomeConsumidor)
print("Consumo registrado: ", consumoAgua, "m3")
print("Tarifa utilizada: R$", tarifa, "por m3")
print("Taxa de serviço: R$", taxaServico)
print("Multa: R$", multa)
print("Valor total da conta: R$", valorTotal)
print("Classificação do consumo: ", classificacao)      