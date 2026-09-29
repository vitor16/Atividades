'''Um motorista deseja calcular o custo de uma viagem e verificar se o combustível
disponível será suficiente.
Desenvolva um programa que solicite:
• Distância total da viagem;
• Consumo médio do veículo em km/l;
• Quantidade de litros disponíveis no tanque;

• Preço do litro do combustível;
• Se a viagem inclui pedágio: S ou N.
Calcule:
litros_necessarios = distancia / consumo_medio
custo_combustivel = litros_necessarios * preco_litro
Se houver pedágio, solicite:
• Quantidade de pedágios;
• Valor médio de cada pedágio.
Depois, calcule o custo total da viagem.
O programa deverá informar:
• Quantos litros serão necessários;
• Quanto será gasto com combustível;
• Quanto será gasto com pedágios;
• Custo total da viagem;
• Se o combustível disponível é suficiente;
• Quantos litros faltarão ou sobrarão.'''
#definir variáveis
distancia = float(input("Digite a distância total da viagem em km: "))
consumoMedio = float(input("Digite o consumo médio do veículo em km/l: "))
litrosDisponiveis = float(input("Digite a quantidade de litros disponíveis no tanque: "))
precoLitro = float(input("Digite o preço do litro do combustível: "))
#calcular litros necessários e custo do combustível
litrosNecessarios = distancia / consumoMedio
custoCombustivel = litrosNecessarios * precoLitro
#verificar se há pedágio
pedagio = input("A viagem inclui pedágio? (S/N): ").upper()
if pedagio == 'S':
    quantidadePedagios = int(input("Digite a quantidade de pedágios: "))
    valorPedagio = float(input("Digite o valor médio de cada pedágio: "))
    custoPedagios = quantidadePedagios * valorPedagio
else:
    custoPedagios = 0
#calcular custo total da viagem
custoTotal = custoCombustivel + custoPedagios
#verificar se o combustível disponível é suficiente
if litrosDisponiveis >= litrosNecessarios:
    litrosSobrando = litrosDisponiveis - litrosNecessarios
    print("O combustível disponível é suficiente para a viagem.")
    print("Litros sobrando: ", litrosSobrando)
else:
    litrosFaltando = litrosNecessarios - litrosDisponiveis
    print("O combustível disponível não é suficiente para a viagem.")
    print("Litros faltando: ", litrosFaltando)
#mostrar resumo da viagem
print("Resumo da Viagem")
print("Distância total da viagem: ", distancia, "km")
print("Consumo médio do veículo: ", consumoMedio, "km/l")
print("Litros necessários: ", litrosNecessarios, "l")
print("Custo com combustível: R$", custoCombustivel)
print("Custo com pedágios: R$", custoPedagios)
print("Custo total da viagem: R$", custoTotal)