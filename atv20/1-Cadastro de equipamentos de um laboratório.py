'''Um laboratório de informática precisa manter o controle dos equipamentos
disponíveis.
Cada equipamento possui informações diferentes e, por isso, o sistema deverá
armazenar um conjunto de dados para cada equipamento.
Para cada equipamento, deverão ser armazenados:
• código do equipamento;
• nome;
• tipo;
• quantidade;
• situação.
Exemplo:
equipamento = {
"codigo": 101,
"nome": "Computador Dell",
"tipo": "Desktop",
"quantidade": 20,
"situacao": "Disponível"
}
Desenvolva um programa que:

• crie uma lista vazia chamada equipamentos;
• cadastre 3 equipamentos;
• solicite todas as informações ao usuário;
• utilize um dicionário para representar cada equipamento;
• utilize append() para adicionar cada equipamento à lista;
• ao final, percorra a lista e apresente todos os equipamentos cadastrados.
O código deverá funcionar como identificador do equipamento.'''

# criando a lista de equipamentos vazia
equipamentos = []
#duas variaveis globais para controlar a quantidade de equipamentos cadastrados e o codigo do equipamento
numDeq = 0
codigo = 0
#definindo a função para cadastrar equipamentos
def cad_equip():
    #global denovo devido ao maldito escopo de variaveis, para poder alterar o valor da variavel global dentro da função
    global numDeq
    global codigo
    global nome
    global quantidade 
    global situacao

    #enquanto o numero de equipamentos cadastrados for menor que 3, ele vai continuar pedindo para cadastrar
    while numDeq <3:
        print("========Cadastro de equipamentos========")
        print()

        #enquanto o usuario nao digitar um numero, ele vai continuar pedindo para digitar o codigo do equipamento
        while True:
            try:
            #se o usuario digitar um valor que nao seja numerico, ele vai mostrar uma mensagem de erro e pedir para digitar novamente
                codigo = int(input(f"Digite o número de código do {numDeq+1}º equipamento: "))      
                break
            except ValueError:
                print("CODIGO precisa ser númeral")  

        #enquanto o usuario nao digitar um valor que seja apenas letras, ele vai continuar pedindo para digitar o nome do equipamento
        while True:
            nome = input(f"Digite o nome do {numDeq+1}º equipamento: ")
            #se o usuario digitar um valor que seja apenas numeros, ele vai mostrar uma mensagem de erro e pedir para digitar novamente
            if nome.isdigit():
                print("Nome precisa ser com letras")
            else:
                break

        #enquanto o usuario nao digitar um valor que seja apenas letras, ele vai continuar pedindo para digitar o tipo do equipamento
        while True:
            tipo = input(f"Digite o tipo do {numDeq+1}º equipamento: ")
            if tipo.isdigit():
                print("TIPO precisa ser com letras")
            else:
                break

        #enquanto o usuario nao digitar um numero, ele vai continuar pedindo para digitar a quantidade do equipamento
        while True:
            try:
                quantidade = int(input(f"Digite a quantidade do {numDeq+1}º equipamento: "))      
                break
            except ValueError:
                print("QUANTIDADE precisa ser númeral")  

        #enquanto o usuario nao digitar um valor que seja apenas letras, ele vai continuar pedindo para digitar a situacao do equipamento
        while True:
            situacao = input(f"Digite a situação do {numDeq+1}º equipamento: ")

            if situacao.isdigit():
                print("SITUAÇÃO precisa ser com letras")
            else:
                break

        #incrementa o numero de equipamentos cadastrados a cada cadastro realizado, para que o while principal saiba quando parar de pedir para cadastrar
        numDeq += 1

    
        #cria um dicionário para armazenar as informações do equipamento e adiciona o dicionário à lista de equipamentos
        equipamento = {
            "cOdigo": codigo,
            "nOme": nome,
            "tIpo": tipo,
            "qUantidade": quantidade,
            "sItuacao": situacao
        }
        equipamentos.append(equipamento)
#mostrar os equipamentos cadastrados
def mOs_equip():
    if len(equipamentos) ==0:
        print("Nenhum equipamento registrado ainda")
        
    else:
        print("Equipamentos cadastrados:")
        for equip in equipamentos:
            print(equip)
#menu principal do sistema, que vai ficar em loop até o usuario digitar 0 para sair
while True:
    print("======Menu Principal======")
    print()
    if numDeq == 3:
        print("numero máximo de cadastros atingidos(ecercicio pede 3)")
    print("1-Cadastrar equipamento")
    print("2-Solicitar informação dos equipamentos")
    print("0-para sair")
    oPc= input("Oque deseja fazer hoje?: ")

    if oPc == "1":
        cad_equip()
    elif oPc == "2":
        mOs_equip()
    elif oPc == "0":
         break
    else:
        print("======Opção inválida!, tente novamente======")

print("Saindo.....")

     