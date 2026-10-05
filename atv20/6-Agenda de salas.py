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



#lista para armazenar a situação das salas de reunião
salas = []

#função para cadastrar salas, onde são solicitadas as informações necessárias e validadas
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

#função para apresentar as salas, verificando se a lista está vazia e exibindo a situação de cada sala e período
def apresentar_salas():
    if not salas:
        print("Nenhuma sala cadastrada. Cadastre as salas primeiro.")
        return
    print("\n=== Salas de Reunião ===")
    for i, sala in enumerate(salas):
        print(f"Sala {i+1}: {sala}")
#função para verificar a disponibilidade de uma sala em um período específico, 
# solicitando ao usuário a sala e o período desejados e informando se está disponível ou ocupado
def verificar_disponibilidade():
    #verifica se a lista de salas está vazia, caso esteja, solicita ao usuário que cadastre as salas primeiro
    if not salas:
        print("Nenhuma sala cadastrada. Cadastre as salas primeiro.")
        return
    #loop para solicitar a sala e o período desejados, garantindo que os valores estejam dentro do intervalo válido
    while True:
        try:
            # Solicitar a sala e o período desejados, subtraindo 1 para ajustar ao índice da lista
            sala_num = int(input("Digite o número da sala (1-3): ")) - 1
            periodo_num = int(input("Digite o período (1-4): ")) - 1
            #verifica se os valores digitados estão dentro do intervalo válido (0 a 2 para sala e 0 a 3 para período)
            if 0 <= sala_num < 3 and 0 <= periodo_num < 4:
                situacao = salas[sala_num][periodo_num]
                status = "disponível" if situacao == 0 else "ocupado"
                print(f"A sala {sala_num + 1}, período {periodo_num + 1} está {status}.")
                break
            else:
                print("Número de sala ou período inválido. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite números válidos.")
#função para contar horários disponíveis em cada sala, percorrendo a lista de salas e contando quantos períodos 
# estão disponíveis (0) em cada sala
def contar_disponiveis():
#verifica se a lista de salas está vazia, caso esteja, solicita ao usuário que cadastre as salas primeiro
    if not salas:
        print("Nenhuma sala cadastrada. Cadastre as salas primeiro.")
        return
    print("\n=== Horários Disponíveis por Sala ===")
    for i, sala in enumerate(salas):
        disponiveis = sala.count(0)
        print(f"Sala {i+1}: {disponiveis} horários disponíveis.")

#menu principal do programa, onde o usuário pode escolher entre cadastrar salas, apresentar salas cadastradas,
# verificar disponibilidade de uma sala em um período específico, contar horários disponíveis em cada 
# sala ou sair do programa

while True:
    #exibe o menu principal com as opções disponíveis para o usuário
    print("\n=== Sistema de Controle de Salas de Reunião ===")
    print("1. Cadastrar salas")
    print("2. Apresentar salas")
    print("3. Verificar disponibilidade")
    print("4. Contar horários disponíveis")
    print("5. Sair")
    #solicita ao usuário que escolha uma opção do menu e executa a função correspondente com base na escolha
    
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

