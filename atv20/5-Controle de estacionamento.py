'''Um estacionamento possui 3 fileiras com 5 vagas em cada uma.
Uma matriz será utilizada para representar as vagas:
0 = vaga livre
1 = vaga ocupada
Exemplo:
estacionamento = [
[0, 1, 0, 0, 1],
[1, 1, 0, 1, 0],
[0, 0, 1, 0, 0]
]
Desenvolva um programa que:
• crie uma matriz 3 × 5;
• solicite ao usuário a situação de cada vaga;
• utilize append() para construir a matriz;

• apresente o estacionamento;
• conte quantas vagas estão ocupadas;
• conte quantas vagas estão livres.
Ao final, apresente:
Total de vagas: 15
Vagas ocupadas: 6
Vagas livres: 9'''

estacionamento = []

def cadastrar_vagas():
    for i in range(3):
        fileira = []
        for j in range(5):
            while True:
                try:
                    vaga = int(input(f"Digite a situação da vaga ({i+1}, {j+1}) [0 = livre, 1 = ocupada]: "))
                    if vaga in [0, 1]:
                        fileira.append(vaga)
                        break
                    else:
                        print("Valor inválido. Digite 0 para livre ou 1 para ocupada.")
                except ValueError:
                    print("Valor inválido. Digite 0 para livre ou 1 para ocupada.")
        estacionamento.append(fileira)

def apresentar_estacionamento():
    if not estacionamento:
        print("Estacionamento vazio. Cadastre as vagas primeiro.")
        return
    print("\n=== Estacionamento ===")
    for i, fileira in enumerate(estacionamento):
        print(f"Fileira {i+1}: {fileira}")

def contar_vagas():
    vagas_ocupadas = sum(sum(fileira) for fileira in estacionamento)
    vagas_livres = 15 - vagas_ocupadas
    print(f"\nTotal de vagas: 15")
    print(f"Vagas ocupadas: {vagas_ocupadas}")
    print(f"Vagas livres: {vagas_livres}")

while True:
    print("\n=== Sistema de Controle de Estacionamento ===")
    print("1. Cadastrar vagas")
    print("2. Apresentar estacionamento")
    print("3. Contar vagas")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        cadastrar_vagas()
    elif opcao == "2":
        apresentar_estacionamento()
    elif opcao == "3":
        contar_vagas()
    elif opcao == "4":
        break
    else:
        print("Opção inválida. Tente novamente.")