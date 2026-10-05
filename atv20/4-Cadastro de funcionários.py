'''Uma empresa deseja armazenar informações básicas dos funcionários.
Cada funcionário deverá possuir:
• matrícula;
• nome;
• setor;
• cargo;
• salário.
Exemplo:
funcionario = {
"matricula": 1001,
"nome": "Carlos",
"setor": "Tecnologia",

"cargo": "Desenvolvedor",
"salario": 4500.00
}
Desenvolva um programa que:
• cadastre 5 funcionários;
• utilize uma lista para armazená-los;
• utilize append() para adicionar cada funcionário;
• ao final, apresente os funcionários cadastrados;
• solicite uma matrícula;
• localize o funcionário correspondente;
• apresente os dados encontrados.
A matrícula deverá funcionar como identificador único.'''

#lista para armazenar os funcionários cadastrados
empresa = []
#função para cadastrar funcionários, onde são solicitadas as informações necessárias e validadas
def cadastrar_funcionario():
    #variável matricula é inicializada como None para garantir que o loop de entrada seja executado
    matricula = None
    while True:
        try:
            # Solicitar a matrícula do funcionário e verificar se já existe na lista de funcionários
            matricula = int(input("Digite a matrícula do funcionário: "))
            #if any(funcionario["matricula"] == matricula for funcionario in empresa) 
            # verifica se a matrícula já existe na lista de funcionários
            #any() retorna True se algum elemento da lista satisfizer a condição, caso contrário, retorna False
            if any(funcionario["matricula"] == matricula for funcionario in empresa):
                print("Matrícula já cadastrada. Digite outra.")
                continue
            break
        except ValueError:
            print("Matrícula precisa ser numérica.")
    #loop para solicitar o nome do funcionário, garantindo que não seja vazio ou numérico
    while True:
        nome = input("Digite o nome do funcionário: ")
        if nome.strip() and not nome.isdigit():
            break
        print("Nome inválido. Digite um nome válido.")
#loop para solicitar o setor do funcionário, garantindo que não seja vazio ou numérico
    while True:
        setor = input("Digite o setor do funcionário: ")
        if setor.strip() and not setor.isdigit():
            break
        print("Setor inválido. Digite um nome válido.")
#loop para solicitar o cargo do funcionário, garantindo que não seja vazio ou numérico
    while True:
        cargo = input("Digite o cargo do funcionário: ")
        if cargo.strip() and not cargo.isdigit():
            break
        print("Cargo inválido. Digite um nome válido.")
#loop para solicitar o salário do funcionário, garantindo que seja numérico
    while True:
        try:
            salario = float(input("Digite o salário do funcionário: "))
            break
        except ValueError:
            print("Salário precisa ser numérico.")
#criação do dicionário funcionario com as informações fornecidas pelo usuário,
# e adição do dicionário à lista empresa usando append()
    funcionario = {
        "matricula": matricula,
        "nome": nome,
        "setor": setor,
        "cargo": cargo,
        "salario": salario
    }
    empresa.append(funcionario)
    print("\nFuncionário cadastrado com sucesso!")

#função para apresentar os funcionários cadastrados, verificando se a lista está vazia e exibindo as informações de cada funcionário
def apresentar_funcionarios():
    if not empresa:
        print("Nenhum funcionário cadastrado.")
        return
    else:
        print("\n=== Funcionários Cadastrados ===")
        for funcionario in empresa:
            print(f"Matrícula: {funcionario['matricula']}, Nome: {funcionario['nome']}, Setor: {funcionario['setor']}, Cargo: {funcionario['cargo']}, Salário: {funcionario['salario']}")
#função para localizar um funcionário pela matrícula, percorrendo a lista de funcionários e 
# retornando o dicionário correspondente se encontrado, ou None caso contrário
def localizar_funcionario(matricula):
    for funcionario in empresa:
        if funcionario["matricula"] == matricula:
            return funcionario
    return None
# Loop principal do programa, onde o usuário pode escolher entre cadastrar funcionários, apresentar funcionários cadastrados, 
# localizar um funcionário por matrícula ou sair do programa.


while True:
    print("\n=== Sistema de Cadastro de Funcionários ===")
    print("1. Cadastrar funcionário")
    print("2. Apresentar funcionários cadastrados")
    print("3. Localizar funcionário por matrícula")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        if len(empresa) < 5:
            cadastrar_funcionario()
        else:
            print("Limite de funcionários cadastrados atingido.")
    elif opcao == "2":
        apresentar_funcionarios()
    elif opcao == "3":
        try:
            matricula = int(input("Digite a matrícula do funcionário a ser localizado: "))
            funcionario = localizar_funcionario(matricula)
            if funcionario:
                print(f"Funcionário encontrado: Matrícula: {funcionario['matricula']}, Nome: {funcionario['nome']}, Setor: {funcionario['setor']}, Cargo: {funcionario['cargo']}, Salário: {funcionario['salario']}")
            else:
                print("Funcionário não encontrado.")
        except ValueError:
            print("Matrícula precisa ser numérica.")
    elif opcao == "4":
        print("Saindo do sistema.")
        break