'''Uma empresa possui 3 salas de reunião e precisa controlar a utilização durante 4
períodos do dia.
Considere:
0 = disponível
1 = ocupado
A matriz deverá representar:
• cada linha → uma sala;
• cada coluna → um período.
Exemplo:
salas = [
[0, 1, 0, 0],
[1, 0, 1, 0],
[0, 0, 1, 1]
]
Desenvolva um programa que:
• crie a matriz;
• permita ao usuário informar a situação de cada sala e período;
• apresente a matriz;
• solicite uma sala e um período;

• informe se o horário está disponível ou ocupado.
Também informe quantos horários estão disponíveis em cada sala.'''

salas = []

def cadastrar_salas():
    for i in range(3):
        sala = []
        for j in range(4):
            while True:
                try:
                    situacao = int(input(f"Digite a situação da sala {i+1}, período {j+1} [0 = disponível, 1 = ocupado]: "))
                    if situacao in [0, 1]:
                        sala.append(situacao)
                        break
                    else:
                        print("Valor inválido. Digite 0 para disponível ou 1 para ocupado.")
                except ValueError:
                    print("Valor inválido. Digite 0 para disponível ou 1 para ocupado.")
        salas.append(sala)

def apresentar_salas():
    if not salas:
        print("Nenhuma sala cadastrada. Cadastre as salas primeiro.")
        return
    print("\n=== Salas de Reunião ===")
    for i, sala in enumerate(salas):
        print(f"Sala {i+1}: {sala}")

def verificar_disponibilidade():
    if not salas:
        print("Nenhuma sala cadastrada. Cadastre as salas primeiro.")
        return
    while True:
        try:
            sala_num = int(input("Digite o número da sala (1-3): ")) - 1
            periodo_num = int(input("Digite o período (1-4): ")) - 1
            if 0 <= sala_num < 3 and 0 <= periodo_num < 4:
                situacao = salas[sala_num][periodo_num]
                status = "disponível" if situacao == 0 else "ocupado"
                print(f"A sala {sala_num + 1}, período {periodo_num + 1} está {status}.")
                break
            else:
                print("Número de sala ou período inválido. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite números válidos.")

def contar_disponiveis():
    if not salas:
        print("Nenhuma sala cadastrada. Cadastre as salas primeiro.")
        return
    print("\n=== Horários Disponíveis por Sala ===")
    for i, sala in enumerate(salas):
        disponiveis = sala.count(0)
        print(f"Sala {i+1}: {disponiveis} horários disponíveis.")

while True:
    print("\n=== Sistema de Controle de Salas de Reunião ===")
    print("1. Cadastrar salas")
    print("2. Apresentar salas")
    print("3. Verificar disponibilidade")
    print("4. Contar horários disponíveis")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        cadastrar_salas()
    elif opcao == "2":
        apresentar_salas()
    elif opcao == "3":
        verificar_disponibilidade()
    elif opcao == "4":
        contar_disponiveis()
    elif opcao == "5":
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")

