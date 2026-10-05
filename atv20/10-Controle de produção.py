'''Uma indústria precisa registrar a quantidade de produtos fabricados por
diferentes máquinas durante os dias da semana.
Considere:
• 3 máquinas;
• 5 dias de produção.
Utilize uma matriz para representar os dados.
Cada linha deverá representar uma máquina e cada coluna um dia da semana.
Exemplo:
producao = [
[120, 135, 140, 150, 145],
[100, 110, 125, 130, 128],
[150, 160, 155, 170, 180]
]
Desenvolva um programa que:
• permita informar a produção de cada máquina durante os 5 dias;
• utilize append() para construir a matriz;
• apresente a produção organizada por máquina;
• calcule o total produzido por cada máquina;
• calcule o total produzido pela indústria;
• identifique qual máquina produziu a maior quantidade durante a semana.
Ao final, apresente um relatório semelhante a:
===== PRODUÇÃO SEMANAL =====

Máquina 1: 690 unidades
Máquina 2: 593 unidades
Máquina 3: 815 unidades

Total produzido: 2098 unidades

Máquina com maior produção: Máquina 3'''


#lista para guardar valores da produção

producao = []

#função para cadastrar a produção das máquinas
def cad_prod():
    for i in range(3):
        maquina = []
        for j in range(5):
            while True:
                try:
                    prod = int(input(f"Digite a produção da máquina {i+1} no dia {j+1}: "))
                    maquina.append(prod)
                    break
                except ValueError:
                    print("\n Valor inválido. Digite um número inteiro para a produção.")
        producao.append(maquina)

#função para apresentar a produção das máquinas, percorrendo a lista de produção e exibindo seus dados

def apresentar_prod():

    #se producao estiver vazia, exibe mensagem de erro e retorna

    if not producao:
        print("Nenhuma produção cadastrada. Cadastre a produção primeiro.")
        return

    #exibe a produção cadastrada, percorrendo a lista de produção e exibindo seus dados
    print("\n=== Produção Semanal ===")
    total_industria = 0
    maior_producao = 0
    maquina_maior = 0
    for i, maquina in enumerate(producao):
        total_maquina = sum(maquina)
        total_industria += total_maquina
        print(f"Máquina {i+1}: {total_maquina} unidades")
        if total_maquina > maior_producao:
            maior_producao = total_maquina
            maquina_maior = i + 1
    print(f"\nTotal produzido: {total_industria} unidades")
    print(f"\nMáquina com maior produção: Máquina {maquina_maior}")
#loop principal
while True:
    print("\n=== Sistema de Controle de Produção ===")
    print("1. Cadastrar produção")
    print("2. Apresentar produção")
    print("3. Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        cad_prod()
    elif opcao == "2":
        apresentar_prod()
    elif opcao == "3":
        print("\n Saindo do programa.....")
        exit()
    else:
        print("\n Opção inválida. Tente novamente.")