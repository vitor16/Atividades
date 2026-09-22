'''Um estacionamento cobra de acordo com o tempo de permanência do veículo. O
estabelecimento também oferece desconto para clientes cadastrados.
Desenvolva um programa que solicite:
• Placa do veículo;
• Quantidade de horas estacionadas;
• Se o cliente é cadastrado: S ou N.
Utilize a seguinte tabela:
Tempo de permanência Valor
Até 1 hora R$ 8,00
Acima de 1 até 3 horas R$ 15,00
Acima de 3 até 6 horas R$ 25,00
Acima de 6 horas R$ 40,00
Regras adicionais:
• Clientes cadastrados recebem 10% de desconto;
• O tempo informado deve ser maior que zero;

• Caso a opção de cadastro seja diferente de S ou N, apresente uma
mensagem de opção inválida.
O programa deverá mostrar:
• Placa do veículo;
• Tempo de permanência;
• Valor original;
• Valor do desconto;
• Valor final.'''

pLaca = input("Digite a placa do veículo: ")
hOras = float(input("Digite a quantidade de horas estacionadas: "))
cAdastrado = input("O cliente é cadastrado? (S/N): ").upper()

if hOras <= 0:
    print("O tempo informado deve ser maior que zero.")
elif hOras <= 1:
    valor_original = 8.00
elif hOras <= 3:
    valor_original = 15.00
elif hOras <= 6:
    valor_original = 25.00
else:
    valor_original = 40.00
if cAdastrado == 'S':
    desconto = valor_original * 0.10
    valor_final = valor_original - desconto
elif cAdastrado == 'N':
    desconto = 0.00
    valor_final = valor_original
else:
    print("Opção inválida para cadastro. Por favor, digite 'S' ou 'N'.")
    desconto = 0.00
    valor_final = valor_original

print("Resumo do Estacionamento")
print("Placa do veículo: ", pLaca)
print("Tempo de permanência: ", hOras, "horas")
print("Valor original: R$ ", valor_original)
print("Valor do desconto: R$ ", desconto)
print("Valor final: R$ ", valor_final)