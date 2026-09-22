'''Uma empresa deseja calcular o salário de seus funcionários considerando horas
trabalhadas, horas extras, benefícios e descontos.
Desenvolva um programa que solicite:
• Nome do funcionário;
• Quantidade de horas trabalhadas;
• Valor recebido por hora;
• Quantidade de horas extras;
• Se recebe vale-transporte: S ou N.
Realize os cálculos:
salario_base = horas_trabalhadas * valor_hora
valor_hora_extra = valor_hora * 1.5
total_horas_extras = horas_extras * valor_hora_extra
salario_bruto = salario_base + total_horas_extras
Desconto de INSS simplificado:
• Até R$ 1.500,00: 5%;
• De R$ 1.500,01 até R$ 3.000,00: 8%;
• Acima de R$ 3.000,00: 11%.
Outras regras:
• Se utilizar vale-transporte, desconte 6% do salário-base;
• Se não utilizar, não haverá esse desconto;
• O salário líquido será o salário bruto menos os descontos.

Apresente todos os valores em um demonstrativo de pagamento.'''
#definir variáveis
nomeFuncionario = input("Digite o nome do funcionário: ")
horasTrabalhadas = float(input("Digite a quantidade de horas trabalhadas: "))
valorHora = float(input("Digite o valor recebido por hora: "))
horasExtras = float(input("Digite a quantidade de horas extras: "))
valeTransporte = input("O funcionário recebe vale-transporte? (S/N): ").upper()
#calcular salário base
salarioBase = horasTrabalhadas * valorHora
#calcular valor da hora extra
valorHoraExtra = valorHora * 1.5
#calcular total de horas extras
totalHorasExtras = horasExtras * valorHoraExtra
#calcular salário bruto
salarioBruto = salarioBase + totalHorasExtras
#calcular desconto de INSS
if salarioBruto <= 1500:
    descontoINSS = salarioBruto * 0.05
elif salarioBruto <= 3000:
    descontoINSS = salarioBruto * 0.08
else:
    descontoINSS = salarioBruto * 0.11
#calcular desconto de vale-transporte
if valeTransporte == 'S':
    descontoValeTransporte = salarioBase * 0.06
else:
    descontoValeTransporte = 0
#calcular salário líquido
salarioLiquido = salarioBruto - descontoINSS - descontoValeTransporte
#mostrar demonstrativo de pagamento
print("Demonstrativo de Pagamento")
print("Nome do funcionário: ", nomeFuncionario)
print("Salário Base: R$ ", salarioBase)
print("Total de Horas Extras: R$ ", totalHorasExtras)
print("Salário Bruto: R$ ", salarioBruto)
print("Desconto de INSS: R$ ", descontoINSS)
print("Desconto de Vale-Transporte: R$ ", descontoValeTransporte)
print("Salário Líquido: R$ ", salarioLiquido)