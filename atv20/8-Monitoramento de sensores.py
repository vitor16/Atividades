'''Uma empresa utiliza sensores para monitorar a temperatura de diferentes
ambientes.
Existem:
• 3 ambientes;
• 4 sensores em cada ambiente.
Utilize uma matriz para armazenar as temperaturas.
Exemplo:
temperaturas = [
[22.5, 23.1, 22.8, 24.0],
[25.2, 26.0, 25.5, 24.8],
[20.5, 21.0, 20.8, 21.5]
]
Desenvolva um programa que:
• solicite as temperaturas;
• construa a matriz utilizando append();
• apresente a matriz;
• calcule a média de cada ambiente;
• identifique a maior temperatura registrada;
• identifique a menor temperatura registrada.
Ao final, apresente os resultados organizados por ambiente.'''

#lista para armazenar as temperaturas dos ambientes
temperaturas = []

#funcao para cadastrar temperaturas.
def cad_temp():
    #loop de for para percorrer os 3 ambientes
    for i in range(3):
        #loop de for para percorrer os 4 sensores de cada ambiente
        ambiente = []
        for j in range(4):
            while True:
                try:
                    #solicita a temperatura do ambiente e sensor, e adiciona à lista de ambiente
                    temp = float(input(f"Digite a temperatura do ambiente {i+1}, sensor {j+1}: "))
                    ambiente.append(temp)
                    break
                except ValueError:
                    print("Valor inválido. Digite um número válido para a temperatura.")
        #adiciona a lista de ambiente à lista de temperaturas
        temperaturas.append(ambiente)
#função para apresentar as temperaturas cadastradas, percorrendo a lista de temperaturas e exibindo seus dados
def apresentar_temp():
    #se temperaturas estiver vazia, exibe mensagem de erro e retorna
    if not temperaturas:
        print("Nenhuma temperatura cadastrada. Cadastre as temperaturas primeiro.")
        return
    #exibe as temperaturas cadastradas, percorrendo a lista de temperaturas e exibindo seus dados
    print("\n=== Temperaturas dos Ambientes ===")
    for i, ambiente in enumerate(temperaturas):
        print(f"Ambiente {i+1}: {ambiente}")
#função para calcular a média de cada ambiente, percorrendo a lista de temperaturas e exibindo seus dados
def mEd_amb():
    if not temperaturas:
        print("Nenhuma temperatura cadastrada. Cadastre as temperaturas primeiro.")
        return
    print("\n=== Média de Temperaturas por Ambiente ===")
    for i, ambiente in enumerate(temperaturas):
        #pega a média das temperaturas de cada ambiente e exibe o resultado
        media = sum(ambiente) / len(ambiente)
        print(f"Ambiente {i+1}: Média = {media:.2f}°C")
#função para identificar a maior e menor temperatura registrada, percorrendo a lista de temperaturas e exibindo seus dados
def maior_menor_temp():
    if not temperaturas:#se temperaturas estiver vazia, exibe mensagem de erro e retorna
        print("Nenhuma temperatura cadastrada. Cadastre as temperaturas primeiro.")
        return
    # guarda todas as temperaturas em uma lista única, e utiliza as funções max() e min() para
    #  identificar a maior e menor temperatura registrada e em seguida exibe o resultado
    #guardando o maior na variável maior e o menor na variável menor

    todas_temperaturas = [temp for ambiente in temperaturas for temp in ambiente]
    maior = max(todas_temperaturas)
    menor = min(todas_temperaturas)
    print(f"\n=== Maior e Menor Temperaturas ===")
    print(f"Maior temperatura registrada: {maior:.2f}°C")
    print(f"Menor temperatura registrada: {menor:.2f}°C")
#menu principal
while True:
    print("\n=== Monitoramento de Sensores ===")
    print("1. Cadastrar Temperaturas")
    print("2. Apresentar Temperaturas")
    print("3. Calcular Média de Cada Ambiente")
    print("4. Identificar Maior e Menor Temperatura")
    print("5. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cad_temp()
    elif opcao == "2":
        apresentar_temp()
    elif opcao == "3":
        mEd_amb()
    elif opcao == "4":
        maior_menor_temp()
    elif opcao == "5":
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")