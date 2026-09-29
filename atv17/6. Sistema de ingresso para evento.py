'''Uma instituição realizará um evento de tecnologia e precisa calcular o valor dos
ingressos de acordo com a idade e a categoria do participante.
Desenvolva um programa que solicite:
• Nome do participante;
• Idade;
• Categoria;
• Quantidade de ingressos.
Categorias:
1 - Estudante
2 - Professor
3 - Público geral
Valores por ingresso:
Categoria Valor
Estudante R$ 20,00
Professor R$ 25,00
Público geral R$ 40,00
Regras:
• Crianças com menos de 10 anos não pagam;

• Pessoas com 60 anos ou mais recebem 50% de desconto;
• Compras de cinco ou mais ingressos recebem 10% de desconto;
• Os descontos não são acumulativos: aplique somente o maior;
• Idade e quantidade de ingressos devem ser maiores que zero.
Apresente a categoria, o valor original, o desconto e o valor final.'''

#definir variáveis
nomeParticipante = input("Digite o nome do participante: ").upper()
idade = int(input("Digite a idade do participante: "))
categoria = int(input("Digite a categoria (1 - Estudante, 2 - Professor, 3 - Público geral): "))
quantidadeIngressos = int(input("Digite a quantidade de ingressos: "))
while idade <= 0 or quantidadeIngressos <= 0:
    print("Idade e quantidade de ingressos devem ser maiores que zero.")
    idade = int(input("Digite a idade do participante: "))
    quantidadeIngressos = int(input("Digite a quantidade de ingressos: "))
#definir valor do ingresso de acordo com a categoria
if categoria == 1:
    valorIngresso = 20.00
    nomeCategoria = "Estudante"
elif categoria == 2:
    valorIngresso = 25.00
    nomeCategoria = "Professor"
elif categoria == 3:
    valorIngresso = 40.00
    nomeCategoria = "Público geral"
else:
    print("Categoria inválida.")
    exit()
#calcular valor original
valorOriginal = valorIngresso * quantidadeIngressos
#calcular desconto de acordo com a idade e quantidade de ingressos
descontoIdade = 0
descontoQuantidade = 0
if idade < 10:
    descontoIdade = valorOriginal
elif idade >= 60:
    descontoIdade = valorOriginal * 0.50
if quantidadeIngressos >= 5:
    descontoQuantidade = valorOriginal * 0.10
#aplicar o maior desconto
if descontoIdade > descontoQuantidade:
    desconto = descontoIdade
else:
    desconto = descontoQuantidade
valorFinal = valorOriginal - desconto
#mostrar resumo da compra
print("Resumo da Compra")
if nomeParticipante == "VITOR":
    print("Nome do participante: ", nomeParticipante, " (Desenvolvedor do programa)")
elif nomeParticipante == "MARCEL":
    print("Nome do participante: ", nomeParticipante, " (Professor de programação)")
else:
    print("Nome do participante: ", nomeParticipante)   
print("Idade: ", idade)
print("Categoria: ", nomeCategoria)
print("Quantidade de ingressos: ", quantidadeIngressos)
print("Valor original: R$", valorOriginal)
print("Desconto: R$", desconto)
print("Valor final: R$", valorFinal)
