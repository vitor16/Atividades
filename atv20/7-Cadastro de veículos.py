'''Uma empresa possui uma frota de veículos e precisa controlar seus dados.
Cada veículo deverá possuir:
• código;
• placa;
• modelo;
• marca;
• ano;
• quilometragem;
• situação.
Exemplo:
veiculo = {
"codigo": 1,
"placa": "ABC1D23",
"modelo": "Onix",
"marca": "Chevrolet",
"ano": 2024,
"quilometragem": 35000,
"situacao": "Disponível"
}
Desenvolva um programa que:
• cadastre 4 veículos;
• armazene os veículos em uma lista;
• utilize append();
• apresente todos os veículos;

• solicite uma placa;
• localize o veículo pela placa;
• apresente seus dados.
Ao final, informe também qual veículo possui a maior quilometragem.'''

#lista para armazenar os veículos
veiculos = []
#função para cadastrar os veículos
def cadastrar_veiculos():
    veiculos = []
    #loop para cadastrar 4 veículos
    for i in range(4):
        print(f"\nCadastro do veículo {i+1}:")
        codigo = int(input("Digite o código do veículo: "))
        placa = input("Digite a placa do veículo: ")
        modelo = input("Digite o modelo do veículo: ")
        marca = input("Digite a marca do veículo: ")
        ano = int(input("Digite o ano do veículo: "))
        quilometragem = float(input("Digite a quilometragem do veículo: "))
        situacao = input("Digite a situação do veículo (Disponível/Ocupado): ")
# cria um dicionário para armazenar os dados do veículo e adiciona à lista de veículos
        veiculo = {
            "codigo": codigo,
            "placa": placa,
            "modelo": modelo,
            "marca": marca,
            "ano": ano,
            "quilometragem": quilometragem,
            "situacao": situacao
        }
        veiculos.append(veiculo)
    return veiculos

#função para apresentar os veículos cadastrados, percorrendo a lista de veículos e exibindo seus dados

def apresentar_veiculos(veiculos):
    print("\n=== Veículos Cadastrados ===")
    for veiculo in veiculos:
        print(f"Código: {veiculo['codigo']}, Placa: {veiculo['placa']}, Modelo: {veiculo['modelo']}, "
              f"Marca: {veiculo['marca']}, Ano: {veiculo['ano']}, Quilometragem: {veiculo['quilometragem']}, "
              f"Situação: {veiculo['situacao']}")

#função para localizar um veículo pela placa, percorrendo a lista de veículos e comparando a
# placa informada pelo usuário com a placa de cada veículo

def localizar_veiculo_por_placa(veiculos):
    placa_procurada = input("\nDigite a placa do veículo que deseja localizar: ")
    for veiculo in veiculos:
        if veiculo['placa'] == placa_procurada:
            print(f"\nVeículo encontrado:\nCódigo: {veiculo['codigo']}, Placa: {veiculo['placa']}, "
                  f"Modelo: {veiculo['modelo']}, Marca: {veiculo['marca']}, Ano: {veiculo['ano']}, "
                  f"Quilometragem: {veiculo['quilometragem']}, Situação: {veiculo['situacao']}")
            return
    print("Veículo não encontrado.")

#função para encontrar o veículo com a maior quilometragem, utilizando a função max() com uma função lambda

def veiculo_maior_quilometragem(veiculos):
    if not veiculos:
        print("Nenhum veículo cadastrado.")
        return
    maior_veiculo = max(veiculos, key=lambda v: v['quilometragem'])
    print(f"\nVeículo com a maior quilometragem:\nCódigo: {maior_veiculo['codigo']}, Placa: {maior_veiculo['placa']}, "
          f"Modelo: {maior_veiculo['modelo']}, Marca: {maior_veiculo['marca']}, Ano: {maior_veiculo['ano']}, "
          f"Quilometragem: {maior_veiculo['quilometragem']}, Situação: {maior_veiculo['situacao']}")

#menu principal do programa, onde o usuário pode escolher entre cadastrar veículos, apresentar veículos cadastrados,
# localizar veículo por placa, encontrar veículo com maior quilometragem ou sair do programa

while True:
    print("\n=== Menu ===")
    print("1. Cadastrar veículos")
    print("2. Apresentar veículos")
    print("3. Localizar veículo por placa")
    print("4. Veículo com maior quilometragem")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        veiculos = cadastrar_veiculos()
    elif opcao == '2':
        apresentar_veiculos(veiculos)
    elif opcao == '3':
        localizar_veiculo_por_placa(veiculos)
    elif opcao == '4':
        veiculo_maior_quilometragem(veiculos)
    elif opcao == '5':
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")
