'''Uma empresa precisa desenvolver um pequeno sistema para controlar seu
estoque.
Para cada produto, o sistema deverá armazenar:
• código do produto;
• nome;
• categoria;
• quantidade atual;
• quantidade mínima;
• preço.
Exemplo:
produto = {
"codigo": 101,
"nome": "Teclado",
"categoria": "Periféricos",
"quantidade": 15,
"quantidade_minima": 5,
"preco": 120.00
}
Desenvolva um programa que:

• crie uma lista vazia chamada estoque;
• permita cadastrar 5 produtos;
• solicite todas as informações ao usuário;
• utilize append() para armazenar cada produto;
• percorra os produtos cadastrados;
• apresente os dados de cada produto;
• informe quais produtos estão abaixo ou iguais à quantidade mínima.
Exemplo de resultado:
PRODUTOS QUE NECESSITAM DE REPOSIÇÃO

Código: 103
Produto: Mouse
Quantidade atual: 3
Quantidade mínima: 5
O código deverá ser utilizado como identificador do produto.'''

estoque = []
numDestq = 0
def aDd_estq():
    #global denovo devido ao maldito escopo de variaveis, para poder alterar o valor da variavel global dentro da função
        global numDestq
        global codigo
        global nome
        global quantidade 
        global situacao
    
        #enquanto o numero de equipamentos cadastrados for menor que 3, ele vai continuar pedindo para cadastrar
        while numDeq <5:
            print("========Cadastro de estoque========")
            print()
    
            #enquanto o usuario nao digitar um numero, ele vai continuar pedindo para digitar o codigo do equipamento
            while True:
                try:
                #se o usuario digitar um valor que nao seja numerico, ele vai mostrar uma mensagem de erro e pedir para digitar novamente
                    codigo = int(input(f"Digite o número de código do {numDestq+1}º produto: "))      
                    break
                except ValueError:
                    print("CODIGO precisa ser númeral")  
    
            #enquanto o usuario nao digitar um valor que seja apenas letras, ele vai continuar pedindo para digitar o nome do equipamento
            while True:
                nome = input(f"Digite o nome do {numDestq+1}º produto: ")
                #se o usuario digitar um valor que seja apenas numeros, ele vai mostrar uma mensagem de erro e pedir para digitar novamente
                if nome.isdigit():
                    print("Nome precisa ser com letras")
                else:
                    break
    
            #enquanto o usuario nao digitar um valor que seja apenas letras, ele vai continuar pedindo para digitar o tipo do equipamento
            while True:
                tipo = input(f"Digite a categoria do {numDestq+1}º produto: ")
                if tipo.isdigit():
                    print("TIPO precisa ser com letras")
                else:
                    break
    
            #enquanto o usuario nao digitar um numero, ele vai continuar pedindo para digitar a quantidade do equipamento
            while True:
                try:
                    quantidade = int(input(f"Digite a quantidade do {numDestq+1}º produto: "))      
                    break
                except ValueError:
                    print("QUANTIDADE precisa ser númeral")  
    
            #enquanto o usuario nao digitar um valor que seja apenas letras, ele vai continuar pedindo para digitar a situacao do equipamento
            while True:
                quantidade_minima = input(f"Digite a quantidade mínima do {numDestq+1}º produto: ")
    
                if situacao.isdigit():
                    print("SITUAÇÃO precisa ser com letras")
                else:
                    break

            numDestq += 1
            
                
                    #cria um dicionário para armazenar as informações do equipamento e adiciona o dicionário à lista de equipamentos
            items = {
                        "cOdigo": codigo,
                        "nOme": nome,
                        "tIpo": tipo,
                        "qUantidade": quantidade,
                        "sItuacao": quantidade_minima
                }
            estoque.append(items)
def mOs_estq():
    if len(estoque) ==0:
        print("Nenhum item registrado ainda")
        
    else:
        print("Equipamentos cadastrados:")
        for equip in estoque:
            print(equip)
def saIda():
    print("saindo...")
    exit()
while True:
    print("========Menu Principal========")
    print()
    print("1-Adicionar item ao estoque")
    print("2-Checar quantidade no estoque")
    print("0-sair")
    print()        
    opcao= input("oque deseja fazer hoje: ")
    if opcao == "1":
        aDd_estq()
    elif opcao == "2":



    