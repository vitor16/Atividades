'''Uma instituição financeira deseja realizar uma análise inicial de solicitações de
empréstimo.
Desenvolva um programa que solicite:
• Nome do cliente;
• Renda mensal;
• Valor solicitado;
• Quantidade de parcelas;
• Se o cliente possui alguma dívida em atraso: S ou N.
Calcule o valor da parcela:
valor_parcela = valor_emprestimo / quantidade_parcelas
O empréstimo será aprovado somente se:
• O cliente não possuir dívida em atraso;
• A parcela não ultrapassar 30% da renda mensal;
• O valor solicitado não ultrapassar dez vezes a renda mensal;
• A quantidade de parcelas estiver entre 1 e 48.
Caso o empréstimo seja negado, informe o principal motivo.
O programa deverá apresentar o valor solicitado, a quantidade de parcelas, o valor
de cada parcela e o resultado da análise.'''
#definir variáveis
nomeCliente = input("Digite o nome do cliente: ")
rendaMensal = float(input("Digite a renda mensal do cliente: "))
valorSolicitado = float(input("Digite o valor solicitado: "))
quantidadeParcelas = int(input("Digite a quantidade de parcelas: "))
dividaAtraso = input("O cliente possui alguma dívida em atraso? (S/N): ").upper()
minhaCasaMinhaVida = input("O empréstimo é para o Minha Casa Minha Vida? (S/N): ").upper()
#calcular valor da parcela
valorParcela = valorSolicitado / quantidadeParcelas
#verificar condições para aprovação do empréstimo
if dividaAtraso == 'S':
    resultadoAnalise = "Empréstimo negado: cliente possui dívida em atraso."
elif valorParcela > rendaMensal * 0.30:
    resultadoAnalise = "Empréstimo negado: parcela ultrapassa 30% da renda mensal."
elif minhaCasaMinhaVida == 'S' and rendaMensal > 12000:
    resultadoAnalise = "Empréstimo negado: renda acima do limite do Minha Casa Minha Vida."
elif minhaCasaMinhaVida != 'S' and valorSolicitado > rendaMensal * 10:
    resultadoAnalise = "Empréstimo negado: valor solicitado ultrapassa dez vezes a renda mensal."   
elif minhaCasaMinhaVida == 'S' and (quantidadeParcelas < 1 or quantidadeParcelas > 420):
    resultadoAnalise = "Empréstimo negado: o Minha Casa Minha Vida permite até 420 parcelas."
elif minhaCasaMinhaVida != 'S' and (quantidadeParcelas < 1 or quantidadeParcelas > 48):
    resultadoAnalise = "Empréstimo negado: quantidade de parcelas inválida."
else:
    resultadoAnalise = "Empréstimo aprovado."
#mostrar resumo da análise
print("Resumo da Análise de Empréstimo")
print("Nome do cliente: ", nomeCliente)
print("Renda mensal: R$", rendaMensal)
print("Valor solicitado: R$", valorSolicitado)
print("Quantidade de parcelas: ", quantidadeParcelas)
print("Valor de cada parcela: R$", valorParcela)
if minhaCasaMinhaVida == 'S':
    print("Modalidade: Minha Casa Minha Vida")
else:
    print("Modalidade: Empréstimo comum")
print("Resultado da análise: ", resultadoAnalise)   